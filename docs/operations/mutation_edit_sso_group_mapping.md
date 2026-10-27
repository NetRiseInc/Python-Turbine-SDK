<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# mutation_edit_sso_group_mapping

[Back to the index](../README.md)

Replace one IdP group mapping rule in place.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |
| `edit_sso_group_mapping_args` | `EditSsoGroupMappingInput` | `true` |

## Response fields

Typed attributes on the response model.

| Field | Type | Nullable |
| --- | --- | --- |
| `editSsoGroupMapping` | `object` | no |
| `editSsoGroupMapping.mapping` | `object` | yes |
| `editSsoGroupMapping.mapping.createdAt` | `string` | yes |
| `editSsoGroupMapping.mapping.idpGroupKey` | `string` | yes |
| `editSsoGroupMapping.mapping.idpGroupLabel` | `string` | yes |
| `editSsoGroupMapping.mapping.lastSyncedAt` | `string` | yes |
| `editSsoGroupMapping.mapping.mappingId` | `string` | no |
| `editSsoGroupMapping.mapping.memberCount` | `integer` | yes |
| `editSsoGroupMapping.mapping.ruleType` | `SsoGroupRuleType` | no |
| `editSsoGroupMapping.mapping.securityGroupId` | `string` | yes |
| `editSsoGroupMapping.mapping.securityGroupName` | `string` | yes |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    EditSsoGroupMappingInput,
    SsoGroupMappingInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.mutation_edit_sso_group_mapping(edit_sso_group_mapping_args=EditSsoGroupMappingInput(mapping_id='id_123', mapping=SsoGroupMappingInput()))
        # Responses are typed Pydantic models: read fields as attributes.
        print(resp.edit_sso_group_mapping.mapping.created_at, resp.edit_sso_group_mapping.mapping.idp_group_key)


if __name__ == "__main__":
    main()
```
