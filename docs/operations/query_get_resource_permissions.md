<!-- Generated file: do not edit by hand -->

# query_get_resource_permissions

Retrieve the caller's effective permissions on a specific resource, defaulting to the organization level.

## Parameters

| name | type | required |
| --- | --- | --- |
| `get_resource_permissions_resource_type` | `AcrResourceType` | `true` |
| `get_resource_permissions_resource_id` | `Union[str, None, UnsetType]` | `false` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `getResourcePermissions` | `object` | yes |
| `getResourcePermissions.permissions[]` | `string` | no |
| `getResourcePermissions.resourceId` | `string` | no |
| `getResourcePermissions.resourceType` | `AcrResourceType` | no |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.enums import (
    AcrResourceType,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_get_resource_permissions(get_resource_permissions_resource_type=AcrResourceType.ORGANIZATION)
        # Responses are typed Pydantic models: read fields as attributes.
        print(resp.get_resource_permissions.resource_id, resp.get_resource_permissions.resource_type)


if __name__ == "__main__":
    main()
```
