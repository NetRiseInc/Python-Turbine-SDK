<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# mutation_user_reset_password

[Back to the index](../README.md)

Send a password-reset email to a user.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |
| `user_reset_password_args` | `UserInput` | `true` |

## Response fields

Typed attributes on the response model.

| Field | Type | Nullable |
| --- | --- | --- |
| `user` | `object` | yes |
| `user.resetPassword` | `object` | yes |
| `user.resetPassword.id` | `string` | no |
| `user.resetPassword.createdAt` | `string` | yes |
| `user.resetPassword.deletedAt` | `string` | yes |
| `user.resetPassword.disabled` | `boolean` | yes |
| `user.resetPassword.disabledReason` | `string` | yes |
| `user.resetPassword.email` | `string` | no |
| `user.resetPassword.failedLoginAttempts` | `integer` | yes |
| `user.resetPassword.isOrgDomainUser` | `boolean` | yes |
| `user.resetPassword.lastFailedLogin` | `string` | yes |
| `user.resetPassword.lastPasswordReset` | `string` | yes |
| `user.resetPassword.lastSuccessfulLogin` | `string` | yes |
| `user.resetPassword.name` | `string` | no |
| `user.resetPassword.organization` | `string` | yes |
| `user.resetPassword.passwordDisabled` | `boolean` | yes |
| `user.resetPassword.picture` | `string` | yes |
| `user.resetPassword.role` | `string` | yes |
| `user.resetPassword.updatedAt` | `string` | yes |
| `user.resetPassword.verified` | `boolean` | yes |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    UserInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.mutation_user_reset_password(user_reset_password_args=UserInput(id='id_123'))
        # Responses are typed Pydantic models: read fields as attributes.
        print(resp.user.reset_password.id, resp.user.reset_password.name)


if __name__ == "__main__":
    main()
```
