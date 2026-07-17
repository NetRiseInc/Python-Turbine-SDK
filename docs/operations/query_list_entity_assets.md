<!-- Generated file: do not edit by hand -->

# query_list_entity_assets

List the assets accessible to a specific user or security group.

## Parameters

| name | type | required |
| --- | --- | --- |
| `list_entity_assets_entity_type` | `AcrEntityType` | `true` |
| `list_entity_assets_entity_id` | `str` | `true` |
| `list_entity_assets_cursor` | `Union[Cursor, None, UnsetType]` | `false` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `listEntityAssets` | `object` | no |
| `listEntityAssets.edges[]` | `object` | yes |
| `listEntityAssets.edges[].cursor` | `string` | yes |
| `listEntityAssets.edges[].node` | `object` | yes |
| `listEntityAssets.edges[].node.id` | `string` | no |
| `listEntityAssets.edges[].node.assetType` | `string` | no |
| `listEntityAssets.edges[].node.name` | `string` | no |
| `listEntityAssets.pageInfo` | `object` | no |
| `listEntityAssets.pageInfo.endCursor` | `string` | yes |
| `listEntityAssets.pageInfo.hasNextPage` | `boolean` | no |
| `listEntityAssets.pageInfo.hasPreviousPage` | `boolean` | no |
| `listEntityAssets.pageInfo.startCursor` | `string` | yes |
| `listEntityAssets.pageInfo.totalCount` | `integer` | yes |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    Cursor,
)
from netrise_turbine_sdk_graphql.enums import (
    AcrEntityType,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_list_entity_assets(list_entity_assets_entity_type=AcrEntityType.USER, list_entity_assets_entity_id='asset_123', list_entity_assets_cursor=Cursor())
        # Responses are typed Pydantic models: read fields as attributes.
        for edge in resp.list_entity_assets.edges or []:
            node = edge.node
            print(node.id, node.name, node.asset_type)


if __name__ == "__main__":
    main()
```
