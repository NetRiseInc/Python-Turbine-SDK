<!-- Generated file: do not edit by hand -->

# query_asset_upload

## Parameters

| name | type | required |
| --- | --- | --- |
| `asset_upload_args` | `Union[AssetUploadInput, None, UnsetType]` | `false` |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_asset_upload()
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
