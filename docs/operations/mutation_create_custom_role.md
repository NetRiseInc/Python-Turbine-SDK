<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# mutation_create_custom_role

[Back to the index](../README.md)

Create an org-scoped custom role with chosen permissions.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |
| `create_custom_role_args` | `CreateCustomRoleInput` | `true` |

## Response fields

Typed attributes on the response model.

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
