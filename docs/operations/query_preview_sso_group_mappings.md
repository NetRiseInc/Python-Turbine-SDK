<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# query_preview_sso_group_mappings

[Back to the index](../README.md)

Test mapping rules against observed SSO claims without saving.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |
| `preview_sso_group_mappings_args` | `PreviewSsoGroupMappingsInput` | `true` |

## Response fields

Typed attributes on the response model.

| Field | Type | Nullable |
| --- | --- | --- |
| `previewSsoGroupMappings` | `object` | no |
| `previewSsoGroupMappings.catchAllSecurityGroupIds[]` | `string` | no |
| `previewSsoGroupMappings.identity` | `object` | yes |
| `previewSsoGroupMappings.identity.displayName` | `string` | yes |
| `previewSsoGroupMappings.identity.email` | `string` | yes |
| `previewSsoGroupMappings.matchedGroups[]` | `object` | no |
| `previewSsoGroupMappings.matchedGroups[].idpGroupKey` | `string` | no |
| `previewSsoGroupMappings.matchedGroups[].idpGroupLabel` | `string` | yes |
| `previewSsoGroupMappings.matchedGroups[].securityGroupId` | `string` | no |
| `previewSsoGroupMappings.unmatchedGroupKeys[]` | `string` | no |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    PreviewSsoGroupMappingsInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_preview_sso_group_mappings(preview_sso_group_mappings_args=PreviewSsoGroupMappingsInput(test_id='id_123'))
        # Responses are typed Pydantic models: read fields as attributes.
        for item in resp.preview_sso_group_mappings.matched_groups or []:
            print(item.idp_group_key, item.idp_group_label, item.security_group_id)


if __name__ == "__main__":
    main()
```
