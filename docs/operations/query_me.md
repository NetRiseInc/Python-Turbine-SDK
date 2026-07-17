<!-- Generated file: do not edit by hand -->

# query_me

Retrieve the authenticated user's profile including their editable display name.

## Parameters

| name | type | required |
| --- | --- | --- |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `me` | `object` | yes |
| `me.id` | `string` | no |
| `me.createdAt` | `string` | yes |
| `me.deletedAt` | `string` | yes |
| `me.disabled` | `boolean` | yes |
| `me.disabledReason` | `string` | yes |
| `me.email` | `string` | no |
| `me.failedLoginAttempts` | `integer` | yes |
| `me.isOrgDomainUser` | `boolean` | yes |
| `me.lastFailedLogin` | `string` | yes |
| `me.lastPasswordReset` | `string` | yes |
| `me.lastSuccessfulLogin` | `string` | yes |
| `me.name` | `string` | no |
| `me.organization` | `string` | yes |
| `me.passwordDisabled` | `boolean` | yes |
| `me.picture` | `string` | yes |
| `me.role` | `string` | yes |
| `me.updatedAt` | `string` | yes |
| `me.verified` | `boolean` | yes |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_me()
        # Responses are typed Pydantic models: read fields as attributes.
        print(resp.me.id, resp.me.name)


if __name__ == "__main__":
    main()
```
