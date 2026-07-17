<!-- Generated file: do not edit by hand -->

# mutation_create_custom_role

Create an org-scoped custom role with a chosen set of permissions.

## Parameters

| name | type | required |
| --- | --- | --- |
| `create_custom_role_args` | `CreateCustomRoleInput` | `true` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `createCustomRole` | `object` | no |
| `createCustomRole.role` | `object` | yes |
| `createCustomRole.role.id` | `string` | no |
| `createCustomRole.role.description` | `string` | yes |
| `createCustomRole.role.isBuiltin` | `boolean` | no |
| `createCustomRole.role.lastModifiedBy` | `string` | yes |
| `createCustomRole.role.lastModifiedByEmail` | `string` | yes |
| `createCustomRole.role.lastModifiedTime` | `string` | yes |
| `createCustomRole.role.name` | `string` | no |
| `createCustomRole.role.orgId` | `string` | no |
| `createCustomRole.role.permissions[]` | `string` | no |
| `createCustomRole.role.precedence` | `integer` | yes |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    CreateCustomRoleInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.mutation_create_custom_role(create_custom_role_args=CreateCustomRoleInput(name='my-example', permissions=['value']))
        # Responses are typed Pydantic models: read fields as attributes.
        print(resp.create_custom_role.role.id, resp.create_custom_role.role.name)


if __name__ == "__main__":
    main()
```
