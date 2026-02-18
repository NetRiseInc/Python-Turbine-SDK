<!-- Generated file: do not edit by hand -->

# mutation_asset_modify_dependency

Update metadata or details for a manually added asset dependency.

## Parameters

| name | type | required |
| --- | --- | --- |
| `asset_modify_dependency_args` | `ModifyDependencyInput` | `true` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `asset` | `object` | yes |
| `asset.modifyDependency` | `object` | yes |
| `asset.modifyDependency.err` | `string` | yes |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    DependencyDetailsInput,
    IdentificationInput,
    ModifyDependencyInput,
)
from netrise_turbine_sdk_graphql.enums import (
    ComponentType,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.mutation_asset_modify_dependency(asset_modify_dependency_args=ModifyDependencyInput(identification=IdentificationInput(composed_asset_id='composed_asset_123', identification_ids=[None  # TODO: fill]), dependency_fields=DependencyDetailsInput(name='my-example', type=ComponentType.UNSPECIFIED)))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
