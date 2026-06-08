<!-- Generated file: do not edit by hand -->

# query_get_secret_reachability

Determine whether discovered secrets are reachable via executable scripts or system paths.

## Parameters

| name | type | required |
| --- | --- | --- |
| `get_secret_reachability_args` | `GetSecretReachabilityInput` | `true` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `getSecretReachability[]` | `object` | yes |
| `getSecretReachability[].cveId` | `string` | yes |
| `getSecretReachability[].entryPoint` | `string` | yes |
| `getSecretReachability[].entryType` | `EvidenceEntryType` | yes |
| `getSecretReachability[].scripts[]` | `object` | yes |
| `getSecretReachability[].scripts[].detail` | `string` | yes |
| `getSecretReachability[].scripts[].edgeType` | `EvidenceEdgeType` | yes |
| `getSecretReachability[].scripts[].invocation` | `string` | yes |
| `getSecretReachability[].scripts[].path` | `string` | yes |
| `getSecretReachability[].user` | `string` | yes |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    GetSecretReachabilityInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_get_secret_reachability(get_secret_reachability_args=GetSecretReachabilityInput(composed_asset_id='composed_asset_123', secret_id='id_123'))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
