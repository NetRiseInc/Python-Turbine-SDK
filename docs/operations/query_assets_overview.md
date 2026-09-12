<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# query_assets_overview

[Back to the index](../README.md)

Get risk and threat rollups across assets.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |
| `assets_overview_args` | `AssetOverviewInput` | `true` |

## Response fields

Typed attributes on the response model.

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
| `assetsOverview.edges[].node.submitDatetime` | `typing.Annotated[datetime.datetime, BeforeValidator(func=<function parse_datetime at 0x1090c2660>, json_schema_input_type=PydanticUndefined)]` | yes |
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

`sdk.iter_assets_overview(...)` paginates for you and accepts filter kwargs.

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig


def main() -> None:
    sdk = TurbineClient(TurbineClientConfig.from_env())

    for item in sdk.iter_assets_overview(page_size=10, max_pages=1):
        print(item.id, item.name)


if __name__ == "__main__":
    main()
```

## Raw client

Same data via `client.query_assets_overview` when you need exact GraphQL control.

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
        # Responses are typed Pydantic models: read fields as attributes.
        for edge in resp.assets_overview.edges or []:
            node = edge.node
            print(node.name, node.version, node.composed_asset_id)


if __name__ == "__main__":
    main()
```
