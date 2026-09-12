<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# query_get_role

[Back to the index](../README.md)

Get one RBAC role by ID.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |
| `get_role_role_id` | `str` | `true` |

## Response fields

Typed attributes on the response model.

| Field | Type | Nullable |
| --- | --- | --- |
| `getRole` | `object` | yes |
| `getRole.id` | `string` | no |
| `getRole.description` | `string` | yes |
| `getRole.isBuiltin` | `boolean` | no |
| `getRole.lastModifiedBy` | `string` | yes |
| `getRole.lastModifiedByEmail` | `string` | yes |
| `getRole.lastModifiedTime` | `string` | yes |
| `getRole.name` | `string` | no |
| `getRole.orgId` | `string` | no |
| `getRole.permissions[]` | `string` | no |
| `getRole.precedence` | `integer` | yes |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_get_role(get_role_role_id='id_123')
        # Responses are typed Pydantic models: read fields as attributes.
        print(resp.get_role.id, resp.get_role.name)


if __name__ == "__main__":
    main()
```
