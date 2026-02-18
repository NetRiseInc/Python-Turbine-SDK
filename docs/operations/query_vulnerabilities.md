<!-- Generated file: do not edit by hand -->

# query_vulnerabilities

List CVEs and associated risks for components in an asset.

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
| `vulnerabilities.edges[].node.attackComplexity` | `string` | yes |
| `vulnerabilities.edges[].node.attackVector` | `string` | yes |
| `vulnerabilities.edges[].node.correlations[]` | `object` | yes |
| `vulnerabilities.edges[].node.correlations[].artifact` | `string` | yes |
| `vulnerabilities.edges[].node.correlations[].assetId` | `string` | yes |
| `vulnerabilities.edges[].node.correlations[].assetName` | `string` | yes |
| `vulnerabilities.edges[].node.correlations[].location` | `string` | yes |
| `vulnerabilities.edges[].node.correlations[].risk` | `object` | yes |
| `vulnerabilities.edges[].node.correlations[].risk.category` | `RiskCategory` | yes |
| `vulnerabilities.edges[].node.correlations[].risk.rawScore` | `float` | yes |
| `vulnerabilities.edges[].node.correlations[].risk.score` | `float` | yes |
| `vulnerabilities.edges[].node.correlations[].updatedAt` | `string` | yes |
| `vulnerabilities.edges[].node.correlationsCount` | `integer` | yes |
| `vulnerabilities.edges[].node.currentRemediation` | `object` | yes |
| `vulnerabilities.edges[].node.currentRemediation.assetId` | `string` | yes |
| `vulnerabilities.edges[].node.currentRemediation.author` | `string` | no |
| `vulnerabilities.edges[].node.currentRemediation.createdAt` | `string` | no |
| `vulnerabilities.edges[].node.currentRemediation.description` | `string` | yes |
| `vulnerabilities.edges[].node.currentRemediation.identificationIds[]` | `string` | yes |
| `vulnerabilities.edges[].node.currentRemediation.justification` | `VexJustification` | yes |
| `vulnerabilities.edges[].node.currentRemediation.response` | `RemediationResponses` | yes |
| `vulnerabilities.edges[].node.currentRemediation.status` | `VexStatus` | no |
| `vulnerabilities.edges[].node.currentRemediation.vulnerabilityId` | `string` | no |
| `vulnerabilities.edges[].node.cve` | `string` | yes |
| `vulnerabilities.edges[].node.cvssScore` | `float` | yes |
| `vulnerabilities.edges[].node.epssPercentile` | `float` | yes |
| `vulnerabilities.edges[].node.epssScore` | `float` | yes |
| `vulnerabilities.edges[].node.filePath` | `string` | yes |
| `vulnerabilities.edges[].node.fixVersions[]` | `string` | yes |
| `vulnerabilities.edges[].node.identificationIds[]` | `string` | yes |
| `vulnerabilities.edges[].node.inKnownExploitedVulnerabilities` | `boolean` | yes |
| `vulnerabilities.edges[].node.isReachable` | `boolean` | yes |
| `vulnerabilities.edges[].node.maturity` | `string` | yes |
| `vulnerabilities.edges[].node.name` | `string` | yes |
| `vulnerabilities.edges[].node.severity` | `string` | yes |
| `vulnerabilities.edges[].node.vendor` | `string` | yes |
| `vulnerabilities.edges[].node.version` | `string` | yes |
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
        resp = client.query_vulnerabilities(vulnerabilities_args=PaginatedVulnerabilitiesInput(asset_id='asset_123'))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
