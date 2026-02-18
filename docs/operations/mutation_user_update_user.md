<!-- Generated file: do not edit by hand -->

# mutation_user_update_user

Modify user profile information including name and contact email details.

## Parameters

| name | type | required |
| --- | --- | --- |
| `user_update_user_args` | `UpdateUserInput` | `true` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `user` | `object` | yes |
| `user.updateUser` | `object` | yes |
| `user.updateUser.id` | `string` | no |
| `user.updateUser.createdAt` | `string` | yes |
| `user.updateUser.deletedAt` | `string` | yes |
| `user.updateUser.disabled` | `boolean` | yes |
| `user.updateUser.disabledReason` | `string` | yes |
| `user.updateUser.email` | `string` | no |
| `user.updateUser.failedLoginAttempts` | `integer` | yes |
| `user.updateUser.isOrgDomainUser` | `boolean` | yes |
| `user.updateUser.lastFailedLogin` | `string` | yes |
| `user.updateUser.lastPasswordReset` | `string` | yes |
| `user.updateUser.lastSuccessfulLogin` | `string` | yes |
| `user.updateUser.name` | `string` | no |
| `user.updateUser.organization` | `string` | yes |
| `user.updateUser.passwordDisabled` | `boolean` | yes |
| `user.updateUser.picture` | `string` | yes |
| `user.updateUser.role` | `string` | yes |
| `user.updateUser.updatedAt` | `string` | yes |
| `user.updateUser.verified` | `boolean` | yes |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    UpdateUserInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.mutation_user_update_user(user_update_user_args=UpdateUserInput(user_id='user_123'))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
