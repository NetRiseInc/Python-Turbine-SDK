<!-- Generated file: do not edit by hand -->

# mutation_add_security_group_member

Add a user as a member of an RBAC security group.

## Parameters

| name | type | required |
| --- | --- | --- |
| `add_security_group_member_args` | `AddSecurityGroupMemberInput` | `true` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `addSecurityGroupMember` | `object` | no |
| `addSecurityGroupMember.member` | `object` | yes |
| `addSecurityGroupMember.member.accessibleAssetCount` | `integer` | yes |
| `addSecurityGroupMember.member.createdTime` | `string` | yes |
| `addSecurityGroupMember.member.displayName` | `string` | yes |
| `addSecurityGroupMember.member.email` | `string` | yes |
| `addSecurityGroupMember.member.lastSeenTime` | `string` | yes |
| `addSecurityGroupMember.member.source` | `SecurityGroupMemberSource` | no |
| `addSecurityGroupMember.member.userId` | `string` | yes |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    AddSecurityGroupMemberInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.mutation_add_security_group_member(add_security_group_member_args=AddSecurityGroupMemberInput(security_group_id='group_123', user_id='user_123'))
        # Responses are typed Pydantic models: read fields as attributes.
        print(resp.add_security_group_member.member.accessible_asset_count, resp.add_security_group_member.member.created_time)


if __name__ == "__main__":
    main()
```
