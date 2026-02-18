<!-- Generated file: do not edit by hand -->

# mutation_asset_add_dependency

Manually inject a missing dependency component into an asset's inventory.

## Parameters

| name | type | required |
| --- | --- | --- |
| `asset_add_dependency_args` | `AddDependencyInput` | `true` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `asset` | `object` | yes |
| `asset.addDependency` | `object` | yes |
| `asset.addDependency.err` | `string` | yes |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    AddDependencyInput,
    DependencyDetailsInput,
)
from netrise_turbine_sdk_graphql.enums import (
    ComponentType,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.mutation_asset_add_dependency(asset_add_dependency_args=AddDependencyInput(composed_asset_id='composed_asset_123', dependency_fields=DependencyDetailsInput(name='my-example', type=ComponentType.UNSPECIFIED)))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
