<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# query_remediated_vulnerabilities_by_asset

[Back to the index](../README.md)

List remediated vulns for one status bucket, by asset.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |
| `remediated_vulnerabilities_by_asset_args` | `RemediatedVulnerabilitiesByAssetInput` | `true` |

## Response fields

Typed attributes on the response model.

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
