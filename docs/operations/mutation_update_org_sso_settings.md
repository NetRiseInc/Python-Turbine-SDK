<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# mutation_update_org_sso_settings

[Back to the index](../README.md)

Update org sign-in settings, such as SSO-only login.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |
| `update_org_sso_settings_args` | `UpdateOrgSsoSettingsInput` | `true` |

## Response fields

Typed attributes on the response model.

| Field | Type | Nullable |
| --- | --- | --- |
| `updateOrgSsoSettings` | `object` | no |
| `updateOrgSsoSettings.settings` | `object` | yes |
| `updateOrgSsoSettings.settings.enforcedDomains[]` | `string` | no |
| `updateOrgSsoSettings.settings.userPassAuthDisabled` | `boolean` | no |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    UpdateOrgSsoSettingsInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.mutation_update_org_sso_settings(update_org_sso_settings_args=UpdateOrgSsoSettingsInput())
        # Responses are typed Pydantic models: read fields as attributes.
        print(resp.update_org_sso_settings.settings.user_pass_auth_disabled)


if __name__ == "__main__":
    main()
```
