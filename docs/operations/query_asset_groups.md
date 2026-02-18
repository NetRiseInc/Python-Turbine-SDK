<!-- Generated file: do not edit by hand -->

# query_asset_groups

Retrieve a detailed paginated list of all asset groups available.

## Parameters

| name | type | required |
| --- | --- | --- |
| `asset_groups_args` | `AssetGroupsInput` | `true` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `assetGroups` | `object` | no |
| `assetGroups.edges[]` | `object` | yes |
| `assetGroups.edges[].cursor` | `string` | yes |
| `assetGroups.edges[].node` | `object` | yes |
| `assetGroups.edges[].node.id` | `string` | no |
| `assetGroups.edges[].node.assetsCount` | `integer` | yes |
| `assetGroups.edges[].node.description` | `string` | yes |
| `assetGroups.edges[].node.highestAssetRisk` | `float` | yes |
| `assetGroups.edges[].node.name` | `string` | no |
| `assetGroups.edges[].node.updatedAt` | `string` | yes |
| `assetGroups.pageInfo` | `object` | no |
| `assetGroups.pageInfo.endCursor` | `string` | yes |
| `assetGroups.pageInfo.hasNextPage` | `boolean` | no |
| `assetGroups.pageInfo.hasPreviousPage` | `boolean` | no |
| `assetGroups.pageInfo.startCursor` | `string` | yes |
| `assetGroups.pageInfo.totalCount` | `integer` | yes |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    AssetGroupsInput,
    Cursor,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_asset_groups(asset_groups_args=AssetGroupsInput(cursor=Cursor()))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
