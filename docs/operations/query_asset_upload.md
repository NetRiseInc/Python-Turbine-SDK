<!-- Generated file: do not edit by hand -->

# query_asset_upload

Obtain a secure pre-signed URL to upload files for analysis.

## Parameters

| name | type | required |
| --- | --- | --- |
| `asset_upload_args` | `Union[AssetUploadInput, None, UnsetType]` | `false` |

## Response Schema

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
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
