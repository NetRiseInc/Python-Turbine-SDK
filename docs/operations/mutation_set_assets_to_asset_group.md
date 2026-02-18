<!-- Generated file: do not edit by hand -->

# mutation_set_assets_to_asset_group

Overwrite the member list of an asset group with new assets.

## Parameters

| name | type | required |
| --- | --- | --- |
| `set_assets_to_asset_group_args` | `SetAssetsToAssetGroupInput` | `true` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `setAssetsToAssetGroup` | `boolean` | no |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    SetAssetsToAssetGroupInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.mutation_set_assets_to_asset_group(set_assets_to_asset_group_args=SetAssetsToAssetGroupInput(group_id='group_123'))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
