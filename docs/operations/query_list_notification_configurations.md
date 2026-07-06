<!-- Generated file: do not edit by hand -->

# query_list_notification_configurations

List all notification configurations with their channels, scopes, and triggers.

## Parameters

| name | type | required |
| --- | --- | --- |
| `list_notification_configurations_args` | `ListNotificationConfigurationsInput` | `true` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `listNotificationConfigurations` | `object` | no |
| `listNotificationConfigurations.edges[]` | `object` | yes |
| `listNotificationConfigurations.edges[].cursor` | `string` | yes |
| `listNotificationConfigurations.edges[].node` | `object` | yes |
| `listNotificationConfigurations.edges[].node.id` | `string` | yes |
| `listNotificationConfigurations.edges[].node.activityScopes[]` | `object` | no |
| `listNotificationConfigurations.edges[].node.activityScopes[].activityType` | `NotificationActivityKind` | yes |
| `listNotificationConfigurations.edges[].node.activityScopes[].entityType` | `ActivityEntityType` | yes |
| `listNotificationConfigurations.edges[].node.activityScopes[].threshold` | `object` | yes |
| `listNotificationConfigurations.edges[].node.activityScopes[].threshold.key` | `NotificationActivityThresholdField` | no |
| `listNotificationConfigurations.edges[].node.activityScopes[].threshold.operator` | `NotificationActivityThresholdOperator` | no |
| `listNotificationConfigurations.edges[].node.activityScopes[].threshold.value` | `string` | no |
| `listNotificationConfigurations.edges[].node.channel` | `NotificationConfigurationChannel` | yes |
| `listNotificationConfigurations.edges[].node.channelConfiguration` | `typing.Annotated[typing.Union[netrise_turbine_sdk_graphql.query_list_notification_configurations.QueryListNotificationConfigurationsListNotificationConfigurationsEdgesNodeChannelConfigurationNotificationConfigurationWebhook, netrise_turbine_sdk_graphql.query_list_notification_configurations.QueryListNotificationConfigurationsListNotificationConfigurationsEdgesNodeChannelConfigurationNotificationConfigurationEmail, netrise_turbine_sdk_graphql.query_list_notification_configurations.QueryListNotificationConfigurationsListNotificationConfigurationsEdgesNodeChannelConfigurationNotificationConfigurationApplication], FieldInfo(annotation=NoneType, required=True, discriminator='typename__')]` | yes |
| `listNotificationConfigurations.edges[].node.createdAt` | `string` | yes |
| `listNotificationConfigurations.edges[].node.disabled` | `boolean` | yes |
| `listNotificationConfigurations.edges[].node.inventoryScopes[]` | `object` | no |
| `listNotificationConfigurations.edges[].node.inventoryScopes[].assetId` | `string` | yes |
| `listNotificationConfigurations.edges[].node.inventoryScopes[].groupId` | `string` | yes |
| `listNotificationConfigurations.edges[].node.inventoryScopes[].organization` | `boolean` | yes |
| `listNotificationConfigurations.edges[].node.name` | `string` | yes |
| `listNotificationConfigurations.edges[].node.silenced` | `boolean` | yes |
| `listNotificationConfigurations.edges[].node.type` | `NotificationConfigurationType` | yes |
| `listNotificationConfigurations.edges[].node.updatedAt` | `string` | yes |
| `listNotificationConfigurations.edges[].node.updatedBy` | `string` | yes |
| `listNotificationConfigurations.pageInfo` | `object` | no |
| `listNotificationConfigurations.pageInfo.endCursor` | `string` | yes |
| `listNotificationConfigurations.pageInfo.hasNextPage` | `boolean` | no |
| `listNotificationConfigurations.pageInfo.hasPreviousPage` | `boolean` | no |
| `listNotificationConfigurations.pageInfo.startCursor` | `string` | yes |
| `listNotificationConfigurations.pageInfo.totalCount` | `integer` | yes |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    ListNotificationConfigurationsInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_list_notification_configurations(list_notification_configurations_args=ListNotificationConfigurationsInput())
        # Responses are typed Pydantic models: read fields as attributes.
        for edge in resp.list_notification_configurations.edges or []:
            node = edge.node
            print(node.id, node.name, node.channel)


if __name__ == "__main__":
    main()
```
