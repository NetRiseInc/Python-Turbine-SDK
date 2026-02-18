<!-- Generated file: do not edit by hand -->

# query_analytics

Access high-level risk data and charts for organization dashboards.

## Parameters

| name | type | required |
| --- | --- | --- |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `analytics` | `object` | yes |
| `analytics.assetsByRiskCategory` | `object` | yes |
| `analytics.assetsByRiskCategory.fields[]` | `object` | yes |
| `analytics.assetsByRiskCategory.fields[].name` | `AssetOverviewRiskCategory` | yes |
| `analytics.assetsByRiskCategory.fields[].value` | `integer` | yes |
| `analytics.highProfileVulnerabilities` | `object` | no |
| `analytics.highProfileVulnerabilities.affectedAssets` | `integer` | yes |
| `analytics.highProfileVulnerabilities.associatedCves` | `integer` | yes |
| `analytics.highProfileVulnerabilities.uniqueExploits` | `integer` | yes |
| `analytics.knownExploitedVulnerabilities` | `object` | no |
| `analytics.knownExploitedVulnerabilities.affectedAssets` | `integer` | yes |
| `analytics.knownExploitedVulnerabilities.pastDue` | `integer` | yes |
| `analytics.knownExploitedVulnerabilities.uniqueKevs` | `integer` | yes |
| `analytics.vulnerabilitiesByAge[]` | `object` | no |
| `analytics.vulnerabilitiesByAge[].age` | `string` | yes |
| `analytics.vulnerabilitiesByAge[].ageGroupId` | `integer` | no |
| `analytics.vulnerabilitiesByAge[].count` | `integer` | yes |
| `analytics.vulnerabilitiesByAge[].from` | `string` | yes |
| `analytics.vulnerabilitiesByAge[].severity` | `string` | yes |
| `analytics.vulnerabilitiesByAge[].to` | `string` | yes |
| `analytics.vulnerabilitiesByAge[].uniqueCount` | `integer` | yes |
| `analytics.vulnerabilitiesByPriorityScore[]` | `object` | no |
| `analytics.vulnerabilitiesByPriorityScore[].occurrences` | `integer` | no |
| `analytics.vulnerabilitiesByPriorityScore[].priorityScore` | `PriorityScore` | no |
| `analytics.vulnerabilitiesByPriorityScore[].priorityScoreFilter` | `string` | no |
| `analytics.vulnerabilitiesByPriorityScore[].uniques` | `integer` | no |
| `analytics.vulnerabilitiesFunnelChart[]` | `object` | yes |
| `analytics.vulnerabilitiesFunnelChart[].category` | `FunnelChartCategory` | yes |
| `analytics.vulnerabilitiesFunnelChart[].critical` | `integer` | yes |
| `analytics.vulnerabilitiesFunnelChart[].high` | `integer` | yes |
| `analytics.vulnerabilitiesFunnelChart[].low` | `integer` | yes |
| `analytics.vulnerabilitiesFunnelChart[].medium` | `integer` | yes |
| `analytics.vulnerabilitiesFunnelChart[].total` | `integer` | yes |
| `analytics.vulnerabilitiesOfInterest[]` | `object` | no |
| `analytics.vulnerabilitiesOfInterest[].name` | `CategoryOfInterestName` | no |
| `analytics.vulnerabilitiesOfInterest[].occurrences` | `integer` | no |
| `analytics.vulnerabilitiesOfInterest[].uniques` | `integer` | no |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_analytics()
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
