<!-- Generated file: do not edit by hand -->

# mutation_set_org_user_status

Enable or disable a user account within the current organization.

## Parameters

| name | type | required |
| --- | --- | --- |
| `set_org_user_status_args` | `SetOrgUserStatusInput` | `true` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `setOrgUserStatus` | `object` | no |
| `setOrgUserStatus.user` | `object` | yes |
| `setOrgUserStatus.user.id` | `string` | no |
| `setOrgUserStatus.user.accessibleAssetCount` | `integer` | yes |
| `setOrgUserStatus.user.acrs[]` | `object` | no |
| `setOrgUserStatus.user.acrs[].id` | `string` | no |
| `setOrgUserStatus.user.acrs[].createdBy` | `string` | yes |
| `setOrgUserStatus.user.acrs[].createdTime` | `string` | yes |
| `setOrgUserStatus.user.acrs[].directPermissions[]` | `string` | no |
| `setOrgUserStatus.user.acrs[].entityId` | `string` | no |
| `setOrgUserStatus.user.acrs[].entityMemberCount` | `integer` | yes |
| `setOrgUserStatus.user.acrs[].entityName` | `string` | yes |
| `setOrgUserStatus.user.acrs[].entityType` | `AcrEntityType` | no |
| `setOrgUserStatus.user.acrs[].expiresAt` | `string` | yes |
| `setOrgUserStatus.user.acrs[].lastModifiedBy` | `string` | yes |
| `setOrgUserStatus.user.acrs[].lastModifiedTime` | `string` | yes |
| `setOrgUserStatus.user.acrs[].orgId` | `string` | no |
| `setOrgUserStatus.user.acrs[].resourceId` | `string` | yes |
| `setOrgUserStatus.user.acrs[].resourceName` | `string` | yes |
| `setOrgUserStatus.user.acrs[].resourceType` | `AcrResourceType` | no |
| `setOrgUserStatus.user.acrs[].roleId` | `string` | yes |
| `setOrgUserStatus.user.acrs[].roleName` | `string` | yes |
| `setOrgUserStatus.user.acrs[].rolePermissions[]` | `string` | no |
| `setOrgUserStatus.user.acrs[].userEmails[]` | `string` | no |
| `setOrgUserStatus.user.createdTime` | `string` | yes |
| `setOrgUserStatus.user.disabledAt` | `string` | yes |
| `setOrgUserStatus.user.disabledBy` | `string` | yes |
| `setOrgUserStatus.user.displayName` | `string` | yes |
| `setOrgUserStatus.user.email` | `string` | no |
| `setOrgUserStatus.user.emailVerified` | `boolean` | no |
| `setOrgUserStatus.user.isExternal` | `boolean` | no |
| `setOrgUserStatus.user.lastModifiedTime` | `string` | yes |
| `setOrgUserStatus.user.lastSeenTime` | `string` | yes |
| `setOrgUserStatus.user.orgId` | `string` | no |
| `setOrgUserStatus.user.permissionCount` | `integer` | yes |
| `setOrgUserStatus.user.securityGroups[]` | `object` | no |
| `setOrgUserStatus.user.securityGroups[].id` | `string` | no |
| `setOrgUserStatus.user.securityGroups[].maxRolePrecedence` | `integer` | no |
| `setOrgUserStatus.user.securityGroups[].name` | `string` | no |
| `setOrgUserStatus.user.status` | `OrgUserStatus` | yes |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    SetOrgUserStatusInput,
)
from netrise_turbine_sdk_graphql.enums import (
    OrgUserStatus,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.mutation_set_org_user_status(set_org_user_status_args=SetOrgUserStatusInput(user_id='user_123', status=OrgUserStatus.ENABLED))
        # Responses are typed Pydantic models: read fields as attributes.
        print(resp.set_org_user_status.user.id, resp.set_org_user_status.user.status)


if __name__ == "__main__":
    main()
```
