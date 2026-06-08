<!-- Generated file: do not edit by hand -->

# mutation_notify_notification_configuration

Send a test notification using an existing notification configuration.

## Parameters

| name | type | required |
| --- | --- | --- |
| `notify_notification_configuration_args` | `NotifyNotificationConfigurationInput` | `true` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `notifyNotificationConfiguration` | `boolean` | no |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    NotifyNotificationConfigurationInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.mutation_notify_notification_configuration(notify_notification_configuration_args=NotifyNotificationConfigurationInput(id='id_123'))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
