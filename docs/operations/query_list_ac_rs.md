<!-- Generated file: do not edit by hand -->

# query_list_ac_rs

List access control records for the organization, optionally filtered to a specific user.

## Parameters

| name | type | required |
| --- | --- | --- |
| `list_ac_rs_user_id` | `Union[str, None, UnsetType]` | `false` |
| `list_ac_rs_cursor` | `Union[Cursor, None, UnsetType]` | `false` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `listACRs` | `object` | no |
| `listACRs.edges[]` | `object` | yes |
| `listACRs.edges[].cursor` | `string` | yes |
| `listACRs.edges[].node` | `object` | yes |
| `listACRs.edges[].node.id` | `string` | no |
| `listACRs.edges[].node.createdBy` | `string` | yes |
| `listACRs.edges[].node.createdTime` | `string` | yes |
| `listACRs.edges[].node.directPermissions[]` | `string` | no |
| `listACRs.edges[].node.entityId` | `string` | no |
| `listACRs.edges[].node.entityMemberCount` | `integer` | yes |
| `listACRs.edges[].node.entityName` | `string` | yes |
| `listACRs.edges[].node.entityType` | `AcrEntityType` | no |
| `listACRs.edges[].node.expiresAt` | `string` | yes |
| `listACRs.edges[].node.lastModifiedBy` | `string` | yes |
| `listACRs.edges[].node.lastModifiedTime` | `string` | yes |
| `listACRs.edges[].node.orgId` | `string` | no |
| `listACRs.edges[].node.resourceId` | `string` | yes |
| `listACRs.edges[].node.resourceName` | `string` | yes |
| `listACRs.edges[].node.resourceType` | `AcrResourceType` | no |
| `listACRs.edges[].node.roleId` | `string` | yes |
| `listACRs.edges[].node.roleName` | `string` | yes |
| `listACRs.edges[].node.rolePermissions[]` | `string` | no |
| `listACRs.edges[].node.userEmails[]` | `string` | no |
| `listACRs.pageInfo` | `object` | no |
| `listACRs.pageInfo.endCursor` | `string` | yes |
| `listACRs.pageInfo.hasNextPage` | `boolean` | no |
| `listACRs.pageInfo.hasPreviousPage` | `boolean` | no |
| `listACRs.pageInfo.startCursor` | `string` | yes |
| `listACRs.pageInfo.totalCount` | `integer` | yes |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    Cursor,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_list_ac_rs(list_ac_rs_cursor=Cursor())
        # Responses are typed Pydantic models: read fields as attributes.
        for edge in resp.list_ac_rs.edges or []:
            node = edge.node
            print(node.id, node.created_by, node.created_time)


if __name__ == "__main__":
    main()
```
