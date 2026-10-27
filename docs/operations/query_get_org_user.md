<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# query_get_org_user

[Back to the index](../README.md)

Get one org user by ID.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |
| `get_org_user_user_id` | `str` | `true` |

## Response fields

Typed attributes on the response model.

| Field | Type | Nullable |
| --- | --- | --- |
| `getOrgUser` | `object` | yes |
| `getOrgUser.id` | `string` | no |
| `getOrgUser.accessibleAssetCount` | `integer` | yes |
| `getOrgUser.acrs[]` | `object` | no |
| `getOrgUser.acrs[].id` | `string` | no |
| `getOrgUser.acrs[].createdBy` | `string` | yes |
| `getOrgUser.acrs[].createdTime` | `string` | yes |
| `getOrgUser.acrs[].directPermissions[]` | `string` | no |
| `getOrgUser.acrs[].entityId` | `string` | no |
| `getOrgUser.acrs[].entityMemberCount` | `integer` | yes |
| `getOrgUser.acrs[].entityName` | `string` | yes |
| `getOrgUser.acrs[].entityType` | `AcrEntityType` | no |
| `getOrgUser.acrs[].expiresAt` | `string` | yes |
| `getOrgUser.acrs[].lastModifiedBy` | `string` | yes |
| `getOrgUser.acrs[].lastModifiedTime` | `string` | yes |
| `getOrgUser.acrs[].orgId` | `string` | no |
| `getOrgUser.acrs[].resourceId` | `string` | yes |
| `getOrgUser.acrs[].resourceName` | `string` | yes |
| `getOrgUser.acrs[].resourceType` | `AcrResourceType` | no |
| `getOrgUser.acrs[].roleId` | `string` | yes |
| `getOrgUser.acrs[].roleName` | `string` | yes |
| `getOrgUser.acrs[].rolePermissions[]` | `string` | no |
| `getOrgUser.acrs[].userEmails[]` | `string` | no |
| `getOrgUser.createdTime` | `string` | yes |
| `getOrgUser.disabledAt` | `string` | yes |
| `getOrgUser.disabledBy` | `string` | yes |
| `getOrgUser.displayName` | `string` | yes |
| `getOrgUser.email` | `string` | no |
| `getOrgUser.emailVerified` | `boolean` | no |
| `getOrgUser.isExternal` | `boolean` | no |
| `getOrgUser.lastModifiedTime` | `string` | yes |
| `getOrgUser.lastSeenTime` | `string` | yes |
| `getOrgUser.orgId` | `string` | no |
| `getOrgUser.permissionCount` | `integer` | yes |
| `getOrgUser.securityGroups[]` | `object` | no |
| `getOrgUser.securityGroups[].id` | `string` | no |
| `getOrgUser.securityGroups[].maxRolePrecedence` | `integer` | no |
| `getOrgUser.securityGroups[].name` | `string` | no |
| `getOrgUser.status` | `OrgUserStatus` | yes |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_get_org_user(get_org_user_user_id='user_123')
        # Responses are typed Pydantic models: read fields as attributes.
        print(resp.get_org_user.id, resp.get_org_user.status)


if __name__ == "__main__":
    main()
```
