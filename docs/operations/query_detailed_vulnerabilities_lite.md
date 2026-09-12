<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# query_detailed_vulnerabilities_lite

[Back to the index](../README.md)

List vulns with description and preferred CVSS v3.1 only.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |
| `detailed_vulnerabilities_args` | `PaginatedDetailedVulnerabilitiesInput` | `true` |

## Response fields

Typed attributes on the response model.

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

`sdk.iter_detailed_vulnerabilities_lite(...)` paginates for you and accepts filter kwargs.

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig


def main() -> None:
    sdk = TurbineClient(TurbineClientConfig.from_env())

    for item in sdk.iter_detailed_vulnerabilities_lite(asset_id="asset_123", page_size=10, max_pages=1):
        print(item)


if __name__ == "__main__":
    main()
```

## Raw client

Same data via `client.query_detailed_vulnerabilities_lite` when you need exact GraphQL control.

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
        # Responses are typed Pydantic models: read fields as attributes.
        for edge in resp.detailed_vulnerabilities.edges or []:
            node = edge.node
            print(node.id, node.severity, node.created_datetime)


if __name__ == "__main__":
    main()
```
