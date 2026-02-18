<!-- Generated file: do not edit by hand -->

# query_vulnerabilities_overview

Get a summary of vulnerability counts and severity across assets.

## Parameters

| name | type | required |
| --- | --- | --- |
| `vulnerabilities_overview_args` | `VulnerabilityOverviewInput` | `true` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `vulnerabilitiesOverview` | `object` | yes |
| `vulnerabilitiesOverview.edges[]` | `object` | yes |
| `vulnerabilitiesOverview.edges[].cursor` | `string` | yes |
| `vulnerabilitiesOverview.edges[].node` | `object` | yes |
| `vulnerabilitiesOverview.edges[].node.botnetsList[]` | `string` | yes |
| `vulnerabilitiesOverview.edges[].node.cisaDueDate` | `typing.Annotated[datetime.datetime, BeforeValidator(func=<function parse_datetime at 0x1090d31a0>, json_schema_input_type=PydanticUndefined)]` | yes |
| `vulnerabilitiesOverview.edges[].node.component` | `string` | yes |
| `vulnerabilitiesOverview.edges[].node.cve` | `string` | yes |
| `vulnerabilitiesOverview.edges[].node.cvssScore` | `float` | yes |
| `vulnerabilitiesOverview.edges[].node.dateAdded` | `typing.Annotated[datetime.datetime, BeforeValidator(func=<function parse_datetime at 0x1090d31a0>, json_schema_input_type=PydanticUndefined)]` | yes |
| `vulnerabilitiesOverview.edges[].node.epssPercentile` | `float` | yes |
| `vulnerabilitiesOverview.edges[].node.epssScore` | `float` | yes |
| `vulnerabilitiesOverview.edges[].node.exploitFound` | `boolean` | yes |
| `vulnerabilitiesOverview.edges[].node.inAssets` | `integer` | yes |
| `vulnerabilitiesOverview.edges[].node.inBotnets` | `boolean` | yes |
| `vulnerabilitiesOverview.edges[].node.inKnownAttacks` | `boolean` | yes |
| `vulnerabilitiesOverview.edges[].node.inKnownExploitedVulnerabilities` | `boolean` | yes |
| `vulnerabilitiesOverview.edges[].node.inRansomware` | `boolean` | yes |
| `vulnerabilitiesOverview.edges[].node.inTheWild` | `boolean` | yes |
| `vulnerabilitiesOverview.edges[].node.inThreatActors` | `boolean` | yes |
| `vulnerabilitiesOverview.edges[].node.knownAttacksList[]` | `string` | yes |
| `vulnerabilitiesOverview.edges[].node.netrisePriorityRating` | `integer` | yes |
| `vulnerabilitiesOverview.edges[].node.occurrences` | `integer` | yes |
| `vulnerabilitiesOverview.edges[].node.priority` | `string` | yes |
| `vulnerabilitiesOverview.edges[].node.severity` | `Severity` | yes |
| `vulnerabilitiesOverview.edges[].node.threatActorsList[]` | `string` | yes |
| `vulnerabilitiesOverview.pageInfo` | `object` | no |
| `vulnerabilitiesOverview.pageInfo.endCursor` | `string` | yes |
| `vulnerabilitiesOverview.pageInfo.hasNextPage` | `boolean` | no |
| `vulnerabilitiesOverview.pageInfo.hasPreviousPage` | `boolean` | no |
| `vulnerabilitiesOverview.pageInfo.startCursor` | `string` | yes |
| `vulnerabilitiesOverview.pageInfo.totalCount` | `integer` | yes |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    Cursor,
    VulnerabilityOverviewInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_vulnerabilities_overview(vulnerabilities_overview_args=VulnerabilityOverviewInput(cursor=Cursor()))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
