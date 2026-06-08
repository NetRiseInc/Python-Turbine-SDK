<!-- Generated file: do not edit by hand -->

# query_get_dependency_reachability

Determine whether a dependency is reachable via executable scripts or system paths.

## Parameters

| name | type | required |
| --- | --- | --- |
| `get_dependency_reachability_args` | `GetDependencyReachabilityInput` | `true` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `getDependencyReachability[]` | `object` | yes |
| `getDependencyReachability[].cveId` | `string` | yes |
| `getDependencyReachability[].entryPoint` | `string` | yes |
| `getDependencyReachability[].entryType` | `EvidenceEntryType` | yes |
| `getDependencyReachability[].scripts[]` | `object` | yes |
| `getDependencyReachability[].scripts[].detail` | `string` | yes |
| `getDependencyReachability[].scripts[].edgeType` | `EvidenceEdgeType` | yes |
| `getDependencyReachability[].scripts[].invocation` | `string` | yes |
| `getDependencyReachability[].scripts[].path` | `string` | yes |
| `getDependencyReachability[].user` | `string` | yes |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    GetDependencyReachabilityInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_get_dependency_reachability(get_dependency_reachability_args=GetDependencyReachabilityInput(composed_asset_id='composed_asset_123', component_id='id_123'))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
