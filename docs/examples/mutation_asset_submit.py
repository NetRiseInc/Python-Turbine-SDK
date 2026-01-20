"""Example: Upload a firmware or SBOM file to Turbine for analysis.

This example demonstrates:
1. Configuring the SDK client
2. Submitting an asset with metadata
3. Uploading the file to the pre-signed URL
4. Checking upload status
5. Accessing the created asset information

Usage:
    python mutation_asset_submit.py <file_path> [options]

Examples:
    # Upload firmware with minimal metadata
    python mutation_asset_submit.py firmware.bin

    # Upload firmware with full metadata
    python mutation_asset_submit.py firmware.bin \\
        --name "Router Firmware" \\
        --vendor "Acme Corp" \\
        --product "ACME-Router" \\
        --version "2.1.0" \\
        --asset-cpe "cpe:2.3:h:acme:acme-router:2.1.0:*:*:*:*:*:*:*" \\
        --asset-group-ids group-id-123 group-id-456

    # Upload SBOM
    python mutation_asset_submit.py sbom.json \\
        --name "Application SBOM" \\
        --vendor "My Company" \\
        --sbom-type CYCLONEDX \\
        --sbom-format JSON
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import httpx
from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql import (
    AssetType,
    SbomFormat,
    SbomType,
    SubmitAssetInput,
)


def upload_asset(
    file_path: str | Path,
    *,
    name: str | None = None,
    vendor: str | None = None,
    product: str | None = None,
    version: str | None = None,
    asset_cpe: str | None = None,
    asset_group_ids: list[str] | None = None,
    sbom_type: SbomType | None = None,
    sbom_format: SbomFormat | None = None,
    timeout: float = 300.0,
) -> str | None:
    """Upload a firmware or SBOM file to Turbine.

    Args:
        file_path: Path to the file to upload (firmware image or SBOM file)
        name: Optional name for the asset
        vendor: Optional vendor/manufacturer name
        product: Optional product name
        version: Optional version string
        asset_cpe: Optional CPE (Common Platform Enumeration) identifier
        asset_group_ids: Optional list of asset group IDs to assign this asset to
        sbom_type: Optional SBOM type (CYCLONEDX or SPDX) - required for SBOM uploads
        sbom_format: Optional SBOM format (JSON, XML, etc.) - required for SBOM uploads
        timeout: HTTP timeout in seconds for file upload

    Returns:
        Asset ID of the created asset, or None if the upload succeeded but asset
        is still processing (you can check status later using query_asset_upload)

    Raises:
        FileNotFoundError: If the file doesn't exist
        httpx.HTTPStatusError: If the upload fails
        ValueError: If required SBOM fields are missing

    Example:
        >>> # Upload firmware
        >>> asset_id = upload_asset(
        ...     "firmware.bin",
        ...     name="Router Firmware",
        ...     vendor="Acme Corp",
        ...     product="ACME-Router",
        ...     version="2.1.0",
        ...     asset_cpe="cpe:2.3:h:acme:acme-router:2.1.0:*:*:*:*:*:*:*",
        ...     asset_group_ids=["group-id-123"]
        ... )
        >>> print(f"Asset created: {asset_id}")

        >>> # Upload SBOM
        >>> asset_id = upload_asset(
        ...     "sbom.json",
        ...     name="Application SBOM",
        ...     vendor="My Company",
        ...     sbom_type=SbomType.CYCLONEDX,
        ...     sbom_format=SbomFormat.JSON
        ... )
    """
    file_path = Path(file_path)
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    # Load configuration from environment variables (.env file)
    # Ensure you have a .env file with the required variables:
    # endpoint=https://apollo.turbine.netrise.io/graphql/v3
    # audience=https://prod.turbine.netrise.io/
    # domain=https://authn.turbine.netrise.io
    # client_id=<your_client_id>
    # client_secret=<your_client_secret>
    # organization_id=<your_org_id>
    cfg = TurbineClientConfig.from_env()
    client = TurbineClient(cfg)

    # Prepare metadata for the asset
    submit_args = SubmitAssetInput(
        name=name or file_path.stem,
        manufacturer=vendor,
        model=product,
        version=version,
        asset_cpe=asset_cpe,
        asset_group_ids=asset_group_ids,
        sbom_type=sbom_type,
        sbom_format=sbom_format,
    )

    with client.graphql() as gql_client:
        # Step 1: Request upload URL from Turbine
        print(f"Requesting upload URL for {file_path.name}...")
        response = gql_client.mutation_asset_submit(
            asset_submit_file_name=file_path.name,
            asset_submit_args=submit_args,
        )

        submit_result = response.asset.submit
        upload_url = submit_result.upload_url
        upload_id = submit_result.upload_id

        print(f"Received upload URL (upload_id: {upload_id})")
        print(f"Upload URL: {upload_url[:80]}...")

        # Step 2: Upload the file to the pre-signed URL
        file_size = file_path.stat().st_size
        print(f"Uploading {file_path} ({file_size:,} bytes)...")

        with open(file_path, "rb") as f:
            # Use httpx to upload directly to the pre-signed URL
            # Use a longer timeout for large files
            with httpx.Client(timeout=timeout) as http_client:
                upload_response = http_client.put(
                    upload_url,
                    content=f.read(),
                    headers={"Content-Type": "application/octet-stream"},
                )
                upload_response.raise_for_status()

        print("✓ File uploaded successfully!")

        # Step 3: Check upload status and return asset ID
        if submit_result.asset and submit_result.asset.id:
            asset_id = submit_result.asset.id
            print(f"✓ Asset created with ID: {asset_id}")
            print(f"  Status: {submit_result.asset.status}")
            if submit_result.asset.sha_256:
                print(f"  SHA256: {submit_result.asset.sha_256}")

            if submit_result.asset.risk:
                risk = submit_result.asset.risk
                print(f"  Risk Category: {risk.category}")
                if risk.score is not None:
                    print(f"  Risk Score: {risk.score}")

            return asset_id
        else:
            # Asset might still be processing - check status separately
            print("Checking upload status...")
            from netrise_turbine_sdk_graphql import AssetUploadInput

            upload_status = gql_client.query_asset_upload(
                asset_upload_args=AssetUploadInput(upload_id=upload_id)
            )

            if upload_status.asset_upload.uploaded:
                asset_id = upload_status.asset_upload.asset_id
                print(f"✓ Upload confirmed (asset_id: {asset_id})")
                return asset_id
            else:
                print("⏳ Upload completed successfully, but asset is still processing.")
                print(f"\n📋 Upload ID: {upload_id}")
                print(
                    "   The file has been uploaded successfully. Turbine is processing "
                    "the asset and will create it shortly."
                )
                print(
                    "   You can check the upload status later using query_asset_upload "
                    f"with upload_id: {upload_id}"
                )
                return None


def main() -> None:
    """Main entry point - parses arguments and uploads file."""
    parser = argparse.ArgumentParser(
        description="Upload a firmware or SBOM file to Turbine for analysis",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )

    parser.add_argument(
        "file_path",
        type=Path,
        help="Path to the file to upload (firmware or SBOM)",
    )

    # Metadata options
    parser.add_argument("--name", help="Name for the asset")
    parser.add_argument("--vendor", "--manufacturer", help="Vendor/manufacturer name")
    parser.add_argument("--product", "--model", help="Product/model name")
    parser.add_argument("--version", help="Version string")

    # Asset identification
    parser.add_argument(
        "--asset-cpe",
        dest="asset_cpe",
        help="CPE (Common Platform Enumeration) identifier",
    )

    # Asset groups
    parser.add_argument(
        "--asset-group-ids",
        nargs="+",
        dest="asset_group_ids",
        help="Asset group IDs to assign this asset to",
    )

    # SBOM-specific options
    parser.add_argument(
        "--sbom-type",
        type=lambda x: SbomType[x.upper()],
        choices=list(SbomType),
        help="SBOM type (CYCLONEDX or SPDX) - required for SBOM uploads",
    )
    parser.add_argument(
        "--sbom-format",
        type=lambda x: SbomFormat[x.upper()],
        choices=list(SbomFormat),
        help="SBOM format (JSON, XML, etc.) - required for SBOM uploads",
    )

    # Advanced options
    parser.add_argument(
        "--timeout",
        type=float,
        default=300.0,
        help="HTTP timeout in seconds for file upload (default: 300.0)",
    )

    args = parser.parse_args()

    try:
        asset_id = upload_asset(
            args.file_path,
            name=args.name,
            vendor=args.vendor,
            product=args.product,
            version=args.version,
            asset_cpe=args.asset_cpe,
            asset_group_ids=args.asset_group_ids,
            sbom_type=args.sbom_type,
            sbom_format=args.sbom_format,
            timeout=args.timeout,
        )
        if asset_id:
            print(f"\n✅ Success! Asset ID: {asset_id}")
        else:
            print("\n✅ File uploaded successfully! Asset is processing...")
        sys.exit(0)
    except FileNotFoundError as e:
        print(f"❌ Error: {e}", file=sys.stderr)
        sys.exit(1)
    except httpx.HTTPStatusError as e:
        print(f"❌ HTTP Error: {e.response.status_code}", file=sys.stderr)
        print(f"   Response: {e.response.text[:200]}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error: {e}", file=sys.stderr)
        import traceback

        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
