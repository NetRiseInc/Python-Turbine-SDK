<!-- Generated file: do not edit by hand -->

# mutation_update_custom_role

Update the name, description, or permissions of an existing custom role.

## Parameters

| name | type | required |
| --- | --- | --- |
| `update_custom_role_args` | `UpdateCustomRoleInput` | `true` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `updateCustomRole` | `object` | no |
| `updateCustomRole.role` | `object` | yes |
| `updateCustomRole.role.id` | `string` | no |
| `updateCustomRole.role.description` | `string` | yes |
| `updateCustomRole.role.isBuiltin` | `boolean` | no |
| `updateCustomRole.role.lastModifiedBy` | `string` | yes |
| `updateCustomRole.role.lastModifiedByEmail` | `string` | yes |
| `updateCustomRole.role.lastModifiedTime` | `string` | yes |
| `updateCustomRole.role.name` | `string` | no |
| `updateCustomRole.role.orgId` | `string` | no |
| `updateCustomRole.role.permissions[]` | `string` | no |
| `updateCustomRole.role.precedence` | `integer` | yes |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    UpdateCustomRoleInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.mutation_update_custom_role(update_custom_role_args=UpdateCustomRoleInput(role_id='id_123', name='my-example', permissions=['value']))
        # Responses are typed Pydantic models: read fields as attributes.
        print(resp.update_custom_role.role.id, resp.update_custom_role.role.name)


if __name__ == "__main__":
    main()
```
