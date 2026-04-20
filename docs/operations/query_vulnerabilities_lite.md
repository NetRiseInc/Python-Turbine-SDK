<!-- Generated file: do not edit by hand -->

# query_vulnerabilities_lite

List vulnerabilities with trimmed fields — keeps CVE, severity, CVSS/EPSS scores, fix versions, and correlation count; drops nested correlations and remediation details.

## Parameters

| name | type | required |
| --- | --- | --- |
| `vulnerabilities_args` | `PaginatedVulnerabilitiesInput` | `true` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `vulnerabilities` | `object` | yes |
| `vulnerabilities.edges[]` | `object` | yes |
| `vulnerabilities.edges[].cursor` | `string` | yes |
| `vulnerabilities.edges[].node` | `object` | yes |
| `vulnerabilities.edges[].node.id` | `string` | no |
| `vulnerabilities.edges[].node.cve` | `string` | yes |
| `vulnerabilities.edges[].node.name` | `string` | yes |
| `vulnerabilities.edges[].node.severity` | `string` | yes |
| `vulnerabilities.edges[].node.cvssScore` | `float` | yes |
| `vulnerabilities.edges[].node.epssScore` | `float` | yes |
| `vulnerabilities.edges[].node.epssPercentile` | `float` | yes |
| `vulnerabilities.edges[].node.fixVersions[]` | `string` | yes |
| `vulnerabilities.edges[].node.identificationIds[]` | `string` | yes |
| `vulnerabilities.edges[].node.inKnownExploitedVulnerabilities` | `boolean` | yes |
| `vulnerabilities.edges[].node.isReachable` | `boolean` | yes |
| `vulnerabilities.edges[].node.correlationsCount` | `integer` | yes |
| `vulnerabilities.pageInfo` | `object` | no |
| `vulnerabilities.pageInfo.endCursor` | `string` | yes |
| `vulnerabilities.pageInfo.hasNextPage` | `boolean` | no |
| `vulnerabilities.pageInfo.hasPreviousPage` | `boolean` | no |
| `vulnerabilities.pageInfo.startCursor` | `string` | yes |
| `vulnerabilities.pageInfo.totalCount` | `integer` | yes |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    PaginatedVulnerabilitiesInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_vulnerabilities_lite(vulnerabilities_args=PaginatedVulnerabilitiesInput(asset_id='asset_123'))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
