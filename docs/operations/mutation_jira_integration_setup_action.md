<!-- Generated file: do not edit by hand -->

# mutation_jira_integration_setup_action

Perform an action in the Jira integration setup or reconnect flow.

## Parameters

| name | type | required |
| --- | --- | --- |
| `jira_integration_setup_action_args` | `JiraIntegrationSetupActionInput` | `true` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `jiraIntegrationSetupAction` | `object` | no |
| `jiraIntegrationSetupAction.appVersion` | `string` | yes |
| `jiraIntegrationSetupAction.availableSites[]` | `object` | no |
| `jiraIntegrationSetupAction.availableSites[].id` | `string` | no |
| `jiraIntegrationSetupAction.availableSites[].selectable` | `boolean` | no |
| `jiraIntegrationSetupAction.availableSites[].url` | `string` | no |
| `jiraIntegrationSetupAction.availableSpaces[]` | `object` | no |
| `jiraIntegrationSetupAction.availableSpaces[].id` | `string` | no |
| `jiraIntegrationSetupAction.availableSpaces[].avatarUrl` | `string` | yes |
| `jiraIntegrationSetupAction.availableSpaces[].name` | `string` | no |
| `jiraIntegrationSetupAction.availableSpaces[].openTicketsCount` | `integer` | no |
| `jiraIntegrationSetupAction.availableSpaces[].selected` | `boolean` | no |
| `jiraIntegrationSetupAction.currentStep` | `JiraSetupStep` | no |
| `jiraIntegrationSetupAction.error` | `object` | yes |
| `jiraIntegrationSetupAction.error.message` | `string` | no |
| `jiraIntegrationSetupAction.error.title` | `string` | no |
| `jiraIntegrationSetupAction.instanceUrl` | `string` | yes |
| `jiraIntegrationSetupAction.mode` | `JiraSetupMode` | no |
| `jiraIntegrationSetupAction.primaryAction` | `object` | no |
| `jiraIntegrationSetupAction.primaryAction.actionType` | `JiraSetupActionType` | no |
| `jiraIntegrationSetupAction.primaryAction.disabled` | `boolean` | no |
| `jiraIntegrationSetupAction.primaryAction.label` | `string` | no |
| `jiraIntegrationSetupAction.primaryAction.loading` | `boolean` | no |
| `jiraIntegrationSetupAction.primaryAction.url` | `string` | yes |
| `jiraIntegrationSetupAction.reconnectSummary` | `object` | yes |
| `jiraIntegrationSetupAction.reconnectSummary.connectedSpacesCount` | `integer` | no |
| `jiraIntegrationSetupAction.selectedSiteId` | `string` | yes |
| `jiraIntegrationSetupAction.selectedSpaceIds[]` | `string` | no |
| `jiraIntegrationSetupAction.steps[]` | `object` | no |
| `jiraIntegrationSetupAction.steps[].description` | `string` | yes |
| `jiraIntegrationSetupAction.steps[].detail` | `string` | yes |
| `jiraIntegrationSetupAction.steps[].status` | `JiraSetupStepStatus` | no |
| `jiraIntegrationSetupAction.steps[].step` | `JiraSetupStep` | no |
| `jiraIntegrationSetupAction.steps[].title` | `string` | no |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    JiraIntegrationSetupActionInput,
)
from netrise_turbine_sdk_graphql.enums import (
    JiraSetupAction,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.mutation_jira_integration_setup_action(jira_integration_setup_action_args=JiraIntegrationSetupActionInput(action=JiraSetupAction.START))
        # Responses are typed Pydantic models: read fields as attributes.
        for item in resp.jira_integration_setup_action.available_sites or []:
            print(item.id, item.selectable, item.url)


if __name__ == "__main__":
    main()
```
