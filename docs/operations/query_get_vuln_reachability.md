<!-- Generated file: do not edit by hand -->

# query_get_vuln_reachability

Determine if a vulnerability can be executed via system paths.

## Parameters

| name | type | required |
| --- | --- | --- |
| `get_vuln_reachability_args` | `GetVulnReachabilityInput` | `true` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `getVulnReachability[]` | `object` | yes |
| `getVulnReachability[].cveId` | `string` | yes |
| `getVulnReachability[].entryPoint` | `string` | yes |
| `getVulnReachability[].entryType` | `EvidenceEntryType` | yes |
| `getVulnReachability[].scripts[]` | `object` | yes |
| `getVulnReachability[].scripts[].invocation` | `string` | yes |
| `getVulnReachability[].scripts[].path` | `string` | yes |
| `getVulnReachability[].user` | `string` | yes |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    GetVulnReachabilityInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_get_vuln_reachability(get_vuln_reachability_args=GetVulnReachabilityInput(asset_id='asset_123', advisory_id='CVE-2024-1234', identification_ids=['value']))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
