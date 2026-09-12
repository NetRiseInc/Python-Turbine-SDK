<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# query_get_resource_permissions

[Back to the index](../README.md)

List the caller's effective permissions on a resource.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |
| `get_resource_permissions_resource_type` | `AcrResourceType` | `true` |
| `get_resource_permissions_resource_id` | `Union[str, None, UnsetType]` | `false` |

## Response fields

Typed attributes on the response model.

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
