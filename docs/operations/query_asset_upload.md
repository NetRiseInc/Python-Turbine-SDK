<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# query_asset_upload

[Back to the index](../README.md)

Get a pre-signed URL to upload a file for analysis.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |
| `asset_upload_args` | `Union[AssetUploadInput, None, UnsetType]` | `false` |

## Response fields

Typed attributes on the response model.

| Field | Type | Nullable |
| --- | --- | --- |
| `assetUpload` | `object` | yes |
| `assetUpload.assetId` | `string` | yes |
| `assetUpload.uploadId` | `string` | yes |
| `assetUpload.uploaded` | `boolean` | yes |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    AssetUploadInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_asset_upload(asset_upload_args=AssetUploadInput())
        # Responses are typed Pydantic models: read fields as attributes.
        print(resp.asset_upload.asset_id, resp.asset_upload.upload_id)


if __name__ == "__main__":
    main()
```
