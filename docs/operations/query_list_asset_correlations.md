<!-- Generated file: do not edit by hand -->

# query_list_asset_correlations

Retrieve cross-asset correlation data linking shared components and vulnerabilities.

## Parameters

| name | type | required |
| --- | --- | --- |
| `list_asset_correlations_args` | `ListAssetCorrelationsInput` | `true` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `listAssetCorrelations` | `object` | no |
| `listAssetCorrelations.edges[]` | `object` | yes |
| `listAssetCorrelations.edges[].cursor` | `string` | yes |
| `listAssetCorrelations.edges[].node` | `object` | no |
| `listAssetCorrelations.edges[].node.artifact` | `string` | yes |
| `listAssetCorrelations.edges[].node.assetId` | `string` | yes |
| `listAssetCorrelations.edges[].node.assetName` | `string` | yes |
| `listAssetCorrelations.edges[].node.location` | `string` | yes |
| `listAssetCorrelations.edges[].node.risk` | `object` | yes |
| `listAssetCorrelations.edges[].node.risk.category` | `RiskCategory` | yes |
| `listAssetCorrelations.edges[].node.risk.rawScore` | `float` | yes |
| `listAssetCorrelations.edges[].node.risk.score` | `float` | yes |
| `listAssetCorrelations.edges[].node.updatedAt` | `string` | yes |
| `listAssetCorrelations.pageInfo` | `object` | no |
| `listAssetCorrelations.pageInfo.endCursor` | `string` | yes |
| `listAssetCorrelations.pageInfo.hasNextPage` | `boolean` | no |
| `listAssetCorrelations.pageInfo.hasPreviousPage` | `boolean` | no |
| `listAssetCorrelations.pageInfo.startCursor` | `string` | yes |
| `listAssetCorrelations.pageInfo.totalCount` | `integer` | yes |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    ListAssetCorrelationsInput,
)
from netrise_turbine_sdk_graphql.enums import (
    AssetCorrelationType,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_list_asset_correlations(list_asset_correlations_args=ListAssetCorrelationsInput(identifier='cpe:2.3:a:vendor:product:1.0', correlation_type=AssetCorrelationType.UNSPECIFIED))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
