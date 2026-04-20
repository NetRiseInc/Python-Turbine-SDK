<!-- Generated file: do not edit by hand -->

# query_detailed_vulnerabilities_lite

Retrieve vulnerability descriptions with preferred CVSS v3.1 scores only — drops full v2/v4 impact blocks, exploit timelines, references, and problem type details.

## Parameters

| name | type | required |
| --- | --- | --- |
| `detailed_vulnerabilities_args` | `PaginatedDetailedVulnerabilitiesInput` | `true` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `detailedVulnerabilities` | `object` | yes |
| `detailedVulnerabilities.edges[]` | `object` | yes |
| `detailedVulnerabilities.edges[].cursor` | `string` | yes |
| `detailedVulnerabilities.edges[].node` | `object` | yes |
| `detailedVulnerabilities.edges[].node.id` | `string` | yes |
| `detailedVulnerabilities.edges[].node.severity` | `string` | yes |
| `detailedVulnerabilities.edges[].node.createdDatetime` | `string` | yes |
| `detailedVulnerabilities.edges[].node.updatedDatetime` | `string` | yes |
| `detailedVulnerabilities.edges[].node.processedDatetime` | `string` | yes |
| `detailedVulnerabilities.edges[].node.description` | `string` | yes |
| `detailedVulnerabilities.edges[].node.impactV31` | `object` | yes |
| `detailedVulnerabilities.edges[].node.impactV31.metric` | `object` | yes |
| `detailedVulnerabilities.edges[].node.impactV31.metric.cvssData` | `object` | yes |
| `detailedVulnerabilities.pageInfo` | `object` | no |
| `detailedVulnerabilities.pageInfo.endCursor` | `string` | yes |
| `detailedVulnerabilities.pageInfo.hasNextPage` | `boolean` | no |
| `detailedVulnerabilities.pageInfo.hasPreviousPage` | `boolean` | no |
| `detailedVulnerabilities.pageInfo.startCursor` | `string` | yes |
| `detailedVulnerabilities.pageInfo.totalCount` | `integer` | yes |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    PaginatedDetailedVulnerabilitiesInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_detailed_vulnerabilities_lite(detailed_vulnerabilities_args=PaginatedDetailedVulnerabilitiesInput(asset_id='asset_123'))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
