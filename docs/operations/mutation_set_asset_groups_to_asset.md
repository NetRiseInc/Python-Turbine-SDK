<!-- Generated file: do not edit by hand -->

# mutation_set_asset_groups_to_asset

## Parameters

| name | type | required |
| --- | --- | --- |
| `set_asset_groups_to_asset_args` | `SetAssetGroupsToAssetInput` | `true` |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    SetAssetGroupsToAssetInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.mutation_set_asset_groups_to_asset(set_asset_groups_to_asset_args=SetAssetGroupsToAssetInput(asset_id='asset_123'))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
