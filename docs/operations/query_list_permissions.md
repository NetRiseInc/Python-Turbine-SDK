<!-- Generated file: do not edit by hand -->

# query_list_permissions

Retrieve the full permission catalog available for building custom roles.

## Parameters

| name | type | required |
| --- | --- | --- |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `listPermissions` | `object` | no |
| `listPermissions.permissions[]` | `object` | no |
| `listPermissions.permissions[].id` | `string` | no |
| `listPermissions.permissions[].category` | `string` | no |
| `listPermissions.permissions[].description` | `string` | no |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_list_permissions()
        # Responses are typed Pydantic models: read fields as attributes.
        for item in resp.list_permissions.permissions or []:
            print(item.id, item.category, item.description)


if __name__ == "__main__":
    main()
```
