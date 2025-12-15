<!-- Generated file: do not edit by hand -->

# mutation_update_org_level_settings

## Parameters

| name | type | required |
| --- | --- | --- |
| `update_org_level_settings_args` | `OrgLevelSettingsInput` | `true` |

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
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
