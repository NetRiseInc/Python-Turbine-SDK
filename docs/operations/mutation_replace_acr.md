<!-- Generated file: do not edit by hand -->

# mutation_replace_acr

Replace an access control record with a new grant in one atomic delete-and-create operation.

## Parameters

| name | type | required |
| --- | --- | --- |
| `replace_acr_args` | `ReplaceAcrInput` | `true` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `replaceACR` | `object` | no |
| `replaceACR.newAcr` | `object` | yes |
| `replaceACR.newAcr.id` | `string` | no |
| `replaceACR.newAcr.createdBy` | `string` | yes |
| `replaceACR.newAcr.createdTime` | `string` | yes |
| `replaceACR.newAcr.directPermissions[]` | `string` | no |
| `replaceACR.newAcr.entityId` | `string` | no |
| `replaceACR.newAcr.entityMemberCount` | `integer` | yes |
| `replaceACR.newAcr.entityName` | `string` | yes |
| `replaceACR.newAcr.entityType` | `AcrEntityType` | no |
| `replaceACR.newAcr.expiresAt` | `string` | yes |
| `replaceACR.newAcr.lastModifiedBy` | `string` | yes |
| `replaceACR.newAcr.lastModifiedTime` | `string` | yes |
| `replaceACR.newAcr.orgId` | `string` | no |
| `replaceACR.newAcr.resourceId` | `string` | yes |
| `replaceACR.newAcr.resourceName` | `string` | yes |
| `replaceACR.newAcr.resourceType` | `AcrResourceType` | no |
| `replaceACR.newAcr.roleId` | `string` | yes |
| `replaceACR.newAcr.roleName` | `string` | yes |
| `replaceACR.newAcr.rolePermissions[]` | `string` | no |
| `replaceACR.newAcr.userEmails[]` | `string` | no |
| `replaceACR.replacedAcr` | `object` | yes |
| `replaceACR.replacedAcr.id` | `string` | no |
| `replaceACR.replacedAcr.createdBy` | `string` | yes |
| `replaceACR.replacedAcr.createdTime` | `string` | yes |
| `replaceACR.replacedAcr.directPermissions[]` | `string` | no |
| `replaceACR.replacedAcr.entityId` | `string` | no |
| `replaceACR.replacedAcr.entityMemberCount` | `integer` | yes |
| `replaceACR.replacedAcr.entityName` | `string` | yes |
| `replaceACR.replacedAcr.entityType` | `AcrEntityType` | no |
| `replaceACR.replacedAcr.expiresAt` | `string` | yes |
| `replaceACR.replacedAcr.lastModifiedBy` | `string` | yes |
| `replaceACR.replacedAcr.lastModifiedTime` | `string` | yes |
| `replaceACR.replacedAcr.orgId` | `string` | no |
| `replaceACR.replacedAcr.resourceId` | `string` | yes |
| `replaceACR.replacedAcr.resourceName` | `string` | yes |
| `replaceACR.replacedAcr.resourceType` | `AcrResourceType` | no |
| `replaceACR.replacedAcr.roleId` | `string` | yes |
| `replaceACR.replacedAcr.roleName` | `string` | yes |
| `replaceACR.replacedAcr.rolePermissions[]` | `string` | no |
| `replaceACR.replacedAcr.userEmails[]` | `string` | no |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    AcrBindingInput,
    ReplaceAcrInput,
)
from netrise_turbine_sdk_graphql.enums import (
    AcrEntityType,
    AcrResourceType,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.mutation_replace_acr(replace_acr_args=ReplaceAcrInput(acr_id='id_123', binding=AcrBindingInput(entity_type=AcrEntityType.USER, entity_id='id_123', resource_type=AcrResourceType.ORGANIZATION)))
        # Responses are typed Pydantic models: read fields as attributes.
        print(resp.replace_acr.new_acr.id, resp.replace_acr.replaced_acr.id)


if __name__ == "__main__":
    main()
```
