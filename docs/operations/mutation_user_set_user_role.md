<!-- Generated file: do not edit by hand -->

# mutation_user_set_user_role

Assign a new permission role like Owner or Operator to users.

## Parameters

| name | type | required |
| --- | --- | --- |
| `user_set_user_role_args` | `SetUserRoleInput` | `true` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `user` | `object` | yes |
| `user.setUserRole` | `object` | yes |
| `user.setUserRole.id` | `string` | no |
| `user.setUserRole.createdAt` | `string` | yes |
| `user.setUserRole.deletedAt` | `string` | yes |
| `user.setUserRole.disabled` | `boolean` | yes |
| `user.setUserRole.disabledReason` | `string` | yes |
| `user.setUserRole.email` | `string` | no |
| `user.setUserRole.failedLoginAttempts` | `integer` | yes |
| `user.setUserRole.isOrgDomainUser` | `boolean` | yes |
| `user.setUserRole.lastFailedLogin` | `string` | yes |
| `user.setUserRole.lastPasswordReset` | `string` | yes |
| `user.setUserRole.lastSuccessfulLogin` | `string` | yes |
| `user.setUserRole.name` | `string` | no |
| `user.setUserRole.organization` | `string` | yes |
| `user.setUserRole.passwordDisabled` | `boolean` | yes |
| `user.setUserRole.picture` | `string` | yes |
| `user.setUserRole.role` | `string` | yes |
| `user.setUserRole.updatedAt` | `string` | yes |
| `user.setUserRole.verified` | `boolean` | yes |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    SetUserRoleInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.mutation_user_set_user_role(user_set_user_role_args=SetUserRoleInput(next_role='VIEWER', user_id='user_123'))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
