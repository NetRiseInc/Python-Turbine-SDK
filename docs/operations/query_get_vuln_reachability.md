<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# query_get_vuln_reachability

[Back to the index](../README.md)

Check whether a vulnerability is reachable via system paths.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |
| `get_vuln_reachability_args` | `GetVulnReachabilityInput` | `true` |

## Response fields

Typed attributes on the response model.

| Field | Type | Nullable |
| --- | --- | --- |
| `getVulnReachability[]` | `object` | yes |
| `getVulnReachability[].cveId` | `string` | yes |
| `getVulnReachability[].entryPoint` | `string` | yes |
| `getVulnReachability[].entryType` | `EvidenceEntryType` | yes |
| `getVulnReachability[].scripts[]` | `object` | yes |
| `getVulnReachability[].scripts[].detail` | `string` | yes |
| `getVulnReachability[].scripts[].edgeType` | `EvidenceEdgeType` | yes |
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
        # Responses are typed Pydantic models: read fields as attributes.
        for item in resp.get_vuln_reachability or []:
            print(item.cve_id, item.entry_point, item.entry_type)


if __name__ == "__main__":
    main()
```
