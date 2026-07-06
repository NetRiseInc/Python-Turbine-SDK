<!-- Generated file: do not edit by hand -->

# mutation_delete_notification_configuration

Permanently delete a notification configuration by its ID.

## Parameters

| name | type | required |
| --- | --- | --- |
| `delete_notification_configuration_args` | `DeleteNotificationConfigurationInput` | `true` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `deleteNotificationConfiguration` | `boolean` | no |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    DeleteNotificationConfigurationInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.mutation_delete_notification_configuration(delete_notification_configuration_args=DeleteNotificationConfigurationInput(id='id_123'))
        # Responses are typed Pydantic models: read fields as attributes.
        print(resp.delete_notification_configuration)


if __name__ == "__main__":
    main()
```
