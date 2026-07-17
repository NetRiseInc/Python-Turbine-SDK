<!-- Generated file: do not edit by hand -->

# mutation_create_security_group

Create a new RBAC security group in the current organization.

## Parameters

| name | type | required |
| --- | --- | --- |
| `create_security_group_args` | `CreateSecurityGroupInput` | `true` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `createSecurityGroup` | `object` | no |
| `createSecurityGroup.securityGroup` | `object` | yes |
| `createSecurityGroup.securityGroup.id` | `string` | no |
| `createSecurityGroup.securityGroup.createdBy` | `string` | yes |
| `createSecurityGroup.securityGroup.createdTime` | `string` | yes |
| `createSecurityGroup.securityGroup.description` | `string` | yes |
| `createSecurityGroup.securityGroup.lastModifiedTime` | `string` | yes |
| `createSecurityGroup.securityGroup.lastSeenTime` | `string` | yes |
| `createSecurityGroup.securityGroup.memberCount` | `integer` | yes |
| `createSecurityGroup.securityGroup.members[]` | `object` | no |
| `createSecurityGroup.securityGroup.members[].displayName` | `string` | yes |
| `createSecurityGroup.securityGroup.members[].email` | `string` | no |
| `createSecurityGroup.securityGroup.members[].userId` | `string` | no |
| `createSecurityGroup.securityGroup.name` | `string` | no |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    CreateSecurityGroupInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.mutation_create_security_group(create_security_group_args=CreateSecurityGroupInput(name='my-example'))
        # Responses are typed Pydantic models: read fields as attributes.
        print(resp.create_security_group.security_group.id, resp.create_security_group.security_group.name)


if __name__ == "__main__":
    main()
```
