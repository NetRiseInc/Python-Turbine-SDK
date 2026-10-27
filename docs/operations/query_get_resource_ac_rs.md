<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# query_get_resource_ac_rs

[Back to the index](../README.md)

List access control records attached to one resource.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |
| `get_resource_ac_rs_resource_type` | `AcrResourceType` | `true` |
| `get_resource_ac_rs_resource_id` | `Union[str, None, UnsetType]` | `false` |

## Response fields

Typed attributes on the response model.

| Field | Type | Nullable |
| --- | --- | --- |
| `getResourceACRs[]` | `object` | no |
| `getResourceACRs[].id` | `string` | no |
| `getResourceACRs[].createdBy` | `string` | yes |
| `getResourceACRs[].createdTime` | `string` | yes |
| `getResourceACRs[].directPermissions[]` | `string` | no |
| `getResourceACRs[].entityId` | `string` | no |
| `getResourceACRs[].entityMemberCount` | `integer` | yes |
| `getResourceACRs[].entityName` | `string` | yes |
| `getResourceACRs[].entityType` | `AcrEntityType` | no |
| `getResourceACRs[].expiresAt` | `string` | yes |
| `getResourceACRs[].lastModifiedBy` | `string` | yes |
| `getResourceACRs[].lastModifiedTime` | `string` | yes |
| `getResourceACRs[].orgId` | `string` | no |
| `getResourceACRs[].resourceId` | `string` | yes |
| `getResourceACRs[].resourceName` | `string` | yes |
| `getResourceACRs[].resourceType` | `AcrResourceType` | no |
| `getResourceACRs[].roleId` | `string` | yes |
| `getResourceACRs[].roleName` | `string` | yes |
| `getResourceACRs[].rolePermissions[]` | `string` | no |
| `getResourceACRs[].userEmails[]` | `string` | no |

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
        resp = client.query_get_resource_ac_rs(get_resource_ac_rs_resource_type=AcrResourceType.ORGANIZATION)
        # Responses are typed Pydantic models: read fields as attributes.
        for item in resp.get_resource_ac_rs or []:
            print(item.id, item.created_by, item.created_time)


if __name__ == "__main__":
    main()
```
