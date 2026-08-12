<!-- Generated file: do not edit by hand -->

# query_remediated_vulnerabilities_by_asset

List remediated vulnerabilities grouped by asset for a single remediation-status bucket, with pagination, filtering, and sorting.

## Parameters

| name | type | required |
| --- | --- | --- |
| `remediated_vulnerabilities_by_asset_args` | `RemediatedVulnerabilitiesByAssetInput` | `true` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `remediatedVulnerabilitiesByAsset` | `object` | yes |
| `remediatedVulnerabilitiesByAsset.edges[]` | `object` | yes |
| `remediatedVulnerabilitiesByAsset.edges[].cursor` | `string` | yes |
| `remediatedVulnerabilitiesByAsset.edges[].node` | `object` | yes |
| `remediatedVulnerabilitiesByAsset.edges[].node.assetId` | `string` | yes |
| `remediatedVulnerabilitiesByAsset.edges[].node.assetName` | `string` | yes |
| `remediatedVulnerabilitiesByAsset.edges[].node.assetStatus` | `AssetOverviewRiskCategory` | yes |
| `remediatedVulnerabilitiesByAsset.edges[].node.assetVendor` | `string` | yes |
| `remediatedVulnerabilitiesByAsset.edges[].node.remediationCount` | `integer` | no |
| `remediatedVulnerabilitiesByAsset.edges[].node.remediationStatus` | `VulnerabilityRemediationStatus` | yes |
| `remediatedVulnerabilitiesByAsset.pageInfo` | `object` | no |
| `remediatedVulnerabilitiesByAsset.pageInfo.endCursor` | `string` | yes |
| `remediatedVulnerabilitiesByAsset.pageInfo.hasNextPage` | `boolean` | no |
| `remediatedVulnerabilitiesByAsset.pageInfo.hasPreviousPage` | `boolean` | no |
| `remediatedVulnerabilitiesByAsset.pageInfo.startCursor` | `string` | yes |
| `remediatedVulnerabilitiesByAsset.pageInfo.totalCount` | `integer` | yes |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    Cursor,
    RemediatedVulnerabilitiesByAssetInput,
)
from netrise_turbine_sdk_graphql.enums import (
    VulnerabilityRemediationStatus,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_remediated_vulnerabilities_by_asset(remediated_vulnerabilities_by_asset_args=RemediatedVulnerabilitiesByAssetInput(cursor=Cursor(), status=VulnerabilityRemediationStatus.UNSPECIFIED))
        # Responses are typed Pydantic models: read fields as attributes.
        for edge in resp.remediated_vulnerabilities_by_asset.edges or []:
            node = edge.node
            print(node.asset_id, node.asset_name, node.asset_status)


if __name__ == "__main__":
    main()
```
