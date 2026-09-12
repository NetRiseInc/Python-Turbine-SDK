<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# query_list_asset_correlations

[Back to the index](../README.md)

List cross-asset correlations for shared components or vulns.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |
| `list_asset_correlations_args` | `ListAssetCorrelationsInput` | `true` |

## Response fields

Typed attributes on the response model.

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
        # Responses are typed Pydantic models: read fields as attributes.
        for edge in resp.list_asset_correlations.edges or []:
            node = edge.node
            print(node.artifact, node.asset_id, node.asset_name)


if __name__ == "__main__":
    main()
```
