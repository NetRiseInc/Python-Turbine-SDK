<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# mutation_add_sso_group_mapping

[Back to the index](../README.md)

Add one IdP group-to-security-group mapping rule.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |
| `add_sso_group_mapping_args` | `AddSsoGroupMappingInput` | `true` |

## Response fields

Typed attributes on the response model.

| Field | Type | Nullable |
| --- | --- | --- |
| `addSsoGroupMapping` | `object` | no |
| `addSsoGroupMapping.mapping` | `object` | yes |
| `addSsoGroupMapping.mapping.createdAt` | `string` | yes |
| `addSsoGroupMapping.mapping.idpGroupKey` | `string` | yes |
| `addSsoGroupMapping.mapping.idpGroupLabel` | `string` | yes |
| `addSsoGroupMapping.mapping.lastSyncedAt` | `string` | yes |
| `addSsoGroupMapping.mapping.mappingId` | `string` | no |
| `addSsoGroupMapping.mapping.memberCount` | `integer` | yes |
| `addSsoGroupMapping.mapping.ruleType` | `SsoGroupRuleType` | no |
| `addSsoGroupMapping.mapping.securityGroupId` | `string` | yes |
| `addSsoGroupMapping.mapping.securityGroupName` | `string` | yes |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    AddSsoGroupMappingInput,
    SsoGroupMappingInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.mutation_add_sso_group_mapping(add_sso_group_mapping_args=AddSsoGroupMappingInput(mapping=SsoGroupMappingInput()))
        # Responses are typed Pydantic models: read fields as attributes.
        print(resp.add_sso_group_mapping.mapping.created_at, resp.add_sso_group_mapping.mapping.idp_group_key)


if __name__ == "__main__":
    main()
```
