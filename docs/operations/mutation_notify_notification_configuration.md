<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# mutation_notify_notification_configuration

[Back to the index](../README.md)

Send a test notification for a configuration.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |
| `notify_notification_configuration_args` | `NotifyNotificationConfigurationInput` | `true` |

## Response fields

Typed attributes on the response model.

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
        # Responses are typed Pydantic models: read fields as attributes.
        print(resp.notify_notification_configuration)


if __name__ == "__main__":
    main()
```
