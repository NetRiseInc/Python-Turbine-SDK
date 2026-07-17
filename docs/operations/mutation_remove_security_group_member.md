<!-- Generated file: do not edit by hand -->

# mutation_remove_security_group_member

Remove a user from an RBAC security group.

## Parameters

| name | type | required |
| --- | --- | --- |
| `remove_security_group_member_args` | `RemoveSecurityGroupMemberInput` | `true` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `removeSecurityGroupMember` | `object` | no |
| `removeSecurityGroupMember.securityGroupId` | `string` | no |
| `removeSecurityGroupMember.success` | `boolean` | no |
| `removeSecurityGroupMember.userId` | `string` | no |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    RemoveSecurityGroupMemberInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.mutation_remove_security_group_member(remove_security_group_member_args=RemoveSecurityGroupMemberInput(security_group_id='group_123', user_id='user_123'))
        # Responses are typed Pydantic models: read fields as attributes.
        print(resp.remove_security_group_member.security_group_id, resp.remove_security_group_member.success)


if __name__ == "__main__":
    main()
```
