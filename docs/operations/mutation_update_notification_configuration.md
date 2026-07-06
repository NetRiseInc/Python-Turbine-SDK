<!-- Generated file: do not edit by hand -->

# mutation_update_notification_configuration

Update channel, scopes, triggers, or status for an existing notification configuration.

## Parameters

| name | type | required |
| --- | --- | --- |
| `update_notification_configuration_args` | `UpdateNotificationConfigurationInput` | `true` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `updateNotificationConfiguration` | `object` | yes |
| `updateNotificationConfiguration.id` | `string` | yes |
| `updateNotificationConfiguration.activityScopes[]` | `object` | no |
| `updateNotificationConfiguration.activityScopes[].activityType` | `NotificationActivityKind` | yes |
| `updateNotificationConfiguration.activityScopes[].entityType` | `ActivityEntityType` | yes |
| `updateNotificationConfiguration.activityScopes[].threshold` | `object` | yes |
| `updateNotificationConfiguration.activityScopes[].threshold.key` | `NotificationActivityThresholdField` | no |
| `updateNotificationConfiguration.activityScopes[].threshold.operator` | `NotificationActivityThresholdOperator` | no |
| `updateNotificationConfiguration.activityScopes[].threshold.value` | `string` | no |
| `updateNotificationConfiguration.channel` | `NotificationConfigurationChannel` | yes |
| `updateNotificationConfiguration.channelConfiguration` | `typing.Annotated[typing.Union[netrise_turbine_sdk_graphql.mutation_update_notification_configuration.MutationUpdateNotificationConfigurationUpdateNotificationConfigurationChannelConfigurationNotificationConfigurationWebhook, netrise_turbine_sdk_graphql.mutation_update_notification_configuration.MutationUpdateNotificationConfigurationUpdateNotificationConfigurationChannelConfigurationNotificationConfigurationEmail, netrise_turbine_sdk_graphql.mutation_update_notification_configuration.MutationUpdateNotificationConfigurationUpdateNotificationConfigurationChannelConfigurationNotificationConfigurationApplication], FieldInfo(annotation=NoneType, required=True, discriminator='typename__')]` | yes |
| `updateNotificationConfiguration.createdAt` | `string` | yes |
| `updateNotificationConfiguration.disabled` | `boolean` | yes |
| `updateNotificationConfiguration.inventoryScopes[]` | `object` | no |
| `updateNotificationConfiguration.inventoryScopes[].assetId` | `string` | yes |
| `updateNotificationConfiguration.inventoryScopes[].groupId` | `string` | yes |
| `updateNotificationConfiguration.inventoryScopes[].organization` | `boolean` | yes |
| `updateNotificationConfiguration.name` | `string` | yes |
| `updateNotificationConfiguration.silenced` | `boolean` | yes |
| `updateNotificationConfiguration.type` | `NotificationConfigurationType` | yes |
| `updateNotificationConfiguration.updatedAt` | `string` | yes |
| `updateNotificationConfiguration.updatedBy` | `string` | yes |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    NotificationChannelConfigurationInput,
    NotificationConfigurationUpdateInput,
    UpdateNotificationConfigurationInput,
)
from netrise_turbine_sdk_graphql.enums import (
    NotificationConfigurationChannel,
    NotificationConfigurationType,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.mutation_update_notification_configuration(update_notification_configuration_args=UpdateNotificationConfigurationInput(configuration=NotificationConfigurationUpdateInput(id='id_123', name='my-example', disabled=True, silenced=True, type=NotificationConfigurationType.NOTIFICATION_TYPE_UNSPECIFIED, channel=NotificationConfigurationChannel.NOTIFICATION_CHANNEL_UNSPECIFIED, activity_scopes=[None], channel_configuration=NotificationChannelConfigurationInput())))
        # Responses are typed Pydantic models: read fields as attributes.
        print(resp.update_notification_configuration.id, resp.update_notification_configuration.name)


if __name__ == "__main__":
    main()
```
