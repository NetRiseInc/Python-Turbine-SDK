<!-- Generated file: do not edit by hand -->

# mutation_delete_custom_role

Permanently delete a custom role from the organization.

## Parameters

| name | type | required |
| --- | --- | --- |
| `delete_custom_role_args` | `DeleteCustomRoleInput` | `true` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `deleteCustomRole` | `object` | no |
| `deleteCustomRole.roleId` | `string` | no |
| `deleteCustomRole.success` | `boolean` | no |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    DeleteCustomRoleInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.mutation_delete_custom_role(delete_custom_role_args=DeleteCustomRoleInput(role_id='id_123'))
        # Responses are typed Pydantic models: read fields as attributes.
        print(resp.delete_custom_role.role_id, resp.delete_custom_role.success)


if __name__ == "__main__":
    main()
```
