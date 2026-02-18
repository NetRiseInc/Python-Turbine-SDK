<!-- Generated file: do not edit by hand -->

# query_assets_overview

View high-level risk and threat exposure metrics for multiple assets.

## Parameters

| name | type | required |
| --- | --- | --- |
| `assets_overview_args` | `AssetOverviewInput` | `true` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `assetsOverview` | `object` | yes |
| `assetsOverview.edges[]` | `object` | yes |
| `assetsOverview.edges[].cursor` | `string` | yes |
| `assetsOverview.edges[].node` | `object` | yes |
| `assetsOverview.edges[].node.associatedCves[]` | `string` | yes |
| `assetsOverview.edges[].node.botnets[]` | `string` | yes |
| `assetsOverview.edges[].node.composedAssetId` | `string` | no |
| `assetsOverview.edges[].node.exploitFound` | `boolean` | yes |
| `assetsOverview.edges[].node.inBotnets` | `boolean` | yes |
| `assetsOverview.edges[].node.inKnownAttacks` | `boolean` | yes |
| `assetsOverview.edges[].node.inKnownExploitedVulnerabilities` | `boolean` | yes |
| `assetsOverview.edges[].node.inRansomware` | `boolean` | yes |
| `assetsOverview.edges[].node.inTheWild` | `boolean` | yes |
| `assetsOverview.edges[].node.inThreatActors` | `boolean` | yes |
| `assetsOverview.edges[].node.knownAttacks[]` | `string` | yes |
| `assetsOverview.edges[].node.name` | `string` | yes |
| `assetsOverview.edges[].node.operatingSystem` | `string` | yes |
| `assetsOverview.edges[].node.operatingSystemKernelVersion` | `string` | yes |
| `assetsOverview.edges[].node.product` | `string` | yes |
| `assetsOverview.edges[].node.risk` | `object` | yes |
| `assetsOverview.edges[].node.risk.category` | `RiskCategory` | yes |
| `assetsOverview.edges[].node.risk.rawScore` | `float` | yes |
| `assetsOverview.edges[].node.risk.score` | `float` | yes |
| `assetsOverview.edges[].node.submitDatetime` | `typing.Annotated[datetime.datetime, BeforeValidator(func=<function parse_datetime at 0x1090d31a0>, json_schema_input_type=PydanticUndefined)]` | yes |
| `assetsOverview.edges[].node.threatActors[]` | `string` | yes |
| `assetsOverview.edges[].node.type` | `AssetType` | yes |
| `assetsOverview.edges[].node.vendor` | `string` | yes |
| `assetsOverview.edges[].node.version` | `string` | yes |
| `assetsOverview.pageInfo` | `object` | no |
| `assetsOverview.pageInfo.endCursor` | `string` | yes |
| `assetsOverview.pageInfo.hasNextPage` | `boolean` | no |
| `assetsOverview.pageInfo.hasPreviousPage` | `boolean` | no |
| `assetsOverview.pageInfo.startCursor` | `string` | yes |
| `assetsOverview.pageInfo.totalCount` | `integer` | yes |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    AssetOverviewInput,
    Cursor,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_assets_overview(assets_overview_args=AssetOverviewInput(cursor=Cursor()))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
