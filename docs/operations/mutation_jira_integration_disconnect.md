<!-- Generated file: do not edit by hand -->

# mutation_jira_integration_disconnect

Disconnect the Jira integration from the organization.

## Parameters

| name | type | required |
| --- | --- | --- |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `jiraIntegrationDisconnect` | `object` | no |
| `jiraIntegrationDisconnect.apiConnectivityActive` | `boolean` | no |
| `jiraIntegrationDisconnect.connectionHealth` | `object` | no |
| `jiraIntegrationDisconnect.connectionHealth.addableSpaces[]` | `object` | no |
| `jiraIntegrationDisconnect.connectionHealth.addableSpaces[].id` | `string` | no |
| `jiraIntegrationDisconnect.connectionHealth.addableSpaces[].avatarUrl` | `string` | yes |
| `jiraIntegrationDisconnect.connectionHealth.addableSpaces[].name` | `string` | no |
| `jiraIntegrationDisconnect.connectionHealth.addableSpaces[].openTicketsCount` | `integer` | no |
| `jiraIntegrationDisconnect.connectionHealth.addableSpaces[].selected` | `boolean` | no |
| `jiraIntegrationDisconnect.connectionHealth.connectedSpaces[]` | `object` | no |
| `jiraIntegrationDisconnect.connectionHealth.connectedSpaces[].id` | `string` | no |
| `jiraIntegrationDisconnect.connectionHealth.connectedSpaces[].avatarUrl` | `string` | yes |
| `jiraIntegrationDisconnect.connectionHealth.connectedSpaces[].category` | `string` | no |
| `jiraIntegrationDisconnect.connectionHealth.connectedSpaces[].iconColorIndex` | `integer` | no |
| `jiraIntegrationDisconnect.connectionHealth.connectedSpaces[].name` | `string` | no |
| `jiraIntegrationDisconnect.connectionHealth.connectedSpaces[].openTicketsCount` | `integer` | no |
| `jiraIntegrationDisconnect.connectionHealth.connectedSpaces[].projectKey` | `string` | no |
| `jiraIntegrationDisconnect.connectionHealth.connectionStatusLabel` | `string` | no |
| `jiraIntegrationDisconnect.connectionHealth.instanceUrl` | `string` | no |
| `jiraIntegrationDisconnect.connectionHealth.metrics` | `object` | no |
| `jiraIntegrationDisconnect.connectionHealth.metrics.connectedSpaces` | `string` | no |
| `jiraIntegrationDisconnect.connectionHealth.metrics.lastSync` | `string` | no |
| `jiraIntegrationDisconnect.connectionHealth.systemChecks[]` | `object` | no |
| `jiraIntegrationDisconnect.connectionHealth.systemChecks[].id` | `string` | no |
| `jiraIntegrationDisconnect.connectionHealth.systemChecks[].description` | `string` | no |
| `jiraIntegrationDisconnect.connectionHealth.systemChecks[].status` | `JiraSystemCheckStatus` | no |
| `jiraIntegrationDisconnect.connectionHealth.systemChecks[].title` | `string` | no |
| `jiraIntegrationDisconnect.instanceUrl` | `string` | yes |
| `jiraIntegrationDisconnect.jiraAppInstalledComplete` | `boolean` | no |
| `jiraIntegrationDisconnect.jiraInstallationId` | `string` | yes |
| `jiraIntegrationDisconnect.lastUpdated` | `string` | yes |
| `jiraIntegrationDisconnect.oauthInstallStepComplete` | `boolean` | no |
| `jiraIntegrationDisconnect.oauthTokenActive` | `boolean` | no |
| `jiraIntegrationDisconnect.spacesCount` | `integer` | yes |
| `jiraIntegrationDisconnect.status` | `JiraIntegrationStatus` | no |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.mutation_jira_integration_disconnect()
        # Responses are typed Pydantic models: read fields as attributes.
        print(resp.jira_integration_disconnect.status)


if __name__ == "__main__":
    main()
```
