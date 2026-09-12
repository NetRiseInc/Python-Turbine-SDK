<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# query_list_notification_logs

[Back to the index](../README.md)

List notification delivery events and statuses.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |
| `list_notification_logs_args` | `ListNotificationLogsInput` | `true` |

## Response fields

Typed attributes on the response model.

| Field | Type | Nullable |
| --- | --- | --- |
| `listNotificationLogs` | `object` | no |
| `listNotificationLogs.edges[]` | `object` | yes |
| `listNotificationLogs.edges[].cursor` | `string` | yes |
| `listNotificationLogs.edges[].node` | `object` | yes |
| `listNotificationLogs.edges[].node.eventCount` | `integer` | yes |
| `listNotificationLogs.edges[].node.messages[]` | `string` | yes |
| `listNotificationLogs.edges[].node.notificationConfigurationId` | `string` | yes |
| `listNotificationLogs.edges[].node.status` | `NotificationLogStatus` | yes |
| `listNotificationLogs.edges[].node.timestamp` | `string` | yes |
| `listNotificationLogs.pageInfo` | `object` | no |
| `listNotificationLogs.pageInfo.endCursor` | `string` | yes |
| `listNotificationLogs.pageInfo.hasNextPage` | `boolean` | no |
| `listNotificationLogs.pageInfo.hasPreviousPage` | `boolean` | no |
| `listNotificationLogs.pageInfo.startCursor` | `string` | yes |
| `listNotificationLogs.pageInfo.totalCount` | `integer` | yes |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    ListNotificationLogsInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_list_notification_logs(list_notification_logs_args=ListNotificationLogsInput())
        # Responses are typed Pydantic models: read fields as attributes.
        for edge in resp.list_notification_logs.edges or []:
            node = edge.node
            print(node.status, node.event_count, node.notification_configuration_id)


if __name__ == "__main__":
    main()
```
