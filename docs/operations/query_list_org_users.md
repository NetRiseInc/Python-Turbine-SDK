<!-- Generated file: do not edit by hand -->

# query_list_org_users

List all users in the organization with their security groups and accessible asset counts.

## Parameters

| name | type | required |
| --- | --- | --- |
| `list_org_users_cursor` | `Union[Cursor, None, UnsetType]` | `false` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `listOrgUsers` | `object` | no |
| `listOrgUsers.edges[]` | `object` | yes |
| `listOrgUsers.edges[].cursor` | `string` | yes |
| `listOrgUsers.edges[].node` | `object` | yes |
| `listOrgUsers.edges[].node.id` | `string` | no |
| `listOrgUsers.edges[].node.accessibleAssetCount` | `integer` | yes |
| `listOrgUsers.edges[].node.acrs[]` | `object` | no |
| `listOrgUsers.edges[].node.acrs[].id` | `string` | no |
| `listOrgUsers.edges[].node.acrs[].createdBy` | `string` | yes |
| `listOrgUsers.edges[].node.acrs[].createdTime` | `string` | yes |
| `listOrgUsers.edges[].node.acrs[].directPermissions[]` | `string` | no |
| `listOrgUsers.edges[].node.acrs[].entityId` | `string` | no |
| `listOrgUsers.edges[].node.acrs[].entityMemberCount` | `integer` | yes |
| `listOrgUsers.edges[].node.acrs[].entityName` | `string` | yes |
| `listOrgUsers.edges[].node.acrs[].entityType` | `AcrEntityType` | no |
| `listOrgUsers.edges[].node.acrs[].expiresAt` | `string` | yes |
| `listOrgUsers.edges[].node.acrs[].lastModifiedBy` | `string` | yes |
| `listOrgUsers.edges[].node.acrs[].lastModifiedTime` | `string` | yes |
| `listOrgUsers.edges[].node.acrs[].orgId` | `string` | no |
| `listOrgUsers.edges[].node.acrs[].resourceId` | `string` | yes |
| `listOrgUsers.edges[].node.acrs[].resourceName` | `string` | yes |
| `listOrgUsers.edges[].node.acrs[].resourceType` | `AcrResourceType` | no |
| `listOrgUsers.edges[].node.acrs[].roleId` | `string` | yes |
| `listOrgUsers.edges[].node.acrs[].roleName` | `string` | yes |
| `listOrgUsers.edges[].node.acrs[].rolePermissions[]` | `string` | no |
| `listOrgUsers.edges[].node.acrs[].userEmails[]` | `string` | no |
| `listOrgUsers.edges[].node.createdTime` | `string` | yes |
| `listOrgUsers.edges[].node.disabledAt` | `string` | yes |
| `listOrgUsers.edges[].node.disabledBy` | `string` | yes |
| `listOrgUsers.edges[].node.displayName` | `string` | yes |
| `listOrgUsers.edges[].node.email` | `string` | no |
| `listOrgUsers.edges[].node.emailVerified` | `boolean` | no |
| `listOrgUsers.edges[].node.isExternal` | `boolean` | no |
| `listOrgUsers.edges[].node.lastModifiedTime` | `string` | yes |
| `listOrgUsers.edges[].node.lastSeenTime` | `string` | yes |
| `listOrgUsers.edges[].node.orgId` | `string` | no |
| `listOrgUsers.edges[].node.permissionCount` | `integer` | yes |
| `listOrgUsers.edges[].node.securityGroups[]` | `object` | no |
| `listOrgUsers.edges[].node.securityGroups[].id` | `string` | no |
| `listOrgUsers.edges[].node.securityGroups[].maxRolePrecedence` | `integer` | no |
| `listOrgUsers.edges[].node.securityGroups[].name` | `string` | no |
| `listOrgUsers.edges[].node.status` | `OrgUserStatus` | yes |
| `listOrgUsers.pageInfo` | `object` | no |
| `listOrgUsers.pageInfo.endCursor` | `string` | yes |
| `listOrgUsers.pageInfo.hasNextPage` | `boolean` | no |
| `listOrgUsers.pageInfo.hasPreviousPage` | `boolean` | no |
| `listOrgUsers.pageInfo.startCursor` | `string` | yes |
| `listOrgUsers.pageInfo.totalCount` | `integer` | yes |

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
        resp = client.query_list_org_users(list_org_users_cursor=Cursor())
        # Responses are typed Pydantic models: read fields as attributes.
        for edge in resp.list_org_users.edges or []:
            node = edge.node
            print(node.id, node.status, node.accessible_asset_count)


if __name__ == "__main__":
    main()
```
