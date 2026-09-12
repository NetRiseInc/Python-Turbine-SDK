<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# query_asset_groups

[Back to the index](../README.md)

List asset groups with pagination and filters.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |
| `asset_groups_args` | `AssetGroupsInput` | `true` |

## Response fields

Typed attributes on the response model.

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

`sdk.iter_asset_groups(...)` paginates for you and accepts filter kwargs.

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig


def main() -> None:
    sdk = TurbineClient(TurbineClientConfig.from_env())

    for item in sdk.iter_asset_groups(asset_id="asset_123", page_size=10, max_pages=1):
        print(item)


if __name__ == "__main__":
    main()
```

## Raw client

Same data via `client.query_asset_groups` when you need exact GraphQL control.

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
        # Responses are typed Pydantic models: read fields as attributes.
        for edge in resp.asset_groups.edges or []:
            node = edge.node
            print(node.id, node.name, node.assets_count)


if __name__ == "__main__":
    main()
```
