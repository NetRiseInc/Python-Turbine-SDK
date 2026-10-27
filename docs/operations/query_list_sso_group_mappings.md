<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# query_list_sso_group_mappings

[Back to the index](../README.md)

List the IdP group mapping rules on the SSO connection.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |
| `list_sso_group_mappings_connection_id` | `Union[str, None, UnsetType]` | `false` |

## Response fields

Typed attributes on the response model.

| Field | Type | Nullable |
| --- | --- | --- |
| `listSsoGroupMappings` | `object` | no |
| `listSsoGroupMappings.mappings[]` | `object` | no |
| `listSsoGroupMappings.mappings[].createdAt` | `string` | yes |
| `listSsoGroupMappings.mappings[].idpGroupKey` | `string` | yes |
| `listSsoGroupMappings.mappings[].idpGroupLabel` | `string` | yes |
| `listSsoGroupMappings.mappings[].lastSyncedAt` | `string` | yes |
| `listSsoGroupMappings.mappings[].mappingId` | `string` | no |
| `listSsoGroupMappings.mappings[].memberCount` | `integer` | yes |
| `listSsoGroupMappings.mappings[].ruleType` | `SsoGroupRuleType` | no |
| `listSsoGroupMappings.mappings[].securityGroupId` | `string` | yes |
| `listSsoGroupMappings.mappings[].securityGroupName` | `string` | yes |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_list_sso_group_mappings()
        # Responses are typed Pydantic models: read fields as attributes.
        for item in resp.list_sso_group_mappings.mappings or []:
            print(item.created_at, item.idp_group_key, item.idp_group_label)


if __name__ == "__main__":
    main()
```
