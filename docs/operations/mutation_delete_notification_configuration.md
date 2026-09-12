<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# mutation_delete_notification_configuration

[Back to the index](../README.md)

Delete a notification configuration by ID.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |
| `delete_notification_configuration_args` | `DeleteNotificationConfigurationInput` | `true` |

## Response fields

Typed attributes on the response model.

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
