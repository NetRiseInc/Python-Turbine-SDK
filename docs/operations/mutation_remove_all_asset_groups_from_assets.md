<!-- Generated file: do not edit by hand -->

# mutation_remove_all_asset_groups_from_assets

Disassociate all asset groups from a specified list of assets.

## Parameters

| name | type | required |
| --- | --- | --- |
| `remove_all_asset_groups_from_assets_args` | `RemoveAllAssetGroupsFromAssetsInput` | `true` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `removeAllAssetGroupsFromAssets` | `boolean` | no |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    RemoveAllAssetGroupsFromAssetsInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.mutation_remove_all_asset_groups_from_assets(remove_all_asset_groups_from_assets_args=RemoveAllAssetGroupsFromAssetsInput(asset_ids=['value']))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
