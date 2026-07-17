<!-- Generated file: do not edit by hand -->

# mutation_create_acr

Create an access control record granting a user or security group a role on a resource.

## Parameters

| name | type | required |
| --- | --- | --- |
| `create_acr_args` | `CreateAcrInput` | `true` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `createACR` | `object` | no |
| `createACR.acr` | `object` | yes |
| `createACR.acr.id` | `string` | no |
| `createACR.acr.createdBy` | `string` | yes |
| `createACR.acr.createdTime` | `string` | yes |
| `createACR.acr.directPermissions[]` | `string` | no |
| `createACR.acr.entityId` | `string` | no |
| `createACR.acr.entityMemberCount` | `integer` | yes |
| `createACR.acr.entityName` | `string` | yes |
| `createACR.acr.entityType` | `AcrEntityType` | no |
| `createACR.acr.expiresAt` | `string` | yes |
| `createACR.acr.lastModifiedBy` | `string` | yes |
| `createACR.acr.lastModifiedTime` | `string` | yes |
| `createACR.acr.orgId` | `string` | no |
| `createACR.acr.resourceId` | `string` | yes |
| `createACR.acr.resourceName` | `string` | yes |
| `createACR.acr.resourceType` | `AcrResourceType` | no |
| `createACR.acr.roleId` | `string` | yes |
| `createACR.acr.roleName` | `string` | yes |
| `createACR.acr.rolePermissions[]` | `string` | no |
| `createACR.acr.userEmails[]` | `string` | no |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    AcrBindingInput,
    CreateAcrInput,
)
from netrise_turbine_sdk_graphql.enums import (
    AcrEntityType,
    AcrResourceType,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.mutation_create_acr(create_acr_args=CreateAcrInput(binding=AcrBindingInput(entity_type=AcrEntityType.USER, entity_id='id_123', resource_type=AcrResourceType.ORGANIZATION)))
        # Responses are typed Pydantic models: read fields as attributes.
        print(resp.create_acr.acr.id)


if __name__ == "__main__":
    main()
```
