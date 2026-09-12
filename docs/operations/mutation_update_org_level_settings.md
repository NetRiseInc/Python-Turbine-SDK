<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# mutation_update_org_level_settings

[Back to the index](../README.md)

Update org settings such as idle session timeout.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |
| `update_org_level_settings_args` | `OrgLevelSettingsInput` | `true` |

## Response fields

Typed attributes on the response model.

| Field | Type | Nullable |
| --- | --- | --- |
| `updateOrgLevelSettings` | `object` | yes |
| `updateOrgLevelSettings.err` | `string` | yes |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    OrgLevelSettingsInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.mutation_update_org_level_settings(update_org_level_settings_args=OrgLevelSettingsInput(idle_timout_enabled=True))
        # Responses are typed Pydantic models: read fields as attributes.
        print(resp.update_org_level_settings.err)


if __name__ == "__main__":
    main()
```
