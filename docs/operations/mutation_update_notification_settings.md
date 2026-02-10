<!-- Generated file: do not edit by hand -->

# mutation_update_notification_settings

Configure notification preferences and alert delivery settings for the organization.

## Parameters

| name | type | required |
| --- | --- | --- |
| `update_notification_settings_args` | `UpdateNotificationSettingsInput` | `true` |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    NotificationSettingsInput,
    UpdateNotificationSettingsInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.mutation_update_notification_settings(update_notification_settings_args=UpdateNotificationSettingsInput(settings=NotificationSettingsInput()))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
