<!-- Generated file: do not edit by hand -->

# mutation_add_assets_to_asset_group

Add specified assets to an existing asset group for organization.

## Parameters

| name | type | required |
| --- | --- | --- |
| `add_assets_to_asset_group_args` | `AddAssetsToAssetGroupInput` | `true` |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    AddAssetsToAssetGroupInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.mutation_add_assets_to_asset_group(add_assets_to_asset_group_args=AddAssetsToAssetGroupInput(id='id_123', asset_ids=['example']))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
