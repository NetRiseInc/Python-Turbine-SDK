<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# mutation_user_update_user

[Back to the index](../README.md)

Update a user's name or email.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |
| `user_update_user_args` | `UpdateUserInput` | `true` |

## Response fields

Typed attributes on the response model.

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
        # Responses are typed Pydantic models: read fields as attributes.
        print(resp.user.update_user.id, resp.user.update_user.name)


if __name__ == "__main__":
    main()
```
