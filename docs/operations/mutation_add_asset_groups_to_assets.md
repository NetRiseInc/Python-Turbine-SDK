<!-- Generated file: do not edit by hand -->

# mutation_add_asset_groups_to_assets

Associate a list of existing asset groups with selected assets.

## Parameters

| name | type | required |
| --- | --- | --- |
| `add_asset_groups_to_assets_args` | `AddAssetGroupsToAssetsInput` | `true` |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    AddAssetGroupsToAssetsInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.mutation_add_asset_groups_to_assets(add_asset_groups_to_assets_args=AddAssetGroupsToAssetsInput(asset_ids=['example']))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
