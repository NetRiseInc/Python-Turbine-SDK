<!-- Generated file: do not edit by hand -->

# mutation_user_invite

Invite a new user to the organization with a specific role.

## Parameters

| name | type | required |
| --- | --- | --- |
| `user_invite_args` | `InviteUserInput` | `true` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `user` | `object` | yes |
| `user.invite` | `object` | yes |
| `user.invite.id` | `string` | no |
| `user.invite.createdAt` | `string` | yes |
| `user.invite.deletedAt` | `string` | yes |
| `user.invite.disabled` | `boolean` | yes |
| `user.invite.disabledReason` | `string` | yes |
| `user.invite.email` | `string` | no |
| `user.invite.failedLoginAttempts` | `integer` | yes |
| `user.invite.isOrgDomainUser` | `boolean` | yes |
| `user.invite.lastFailedLogin` | `string` | yes |
| `user.invite.lastPasswordReset` | `string` | yes |
| `user.invite.lastSuccessfulLogin` | `string` | yes |
| `user.invite.name` | `string` | no |
| `user.invite.organization` | `string` | yes |
| `user.invite.passwordDisabled` | `boolean` | yes |
| `user.invite.picture` | `string` | yes |
| `user.invite.role` | `string` | yes |
| `user.invite.updatedAt` | `string` | yes |
| `user.invite.verified` | `boolean` | yes |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    InviteUserInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.mutation_user_invite(user_invite_args=InviteUserInput(email='user@example.com', role='VIEWER'))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
