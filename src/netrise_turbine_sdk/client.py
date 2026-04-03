from __future__ import annotations

import os
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Optional

import httpx
from dotenv import find_dotenv, load_dotenv

# The generated client will live in this module after `ariadne-codegen` runs.
# It is intentionally a separate top-level package so it won't overwrite
# handwritten wrapper code.
from netrise_turbine_sdk_graphql import Client as GeneratedClient


@dataclass(frozen=True)
class TurbineClientConfig:
    endpoint: str

    # Client credentials
    domain: Optional[str] = None
    client_id: Optional[str] = None
    client_secret: Optional[str] = None
    audience: Optional[str] = None
    organization_id: Optional[str] = None

    # Manual token override
    turbine_api_token: Optional[str] = None

    @staticmethod
    def from_env(load_env_file: bool = True) -> "TurbineClientConfig":
        """Load config from environment variables.

        If `load_env_file` is True, automatically loads a `.env` file from:
        - Current working directory (most common)
        - Parent directories (walks up the directory tree)

        Environment variables can also be set directly without a `.env` file.
        Set `load_env_file=False` to disable automatic `.env` file loading.
        """
        if load_env_file:
            # Prioritize .env file in current working directory
            # This ensures local .env files take precedence over parent directories
            current_dir_env = Path.cwd() / ".env"
            if current_dir_env.exists():
                load_dotenv(current_dir_env, override=False)
            else:
                # If no .env in current directory, search parent directories
                dotenv_path = find_dotenv(usecwd=True)
                if dotenv_path:
                    load_dotenv(dotenv_path, override=False)
                else:
                    # Fallback to default behavior if find_dotenv doesn't find anything
                    load_dotenv(override=False)

        endpoint = (os.getenv("endpoint") or "").strip()
        if not endpoint:
            raise ValueError(
                "endpoint is required (e.g. https://apollo.turbine.netrise.io/graphql/v3)"
            )

        return TurbineClientConfig(
            endpoint=endpoint,
            domain=_strip_or_none(os.getenv("domain")),
            client_id=_strip_or_none(os.getenv("client_id")),
            client_secret=_strip_or_none(os.getenv("client_secret")),
            audience=_strip_or_none(os.getenv("audience")),
            organization_id=_strip_or_none(os.getenv("organization_id")),
            turbine_api_token=_strip_or_none(os.getenv("TURBINE_API_TOKEN")),
        )


class TurbineClient:
    """Sync-first Turbine GraphQL client.

    - Uses `TURBINE_API_TOKEN` if provided.
    - Otherwise uses client credentials to fetch a token.

    The underlying request execution is provided by the generated client from
    `ariadne-codegen`.
    """

    def __init__(
        self,
        config: TurbineClientConfig,
        *,
        timeout: float = 30.0,
        httpx_client: Optional[httpx.Client] = None,
    ) -> None:
        self._config = config
        self._timeout = timeout
        self._httpx_client = httpx_client

        self._cached_token: Optional[str] = None
        self._cached_token_expires_at: float = 0.0

    @property
    def config(self) -> TurbineClientConfig:
        return self._config

    def _get_auth_header(self) -> Dict[str, str]:
        token = self._get_token()
        if not token.startswith("Bearer "):
            token = f"Bearer {token}"
        return {"Authorization": token}

    def _get_token(self) -> str:
        # 1) Manual token override
        if self._config.turbine_api_token:
            return self._config.turbine_api_token

        # 2) Cached token
        now = time.time()
        if self._cached_token and now < self._cached_token_expires_at:
            return self._cached_token

        # 3) Fetch via client credentials
        token, expires_in = _fetch_token(
            domain=self._config.domain,
            client_id=self._config.client_id,
            client_secret=self._config.client_secret,
            audience=self._config.audience,
            organization_id=self._config.organization_id,
            timeout=self._timeout,
        )

        # Cache with a small safety buffer.
        self._cached_token = token
        self._cached_token_expires_at = time.time() + max(0, expires_in - 30)
        return token

    def graphql(self) -> GeneratedClient:
        """Return a generated client instance (sync)."""
        headers = self._get_auth_header()

        # Prefer reusing caller-provided httpx client.
        if self._httpx_client is not None:
            self._httpx_client.headers.update(headers)
            return GeneratedClient(
                url=self._config.endpoint,
                http_client=self._httpx_client,
            )

        http_client = httpx.Client(timeout=self._timeout, headers=headers)
        return GeneratedClient(
            url=self._config.endpoint,
            http_client=http_client,
        )

    def upload_asset(
        self,
        file_path: str | Path,
        *,
        submit_args: Optional[Any] = None,
        name: Optional[str] = None,
    ) -> Any:
        """Upload a file and submit it as an asset.

        Args:
            file_path: Path to the file to upload.
            submit_args: Optional SubmitAssetInput with metadata (name, manufacturer,
                model, version, type, etc.). Import from netrise_turbine_sdk_graphql.input_types.
            name: Optional display name for the asset. Defaults to the filename.
                Ignored if submit_args.name is already set.

        Returns:
            MutationAssetSubmit response containing asset info and upload details.

        Example:
            >>> from netrise_turbine_sdk_graphql.input_types import SubmitAssetInput
            >>> sdk = TurbineClient(TurbineClientConfig.from_env())
            >>> resp = sdk.upload_asset("firmware.bin", name="My Firmware v1.0")
            >>> print(resp.asset.submit.asset.id)
        """
        # Lazy import to avoid import-time coupling with generated code
        from netrise_turbine_sdk_graphql.input_types import SubmitAssetInput

        path = Path(file_path)
        if not path.exists():
            raise FileNotFoundError(f"File not found: {path}")

        file_name = path.name

        # Build submit_args if not provided
        if submit_args is None:
            submit_args = SubmitAssetInput(name=name or file_name)
        elif name and submit_args.name is None:
            # User provided submit_args but no name in it; use the name param
            submit_args = SubmitAssetInput(
                **{**submit_args.model_dump(exclude_unset=True), "name": name}
            )

        with self.graphql() as client:
            # Step 1: Submit asset metadata and get presigned URL
            resp = client.mutation_asset_submit(
                asset_submit_file_name=file_name,
                asset_submit_args=submit_args,
            )

            upload_url = resp.asset.submit.upload_url

            # Step 2: Upload file content to presigned URL
            file_content = path.read_bytes()
            with httpx.Client(timeout=self._timeout) as http:
                put_resp = http.put(upload_url, content=file_content)
                put_resp.raise_for_status()

        return resp

    def upload_assets(
        self,
        directory: str | Path,
        *,
        submit_args_fn: Optional[Any] = None,
    ) -> list[tuple[Path, Any]]:
        """Upload all files in a directory as assets.

        Args:
            directory: Path to directory containing files to upload.
            submit_args_fn: Optional callable that takes a file Path and returns
                a SubmitAssetInput for that file. If not provided, each file is
                uploaded with its filename as the asset name.

        Returns:
            List of (Path, MutationAssetSubmit) tuples for successfully uploaded files.
            Failed uploads are printed to stderr but do not stop the batch.

        Example:
            >>> from netrise_turbine_sdk_graphql.input_types import SubmitAssetInput
            >>> sdk = TurbineClient(TurbineClientConfig.from_env())
            >>>
            >>> # Simple: upload all files with default names
            >>> results = sdk.upload_assets("./firmware_images/")
            >>>
            >>> # Custom: add metadata per file
            >>> def make_args(path):
            ...     return SubmitAssetInput(
            ...         name=f"chainguard-{path.name}",
            ...         product="chainguard",
            ...     )
            >>> results = sdk.upload_assets("./images/", submit_args_fn=make_args)
        """
        import sys

        dir_path = Path(directory)
        if not dir_path.exists():
            raise FileNotFoundError(f"Directory not found: {dir_path}")
        if not dir_path.is_dir():
            raise NotADirectoryError(f"Not a directory: {dir_path}")

        files = [f for f in dir_path.iterdir() if f.is_file()]
        if not files:
            print(f"No files found in {dir_path}", file=sys.stderr)
            return []

        results: list[tuple[Path, Any]] = []

        for file_path in files:
            try:
                submit_args = None
                if submit_args_fn is not None:
                    submit_args = submit_args_fn(file_path)

                resp = self.upload_asset(file_path, submit_args=submit_args)
                results.append((file_path, resp))
                print(f"[OK] Uploaded: {file_path.name}")

            except Exception as e:
                print(f"[FAILED] {file_path.name}: {e}", file=sys.stderr)

        return results


def _strip_or_none(v: Optional[str]) -> Optional[str]:
    if v is None:
        return None
    v = v.strip()
    return v or None


def _fetch_token(
    *,
    domain: Optional[str],
    client_id: Optional[str],
    client_secret: Optional[str],
    audience: Optional[str],
    organization_id: Optional[str],
    timeout: float,
) -> tuple[str, int]:
    if not domain:
        raise ValueError("domain is required when TURBINE_API_TOKEN is not set")
    if not client_id or not client_secret:
        raise ValueError(
            "client_id and client_secret are required when TURBINE_API_TOKEN is not set"
        )
    if not audience:
        raise ValueError("audience is required when TURBINE_API_TOKEN is not set")

    domain = domain.rstrip("/")
    token_url = f"{domain}/oauth/token"

    payload: Dict[str, Any] = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret,
        "audience": audience,
    }

    # Organizations support depends on the client grant settings.
    if organization_id:
        payload["organization"] = organization_id

    with httpx.Client(timeout=timeout) as c:
        r = c.post(token_url, json=payload)
        r.raise_for_status()
        data = r.json()

    token = data.get("access_token")
    expires_in = int(data.get("expires_in", 3600))

    if not token:
        raise RuntimeError(f"Token response missing access_token: {data}")

    return token if token.startswith("Bearer ") else f"Bearer {token}", expires_in
