<!-- Generated file: do not edit by hand -->

# mutation_update_security_group

Update the name or description of an existing security group.

## Parameters

| name | type | required |
| --- | --- | --- |
| `update_security_group_args` | `UpdateSecurityGroupInput` | `true` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `updateSecurityGroup` | `object` | no |
| `updateSecurityGroup.securityGroup` | `object` | yes |
| `updateSecurityGroup.securityGroup.id` | `string` | no |
| `updateSecurityGroup.securityGroup.createdBy` | `string` | yes |
| `updateSecurityGroup.securityGroup.createdTime` | `string` | yes |
| `updateSecurityGroup.securityGroup.description` | `string` | yes |
| `updateSecurityGroup.securityGroup.lastModifiedTime` | `string` | yes |
| `updateSecurityGroup.securityGroup.lastSeenTime` | `string` | yes |
| `updateSecurityGroup.securityGroup.memberCount` | `integer` | yes |
| `updateSecurityGroup.securityGroup.members[]` | `object` | no |
| `updateSecurityGroup.securityGroup.members[].displayName` | `string` | yes |
| `updateSecurityGroup.securityGroup.members[].email` | `string` | no |
| `updateSecurityGroup.securityGroup.members[].userId` | `string` | no |
| `updateSecurityGroup.securityGroup.name` | `string` | no |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    UpdateSecurityGroupInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.mutation_update_security_group(update_security_group_args=UpdateSecurityGroupInput(security_group_id='group_123', name='my-example'))
        # Responses are typed Pydantic models: read fields as attributes.
        print(resp.update_security_group.security_group.id, resp.update_security_group.security_group.name)


if __name__ == "__main__":
    main()
```
