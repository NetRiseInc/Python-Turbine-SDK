<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# query_get_org_sso_settings

[Back to the index](../README.md)

Get the org's sign-in settings and enforced domains.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |

## Response fields

Typed attributes on the response model.

| Field | Type | Nullable |
| --- | --- | --- |
| `getOrgSsoSettings` | `object` | no |
| `getOrgSsoSettings.enforcedDomains[]` | `string` | no |
| `getOrgSsoSettings.userPassAuthDisabled` | `boolean` | no |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_get_org_sso_settings()
        # Responses are typed Pydantic models: read fields as attributes.
        print(resp.get_org_sso_settings.user_pass_auth_disabled)


if __name__ == "__main__":
    main()
```
