<!-- Generated file: do not edit by hand -->

# mutation_user_action

Perform administrative actions like enabling or disabling specific user accounts.

## Parameters

| name | type | required |
| --- | --- | --- |
| `user_action_args` | `UserActionInput` | `true` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `user` | `object` | yes |
| `user.action` | `object` | yes |
| `user.action.id` | `string` | no |
| `user.action.createdAt` | `string` | yes |
| `user.action.deletedAt` | `string` | yes |
| `user.action.disabled` | `boolean` | yes |
| `user.action.disabledReason` | `string` | yes |
| `user.action.email` | `string` | no |
| `user.action.failedLoginAttempts` | `integer` | yes |
| `user.action.isOrgDomainUser` | `boolean` | yes |
| `user.action.lastFailedLogin` | `string` | yes |
| `user.action.lastPasswordReset` | `string` | yes |
| `user.action.lastSuccessfulLogin` | `string` | yes |
| `user.action.name` | `string` | no |
| `user.action.organization` | `string` | yes |
| `user.action.passwordDisabled` | `boolean` | yes |
| `user.action.picture` | `string` | yes |
| `user.action.role` | `string` | yes |
| `user.action.updatedAt` | `string` | yes |
| `user.action.verified` | `boolean` | yes |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    UserActionInput,
)
from netrise_turbine_sdk_graphql.enums import (
    UserActionEnum,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.mutation_user_action(user_action_args=UserActionInput(type=UserActionEnum.DISABLE, user_id='user_123'))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
