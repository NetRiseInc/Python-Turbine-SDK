<!-- Generated file: do not edit by hand -->

# query_jira_integration_setup

Retrieve the current state of the Jira integration setup wizard.

## Parameters

| name | type | required |
| --- | --- | --- |
| `jira_integration_setup_args` | `Union[JiraIntegrationSetupInput, None, UnsetType]` | `false` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `jiraIntegrationSetup` | `object` | no |
| `jiraIntegrationSetup.appVersion` | `string` | yes |
| `jiraIntegrationSetup.availableSites[]` | `object` | no |
| `jiraIntegrationSetup.availableSites[].id` | `string` | no |
| `jiraIntegrationSetup.availableSites[].selectable` | `boolean` | no |
| `jiraIntegrationSetup.availableSites[].url` | `string` | no |
| `jiraIntegrationSetup.availableSpaces[]` | `object` | no |
| `jiraIntegrationSetup.availableSpaces[].id` | `string` | no |
| `jiraIntegrationSetup.availableSpaces[].avatarUrl` | `string` | yes |
| `jiraIntegrationSetup.availableSpaces[].name` | `string` | no |
| `jiraIntegrationSetup.availableSpaces[].openTicketsCount` | `integer` | no |
| `jiraIntegrationSetup.availableSpaces[].selected` | `boolean` | no |
| `jiraIntegrationSetup.currentStep` | `JiraSetupStep` | no |
| `jiraIntegrationSetup.error` | `object` | yes |
| `jiraIntegrationSetup.error.message` | `string` | no |
| `jiraIntegrationSetup.error.title` | `string` | no |
| `jiraIntegrationSetup.instanceUrl` | `string` | yes |
| `jiraIntegrationSetup.mode` | `JiraSetupMode` | no |
| `jiraIntegrationSetup.primaryAction` | `object` | no |
| `jiraIntegrationSetup.primaryAction.actionType` | `JiraSetupActionType` | no |
| `jiraIntegrationSetup.primaryAction.disabled` | `boolean` | no |
| `jiraIntegrationSetup.primaryAction.label` | `string` | no |
| `jiraIntegrationSetup.primaryAction.loading` | `boolean` | no |
| `jiraIntegrationSetup.primaryAction.url` | `string` | yes |
| `jiraIntegrationSetup.reconnectSummary` | `object` | yes |
| `jiraIntegrationSetup.reconnectSummary.connectedSpacesCount` | `integer` | no |
| `jiraIntegrationSetup.selectedSiteId` | `string` | yes |
| `jiraIntegrationSetup.selectedSpaceIds[]` | `string` | no |
| `jiraIntegrationSetup.steps[]` | `object` | no |
| `jiraIntegrationSetup.steps[].description` | `string` | yes |
| `jiraIntegrationSetup.steps[].detail` | `string` | yes |
| `jiraIntegrationSetup.steps[].status` | `JiraSetupStepStatus` | no |
| `jiraIntegrationSetup.steps[].step` | `JiraSetupStep` | no |
| `jiraIntegrationSetup.steps[].title` | `string` | no |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    JiraIntegrationSetupInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_jira_integration_setup(jira_integration_setup_args=JiraIntegrationSetupInput())
        # Responses are typed Pydantic models: read fields as attributes.
        for item in resp.jira_integration_setup.available_sites or []:
            print(item.id, item.selectable, item.url)


if __name__ == "__main__":
    main()
```
