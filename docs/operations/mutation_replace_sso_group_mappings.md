<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# mutation_replace_sso_group_mappings

[Back to the index](../README.md)

Replace the full set of IdP group mapping rules.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |
| `replace_sso_group_mappings_args` | `ReplaceSsoGroupMappingsInput` | `true` |

## Response fields

Typed attributes on the response model.

| Field | Type | Nullable |
| --- | --- | --- |
| `replaceSsoGroupMappings` | `object` | no |
| `replaceSsoGroupMappings.mappings[]` | `object` | no |
| `replaceSsoGroupMappings.mappings[].createdAt` | `string` | yes |
| `replaceSsoGroupMappings.mappings[].idpGroupKey` | `string` | yes |
| `replaceSsoGroupMappings.mappings[].idpGroupLabel` | `string` | yes |
| `replaceSsoGroupMappings.mappings[].lastSyncedAt` | `string` | yes |
| `replaceSsoGroupMappings.mappings[].mappingId` | `string` | no |
| `replaceSsoGroupMappings.mappings[].memberCount` | `integer` | yes |
| `replaceSsoGroupMappings.mappings[].ruleType` | `SsoGroupRuleType` | no |
| `replaceSsoGroupMappings.mappings[].securityGroupId` | `string` | yes |
| `replaceSsoGroupMappings.mappings[].securityGroupName` | `string` | yes |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    ReplaceSsoGroupMappingsInput,
    SsoGroupMappingInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.mutation_replace_sso_group_mappings(replace_sso_group_mappings_args=ReplaceSsoGroupMappingsInput(mappings=[SsoGroupMappingInput()]))
        # Responses are typed Pydantic models: read fields as attributes.
        for item in resp.replace_sso_group_mappings.mappings or []:
            print(item.created_at, item.idp_group_key, item.idp_group_label)


if __name__ == "__main__":
    main()
```
