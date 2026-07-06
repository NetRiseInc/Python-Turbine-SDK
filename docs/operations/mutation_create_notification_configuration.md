<!-- Generated file: do not edit by hand -->

# mutation_create_notification_configuration

Create a notification configuration defining channel, scopes, and triggers for alerts.

## Parameters

| name | type | required |
| --- | --- | --- |
| `create_notification_configuration_args` | `CreateNotificationConfigurationInput` | `true` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `createNotificationConfiguration` | `object` | yes |
| `createNotificationConfiguration.id` | `string` | yes |
| `createNotificationConfiguration.activityScopes[]` | `object` | no |
| `createNotificationConfiguration.activityScopes[].activityType` | `NotificationActivityKind` | yes |
| `createNotificationConfiguration.activityScopes[].entityType` | `ActivityEntityType` | yes |
| `createNotificationConfiguration.activityScopes[].threshold` | `object` | yes |
| `createNotificationConfiguration.activityScopes[].threshold.key` | `NotificationActivityThresholdField` | no |
| `createNotificationConfiguration.activityScopes[].threshold.operator` | `NotificationActivityThresholdOperator` | no |
| `createNotificationConfiguration.activityScopes[].threshold.value` | `string` | no |
| `createNotificationConfiguration.channel` | `NotificationConfigurationChannel` | yes |
| `createNotificationConfiguration.channelConfiguration` | `typing.Annotated[typing.Union[netrise_turbine_sdk_graphql.mutation_create_notification_configuration.MutationCreateNotificationConfigurationCreateNotificationConfigurationChannelConfigurationNotificationConfigurationWebhook, netrise_turbine_sdk_graphql.mutation_create_notification_configuration.MutationCreateNotificationConfigurationCreateNotificationConfigurationChannelConfigurationNotificationConfigurationEmail, netrise_turbine_sdk_graphql.mutation_create_notification_configuration.MutationCreateNotificationConfigurationCreateNotificationConfigurationChannelConfigurationNotificationConfigurationApplication], FieldInfo(annotation=NoneType, required=True, discriminator='typename__')]` | yes |
| `createNotificationConfiguration.createdAt` | `string` | yes |
| `createNotificationConfiguration.disabled` | `boolean` | yes |
| `createNotificationConfiguration.inventoryScopes[]` | `object` | no |
| `createNotificationConfiguration.inventoryScopes[].assetId` | `string` | yes |
| `createNotificationConfiguration.inventoryScopes[].groupId` | `string` | yes |
| `createNotificationConfiguration.inventoryScopes[].organization` | `boolean` | yes |
| `createNotificationConfiguration.name` | `string` | yes |
| `createNotificationConfiguration.silenced` | `boolean` | yes |
| `createNotificationConfiguration.type` | `NotificationConfigurationType` | yes |
| `createNotificationConfiguration.updatedAt` | `string` | yes |
| `createNotificationConfiguration.updatedBy` | `string` | yes |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    CreateNotificationConfigurationInput,
    NotificationConfigurationCreateInput,
)
from netrise_turbine_sdk_graphql.enums import (
    NotificationConfigurationChannel,
    NotificationConfigurationType,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.mutation_create_notification_configuration(create_notification_configuration_args=CreateNotificationConfigurationInput(configuration=NotificationConfigurationCreateInput(type=NotificationConfigurationType.NOTIFICATION_TYPE_UNSPECIFIED, channel=NotificationConfigurationChannel.NOTIFICATION_CHANNEL_UNSPECIFIED, activity_scopes=[None])))
        # Responses are typed Pydantic models: read fields as attributes.
        print(resp.create_notification_configuration.id, resp.create_notification_configuration.name)


if __name__ == "__main__":
    main()
```
