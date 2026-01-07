<!-- Generated file: do not edit by hand -->

# mutation_remove_assets_from_asset_group

Remove selected assets from a specific asset group container configuration.

## Parameters

| name | type | required |
| --- | --- | --- |
| `remove_assets_from_asset_group_args` | `RemoveAssetsFromAssetGroupInput` | `true` |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    RemoveAssetsFromAssetGroupInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.mutation_remove_assets_from_asset_group(remove_assets_from_asset_group_args=RemoveAssetsFromAssetGroupInput(id='id_123', asset_ids=['example']))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
