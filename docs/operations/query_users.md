<!-- Generated file: do not edit by hand -->

# query_users

Retrieve a detailed list of all users and their assigned roles.

## Parameters

| name | type | required |
| --- | --- | --- |
| `users_args` | `UsersInput` | `true` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `users` | `object` | no |
| `users.edges[]` | `object` | yes |
| `users.edges[].cursor` | `string` | yes |
| `users.edges[].node` | `object` | yes |
| `users.edges[].node.id` | `string` | no |
| `users.edges[].node.createdAt` | `string` | yes |
| `users.edges[].node.deletedAt` | `string` | yes |
| `users.edges[].node.disabled` | `boolean` | yes |
| `users.edges[].node.disabledReason` | `string` | yes |
| `users.edges[].node.email` | `string` | no |
| `users.edges[].node.failedLoginAttempts` | `integer` | yes |
| `users.edges[].node.isOrgDomainUser` | `boolean` | yes |
| `users.edges[].node.lastFailedLogin` | `string` | yes |
| `users.edges[].node.lastPasswordReset` | `string` | yes |
| `users.edges[].node.lastSuccessfulLogin` | `string` | yes |
| `users.edges[].node.name` | `string` | no |
| `users.edges[].node.organization` | `string` | yes |
| `users.edges[].node.passwordDisabled` | `boolean` | yes |
| `users.edges[].node.picture` | `string` | yes |
| `users.edges[].node.role` | `string` | yes |
| `users.edges[].node.updatedAt` | `string` | yes |
| `users.edges[].node.verified` | `boolean` | yes |
| `users.pageInfo` | `object` | no |
| `users.pageInfo.endCursor` | `string` | yes |
| `users.pageInfo.hasNextPage` | `boolean` | no |
| `users.pageInfo.hasPreviousPage` | `boolean` | no |
| `users.pageInfo.startCursor` | `string` | yes |
| `users.pageInfo.totalCount` | `integer` | yes |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    Cursor,
    UsersInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_users(users_args=UsersInput(cursor=Cursor()))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
