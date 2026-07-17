<!-- Generated file: do not edit by hand -->

# query_list_my_ac_rs

List the access control records that apply to the calling user.

## Parameters

| name | type | required |
| --- | --- | --- |
| `list_my_ac_rs_cursor` | `Union[Cursor, None, UnsetType]` | `false` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `listMyACRs` | `object` | no |
| `listMyACRs.edges[]` | `object` | yes |
| `listMyACRs.edges[].cursor` | `string` | yes |
| `listMyACRs.edges[].node` | `object` | yes |
| `listMyACRs.edges[].node.id` | `string` | no |
| `listMyACRs.edges[].node.createdBy` | `string` | yes |
| `listMyACRs.edges[].node.createdTime` | `string` | yes |
| `listMyACRs.edges[].node.directPermissions[]` | `string` | no |
| `listMyACRs.edges[].node.entityId` | `string` | no |
| `listMyACRs.edges[].node.entityMemberCount` | `integer` | yes |
| `listMyACRs.edges[].node.entityName` | `string` | yes |
| `listMyACRs.edges[].node.entityType` | `AcrEntityType` | no |
| `listMyACRs.edges[].node.expiresAt` | `string` | yes |
| `listMyACRs.edges[].node.lastModifiedBy` | `string` | yes |
| `listMyACRs.edges[].node.lastModifiedTime` | `string` | yes |
| `listMyACRs.edges[].node.orgId` | `string` | no |
| `listMyACRs.edges[].node.resourceId` | `string` | yes |
| `listMyACRs.edges[].node.resourceName` | `string` | yes |
| `listMyACRs.edges[].node.resourceType` | `AcrResourceType` | no |
| `listMyACRs.edges[].node.roleId` | `string` | yes |
| `listMyACRs.edges[].node.roleName` | `string` | yes |
| `listMyACRs.edges[].node.rolePermissions[]` | `string` | no |
| `listMyACRs.edges[].node.userEmails[]` | `string` | no |
| `listMyACRs.pageInfo` | `object` | no |
| `listMyACRs.pageInfo.endCursor` | `string` | yes |
| `listMyACRs.pageInfo.hasNextPage` | `boolean` | no |
| `listMyACRs.pageInfo.hasPreviousPage` | `boolean` | no |
| `listMyACRs.pageInfo.startCursor` | `string` | yes |
| `listMyACRs.pageInfo.totalCount` | `integer` | yes |

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
        resp = client.query_list_my_ac_rs(list_my_ac_rs_cursor=Cursor())
        # Responses are typed Pydantic models: read fields as attributes.
        for edge in resp.list_my_ac_rs.edges or []:
            node = edge.node
            print(node.id, node.created_by, node.created_time)


if __name__ == "__main__":
    main()
```
