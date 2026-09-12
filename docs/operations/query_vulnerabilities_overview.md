<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# query_vulnerabilities_overview

[Back to the index](../README.md)

Get vulnerability counts and severity across assets.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |
| `vulnerabilities_overview_args` | `VulnerabilityOverviewInput` | `true` |

## Response fields

Typed attributes on the response model.

| Field | Type | Nullable |
| --- | --- | --- |
| `vulnerabilitiesOverview` | `object` | yes |
| `vulnerabilitiesOverview.edges[]` | `object` | yes |
| `vulnerabilitiesOverview.edges[].cursor` | `string` | yes |
| `vulnerabilitiesOverview.edges[].node` | `object` | yes |
| `vulnerabilitiesOverview.edges[].node.botnetsList[]` | `string` | yes |
| `vulnerabilitiesOverview.edges[].node.cisaDueDate` | `typing.Annotated[datetime.datetime, BeforeValidator(func=<function parse_datetime at 0x1090c2660>, json_schema_input_type=PydanticUndefined)]` | yes |
| `vulnerabilitiesOverview.edges[].node.component` | `string` | yes |
| `vulnerabilitiesOverview.edges[].node.cve` | `string` | yes |
| `vulnerabilitiesOverview.edges[].node.cvssScore` | `float` | yes |
| `vulnerabilitiesOverview.edges[].node.dateAdded` | `typing.Annotated[datetime.datetime, BeforeValidator(func=<function parse_datetime at 0x1090c2660>, json_schema_input_type=PydanticUndefined)]` | yes |
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

`sdk.iter_vulnerabilities_overview(...)` paginates for you and accepts filter kwargs.

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig


def main() -> None:
    sdk = TurbineClient(TurbineClientConfig.from_env())

    for item in sdk.iter_vulnerabilities_overview(asset_id="asset_123", page_size=10, max_pages=1):
        print(item)


if __name__ == "__main__":
    main()
```

## Raw client

Same data via `client.query_vulnerabilities_overview` when you need exact GraphQL control.

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
        # Responses are typed Pydantic models: read fields as attributes.
        for edge in resp.vulnerabilities_overview.edges or []:
            node = edge.node
            print(node.cve, node.severity, node.cisa_due_date)


if __name__ == "__main__":
    main()
```
