<!-- Generated file: do not edit by hand -->

# query_jira_integration

Retrieve the Jira integration summary and connection health details.

## Parameters

| name | type | required |
| --- | --- | --- |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `jiraIntegration` | `object` | no |
| `jiraIntegration.apiConnectivityActive` | `boolean` | no |
| `jiraIntegration.connectionHealth` | `object` | no |
| `jiraIntegration.connectionHealth.addableSpaces[]` | `object` | no |
| `jiraIntegration.connectionHealth.addableSpaces[].id` | `string` | no |
| `jiraIntegration.connectionHealth.addableSpaces[].avatarUrl` | `string` | yes |
| `jiraIntegration.connectionHealth.addableSpaces[].name` | `string` | no |
| `jiraIntegration.connectionHealth.addableSpaces[].openTicketsCount` | `integer` | no |
| `jiraIntegration.connectionHealth.addableSpaces[].selected` | `boolean` | no |
| `jiraIntegration.connectionHealth.connectedSpaces[]` | `object` | no |
| `jiraIntegration.connectionHealth.connectedSpaces[].id` | `string` | no |
| `jiraIntegration.connectionHealth.connectedSpaces[].avatarUrl` | `string` | yes |
| `jiraIntegration.connectionHealth.connectedSpaces[].category` | `string` | no |
| `jiraIntegration.connectionHealth.connectedSpaces[].iconColorIndex` | `integer` | no |
| `jiraIntegration.connectionHealth.connectedSpaces[].name` | `string` | no |
| `jiraIntegration.connectionHealth.connectedSpaces[].openTicketsCount` | `integer` | no |
| `jiraIntegration.connectionHealth.connectedSpaces[].projectKey` | `string` | no |
| `jiraIntegration.connectionHealth.connectionStatusLabel` | `string` | no |
| `jiraIntegration.connectionHealth.instanceUrl` | `string` | no |
| `jiraIntegration.connectionHealth.metrics` | `object` | no |
| `jiraIntegration.connectionHealth.metrics.connectedSpaces` | `string` | no |
| `jiraIntegration.connectionHealth.metrics.lastSync` | `string` | no |
| `jiraIntegration.connectionHealth.systemChecks[]` | `object` | no |
| `jiraIntegration.connectionHealth.systemChecks[].id` | `string` | no |
| `jiraIntegration.connectionHealth.systemChecks[].description` | `string` | no |
| `jiraIntegration.connectionHealth.systemChecks[].status` | `JiraSystemCheckStatus` | no |
| `jiraIntegration.connectionHealth.systemChecks[].title` | `string` | no |
| `jiraIntegration.instanceUrl` | `string` | yes |
| `jiraIntegration.jiraAppInstalledComplete` | `boolean` | no |
| `jiraIntegration.jiraInstallationId` | `string` | yes |
| `jiraIntegration.lastUpdated` | `string` | yes |
| `jiraIntegration.oauthInstallStepComplete` | `boolean` | no |
| `jiraIntegration.oauthTokenActive` | `boolean` | no |
| `jiraIntegration.spacesCount` | `integer` | yes |
| `jiraIntegration.status` | `JiraIntegrationStatus` | no |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_jira_integration()
        # Responses are typed Pydantic models: read fields as attributes.
        print(resp.jira_integration.status)


if __name__ == "__main__":
    main()
```
