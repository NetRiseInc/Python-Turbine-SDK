<!-- Generated file: do not edit by hand -->

# mutation_update_asset_group

## Parameters

| name | type | required |
| --- | --- | --- |
| `update_asset_group_args` | `UpdateAssetGroupInput` | `true` |

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
        resp = client.mutation_update_asset_group(update_asset_group_args=UpdateAssetGroupInput(id='id_123', name='example'))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
