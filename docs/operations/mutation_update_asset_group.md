<!-- Generated file: do not edit by hand -->

# mutation_update_asset_group

Rename or update the description of an existing asset group.

## Parameters

| name | type | required |
| --- | --- | --- |
| `update_asset_group_args` | `UpdateAssetGroupInput` | `true` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `updateAssetGroup` | `object` | no |
| `updateAssetGroup.assetGroup` | `object` | yes |
| `updateAssetGroup.assetGroup.id` | `string` | no |
| `updateAssetGroup.assetGroup.description` | `string` | yes |
| `updateAssetGroup.assetGroup.name` | `string` | no |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    UpdateAssetGroupInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.mutation_update_asset_group(update_asset_group_args=UpdateAssetGroupInput(id='id_123', name='my-example'))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
