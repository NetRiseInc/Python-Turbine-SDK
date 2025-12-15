<!-- Generated file: do not edit by hand -->

# mutation_create_asset_group

## Parameters

| name | type | required |
| --- | --- | --- |
| `create_asset_group_args` | `CreateAssetGroupInput` | `true` |

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
        resp = client.mutation_create_asset_group(create_asset_group_args=CreateAssetGroupInput(name='example'))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
