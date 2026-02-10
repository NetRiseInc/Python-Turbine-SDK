<!-- Generated file: do not edit by hand -->

# query_list_asset_crypto_libraries

List cryptographic libraries and algorithms detected within an asset.

## Parameters

| name | type | required |
| --- | --- | --- |
| `list_asset_crypto_libraries_args` | `ListAssetCryptoLibrariesInput` | `true` |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    Cursor,
    ListAssetCryptoLibrariesInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_list_asset_crypto_libraries(list_asset_crypto_libraries_args=ListAssetCryptoLibrariesInput(asset_id='asset_123', cursor=Cursor()))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
