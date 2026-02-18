<!-- Generated file: do not edit by hand -->

# mutation_create_asset_group

Create a new named group to organize and track assets.

## Parameters

| name | type | required |
| --- | --- | --- |
| `create_asset_group_args` | `CreateAssetGroupInput` | `true` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `createAssetGroup` | `object` | no |
| `createAssetGroup.assetGroup` | `object` | yes |
| `createAssetGroup.assetGroup.id` | `string` | no |
| `createAssetGroup.assetGroup.description` | `string` | yes |
| `createAssetGroup.assetGroup.name` | `string` | no |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    CreateAssetGroupInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.mutation_create_asset_group(create_asset_group_args=CreateAssetGroupInput(name='my-example'))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
