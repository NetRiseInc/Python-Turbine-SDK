<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# query_vulnerabilities

[Back to the index](../README.md)

List CVEs on an asset with scores and fix versions.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |
| `vulnerabilities_args` | `PaginatedVulnerabilitiesInput` | `true` |

## Filter fields

Use `where()` to build `VulnerabilityFilter` — see [Filtering](../guides/filtering.md).

```python
from netrise_turbine_sdk import where
from netrise_turbine_sdk_graphql.input_types import VulnerabilityFilter

flt = where(VulnerabilityFilter, severity="...", name__contains="...")
```

| `where()` kwarg | GraphQL field | exact match uses |
| --- | --- | --- |
| `cve` | `VulnerabilityField.CVE` | `EQUAL` |
| `severity` | `VulnerabilityField.SEVERITY` | `ENUM` |
| `name` | `VulnerabilityField.NAME` | `EQUAL` |
| `version` | `VulnerabilityField.VERSION` | `EQUAL` |
| `vendor` | `VulnerabilityField.VENDOR` | `EQUAL` |
| `maturity` | `VulnerabilityField.MATURITY` | `ENUM` |
| `filepath` | `VulnerabilityField.FILEPATH` | `EQUAL` |
| `attack_vector` | `VulnerabilityField.ATTACKVECTOR` | `ENUM` |
| `attack_complexity` | `VulnerabilityField.ATTACKCOMPLEXITY` | `ENUM` |
| `remediation_status` | `VulnerabilityField.VULNERABILITYREMEDIATIONSTATUS` | `ENUM` |
| `epss_score` | `VulnerabilityField.EPSSSCORE` | `EQUAL` |
| `epss_percentile` | `VulnerabilityField.EPSSPERCENTILE` | `EQUAL` |

Lookups: `field=` (exact), `field__contains=`, `field__in=`, `field__gt=`, `field__gte=`, `field__lt=`, `field__lte=`.

## Response fields

Typed attributes on the response model.

| Field | Type | Nullable |
| --- | --- | --- |
| `vulnerabilities` | `object` | yes |
| `vulnerabilities.edges[]` | `object` | yes |
| `vulnerabilities.edges[].cursor` | `string` | yes |
| `vulnerabilities.edges[].node` | `object` | yes |
| `vulnerabilities.edges[].node.id` | `string` | no |
| `vulnerabilities.edges[].node.attackComplexity` | `string` | yes |
| `vulnerabilities.edges[].node.attackVector` | `string` | yes |
| `vulnerabilities.edges[].node.componentId` | `string` | yes |
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
| `vulnerabilities.edges[].node.currentRemediation.responses[]` | `RemediationResponses` | yes |
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
| `vulnerabilities.edges[].node.jiraTicket` | `object` | yes |
| `vulnerabilities.edges[].node.jiraTicket.issueKey` | `string` | no |
| `vulnerabilities.edges[].node.jiraTicket.issueUrl` | `string` | no |
| `vulnerabilities.edges[].node.maturity` | `string` | yes |
| `vulnerabilities.edges[].node.name` | `string` | yes |
| `vulnerabilities.edges[].node.severity` | `string` | yes |
| `vulnerabilities.edges[].node.ssvc` | `object` | yes |
| `vulnerabilities.edges[].node.ssvc.automatable` | `boolean` | yes |
| `vulnerabilities.edges[].node.ssvc.dateAccessed` | `string` | yes |
| `vulnerabilities.edges[].node.ssvc.exploitation` | `SsvcExploitation` | yes |
| `vulnerabilities.edges[].node.ssvc.source` | `string` | yes |
| `vulnerabilities.edges[].node.ssvc.technicalImpact` | `SsvcTechnicalImpact` | yes |
| `vulnerabilities.edges[].node.vendor` | `string` | yes |
| `vulnerabilities.edges[].node.version` | `string` | yes |
| `vulnerabilities.pageInfo` | `object` | no |
| `vulnerabilities.pageInfo.endCursor` | `string` | yes |
| `vulnerabilities.pageInfo.hasNextPage` | `boolean` | no |
| `vulnerabilities.pageInfo.hasPreviousPage` | `boolean` | no |
| `vulnerabilities.pageInfo.startCursor` | `string` | yes |
| `vulnerabilities.pageInfo.totalCount` | `integer` | yes |

## Example

`sdk.iter_vulnerabilities(...)` paginates for you and accepts filter kwargs.

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig


def main() -> None:
    sdk = TurbineClient(TurbineClientConfig.from_env())

    for item in sdk.iter_vulnerabilities(asset_id="asset_123", page_size=10, max_pages=1):
        print(item)


if __name__ == "__main__":
    main()
```

## Raw client

Same data via `client.query_vulnerabilities` when you need exact GraphQL control.

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
        # Responses are typed Pydantic models: read fields as attributes.
        for edge in resp.vulnerabilities.edges or []:
            node = edge.node
            print(node.id, node.cve, node.name)


if __name__ == "__main__":
    main()
```
