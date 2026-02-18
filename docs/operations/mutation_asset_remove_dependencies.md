<!-- Generated file: do not edit by hand -->

# mutation_asset_remove_dependencies

Remove specific dependencies from the component list of an asset.

## Parameters

| name | type | required |
| --- | --- | --- |
| `asset_remove_dependencies_args` | `IdentificationInput` | `true` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `asset` | `object` | yes |
| `asset.removeDependencies` | `object` | yes |
| `asset.removeDependencies.err` | `string` | yes |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    IdentificationInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.mutation_asset_remove_dependencies(asset_remove_dependencies_args=IdentificationInput(composed_asset_id='composed_asset_123', identification_ids=['value']))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
