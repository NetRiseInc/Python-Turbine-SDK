<!-- Generated file: do not edit by hand -->

# query_grouped_dependencies

View dependencies aggregated by vendor, license, or specific component type.

## Parameters

| name | type | required |
| --- | --- | --- |
| `grouped_dependencies_args` | `GroupedDependenciesInput` | `true` |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    GroupedDependenciesInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_grouped_dependencies(grouped_dependencies_args=GroupedDependenciesInput(composed_asset_id='asset_123'))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
