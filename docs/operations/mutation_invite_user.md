<!-- Generated file: do not edit by hand -->

# mutation_invite_user

Invite a user to the organization with a role and optional security group memberships.

## Parameters

| name | type | required |
| --- | --- | --- |
| `invite_user_args` | `InviteOrgUserInput` | `true` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `inviteUser` | `object` | no |
| `inviteUser.user` | `object` | yes |
| `inviteUser.user.id` | `string` | no |
| `inviteUser.user.accessibleAssetCount` | `integer` | yes |
| `inviteUser.user.acrs[]` | `object` | no |
| `inviteUser.user.acrs[].id` | `string` | no |
| `inviteUser.user.acrs[].createdBy` | `string` | yes |
| `inviteUser.user.acrs[].createdTime` | `string` | yes |
| `inviteUser.user.acrs[].directPermissions[]` | `string` | no |
| `inviteUser.user.acrs[].entityId` | `string` | no |
| `inviteUser.user.acrs[].entityMemberCount` | `integer` | yes |
| `inviteUser.user.acrs[].entityName` | `string` | yes |
| `inviteUser.user.acrs[].entityType` | `AcrEntityType` | no |
| `inviteUser.user.acrs[].expiresAt` | `string` | yes |
| `inviteUser.user.acrs[].lastModifiedBy` | `string` | yes |
| `inviteUser.user.acrs[].lastModifiedTime` | `string` | yes |
| `inviteUser.user.acrs[].orgId` | `string` | no |
| `inviteUser.user.acrs[].resourceId` | `string` | yes |
| `inviteUser.user.acrs[].resourceName` | `string` | yes |
| `inviteUser.user.acrs[].resourceType` | `AcrResourceType` | no |
| `inviteUser.user.acrs[].roleId` | `string` | yes |
| `inviteUser.user.acrs[].roleName` | `string` | yes |
| `inviteUser.user.acrs[].rolePermissions[]` | `string` | no |
| `inviteUser.user.acrs[].userEmails[]` | `string` | no |
| `inviteUser.user.createdTime` | `string` | yes |
| `inviteUser.user.disabledAt` | `string` | yes |
| `inviteUser.user.disabledBy` | `string` | yes |
| `inviteUser.user.displayName` | `string` | yes |
| `inviteUser.user.email` | `string` | no |
| `inviteUser.user.emailVerified` | `boolean` | no |
| `inviteUser.user.isExternal` | `boolean` | no |
| `inviteUser.user.lastModifiedTime` | `string` | yes |
| `inviteUser.user.lastSeenTime` | `string` | yes |
| `inviteUser.user.orgId` | `string` | no |
| `inviteUser.user.permissionCount` | `integer` | yes |
| `inviteUser.user.securityGroups[]` | `object` | no |
| `inviteUser.user.securityGroups[].id` | `string` | no |
| `inviteUser.user.securityGroups[].maxRolePrecedence` | `integer` | no |
| `inviteUser.user.securityGroups[].name` | `string` | no |
| `inviteUser.user.status` | `OrgUserStatus` | yes |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    InviteOrgUserInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.mutation_invite_user(invite_user_args=InviteOrgUserInput(email='user@example.com'))
        # Responses are typed Pydantic models: read fields as attributes.
        print(resp.invite_user.user.id, resp.invite_user.user.status)


if __name__ == "__main__":
    main()
```
