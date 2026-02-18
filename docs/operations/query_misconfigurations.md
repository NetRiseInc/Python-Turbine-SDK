<!-- Generated file: do not edit by hand -->

# query_misconfigurations

List failed security checks and configuration risks found in assets.

## Parameters

| name | type | required |
| --- | --- | --- |
| `misconfigurations_args` | `MisconfigurationsInput` | `true` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `misconfigurations` | `object` | yes |
| `misconfigurations.edges[]` | `object` | yes |
| `misconfigurations.edges[].cursor` | `string` | no |
| `misconfigurations.edges[].node` | `object` | yes |
| `misconfigurations.edges[].node.category` | `MisconfigurationCategoryType` | yes |
| `misconfigurations.edges[].node.checkDescription` | `string` | yes |
| `misconfigurations.edges[].node.checkId` | `string` | yes |
| `misconfigurations.edges[].node.checkRecommendation` | `string` | yes |
| `misconfigurations.edges[].node.context` | `Any` | yes |
| `misconfigurations.edges[].node.correlations[]` | `object` | yes |
| `misconfigurations.edges[].node.correlations[].artifact` | `string` | yes |
| `misconfigurations.edges[].node.correlations[].assetId` | `string` | yes |
| `misconfigurations.edges[].node.correlations[].assetName` | `string` | yes |
| `misconfigurations.edges[].node.correlations[].location` | `string` | yes |
| `misconfigurations.edges[].node.correlations[].risk` | `object` | yes |
| `misconfigurations.edges[].node.correlations[].risk.category` | `RiskCategory` | yes |
| `misconfigurations.edges[].node.correlations[].risk.rawScore` | `float` | yes |
| `misconfigurations.edges[].node.correlations[].risk.score` | `float` | yes |
| `misconfigurations.edges[].node.correlations[].updatedAt` | `string` | yes |
| `misconfigurations.edges[].node.correlationsCount` | `integer` | yes |
| `misconfigurations.edges[].node.displayName` | `string` | yes |
| `misconfigurations.edges[].node.result` | `MisconfigurationStatusType` | yes |
| `misconfigurations.edges[].node.severity` | `MisconfigurationSeverityType` | yes |
| `misconfigurations.pageInfo` | `object` | yes |
| `misconfigurations.pageInfo.endCursor` | `string` | yes |
| `misconfigurations.pageInfo.hasNextPage` | `boolean` | no |
| `misconfigurations.pageInfo.hasPreviousPage` | `boolean` | no |
| `misconfigurations.pageInfo.startCursor` | `string` | yes |
| `misconfigurations.pageInfo.totalCount` | `integer` | yes |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    Cursor,
    MisconfigurationsInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_misconfigurations(misconfigurations_args=MisconfigurationsInput(asset_id='asset_123', cursor=Cursor()))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
