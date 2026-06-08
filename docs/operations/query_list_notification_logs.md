<!-- Generated file: do not edit by hand -->

# query_list_notification_logs

Retrieve a paginated log of notification delivery events and their statuses.

## Parameters

| name | type | required |
| --- | --- | --- |
| `list_notification_logs_args` | `ListNotificationLogsInput` | `true` |

## Response Schema

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
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
