<!-- Generated file: do not edit by hand -->

# query_package_dependencies_by_id

## Parameters

| name | type | required |
| --- | --- | --- |
| `package_dependencies_by_id_args` | `packageDependenciesByIdInput` | `true` |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    packageDependenciesByIdInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_package_dependencies_by_id(package_dependencies_by_id_args=packageDependenciesByIdInput(composed_asset_id='asset_123'))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
