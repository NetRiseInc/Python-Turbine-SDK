<!-- Generated file: do not edit by hand -->

# mutation_jira_integration_reconnect

Re-enable a Jira installation when the OAuth and app install steps are already complete.

## Parameters

| name | type | required |
| --- | --- | --- |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `jiraIntegrationReconnect` | `object` | no |
| `jiraIntegrationReconnect.apiConnectivityActive` | `boolean` | no |
| `jiraIntegrationReconnect.connectionHealth` | `object` | no |
| `jiraIntegrationReconnect.connectionHealth.addableSpaces[]` | `object` | no |
| `jiraIntegrationReconnect.connectionHealth.addableSpaces[].id` | `string` | no |
| `jiraIntegrationReconnect.connectionHealth.addableSpaces[].avatarUrl` | `string` | yes |
| `jiraIntegrationReconnect.connectionHealth.addableSpaces[].name` | `string` | no |
| `jiraIntegrationReconnect.connectionHealth.addableSpaces[].openTicketsCount` | `integer` | no |
| `jiraIntegrationReconnect.connectionHealth.addableSpaces[].selected` | `boolean` | no |
| `jiraIntegrationReconnect.connectionHealth.connectedSpaces[]` | `object` | no |
| `jiraIntegrationReconnect.connectionHealth.connectedSpaces[].id` | `string` | no |
| `jiraIntegrationReconnect.connectionHealth.connectedSpaces[].avatarUrl` | `string` | yes |
| `jiraIntegrationReconnect.connectionHealth.connectedSpaces[].category` | `string` | no |
| `jiraIntegrationReconnect.connectionHealth.connectedSpaces[].iconColorIndex` | `integer` | no |
| `jiraIntegrationReconnect.connectionHealth.connectedSpaces[].name` | `string` | no |
| `jiraIntegrationReconnect.connectionHealth.connectedSpaces[].openTicketsCount` | `integer` | no |
| `jiraIntegrationReconnect.connectionHealth.connectedSpaces[].projectKey` | `string` | no |
| `jiraIntegrationReconnect.connectionHealth.connectionStatusLabel` | `string` | no |
| `jiraIntegrationReconnect.connectionHealth.instanceUrl` | `string` | no |
| `jiraIntegrationReconnect.connectionHealth.metrics` | `object` | no |
| `jiraIntegrationReconnect.connectionHealth.metrics.connectedSpaces` | `string` | no |
| `jiraIntegrationReconnect.connectionHealth.metrics.lastSync` | `string` | no |
| `jiraIntegrationReconnect.connectionHealth.systemChecks[]` | `object` | no |
| `jiraIntegrationReconnect.connectionHealth.systemChecks[].id` | `string` | no |
| `jiraIntegrationReconnect.connectionHealth.systemChecks[].description` | `string` | no |
| `jiraIntegrationReconnect.connectionHealth.systemChecks[].status` | `JiraSystemCheckStatus` | no |
| `jiraIntegrationReconnect.connectionHealth.systemChecks[].title` | `string` | no |
| `jiraIntegrationReconnect.instanceUrl` | `string` | yes |
| `jiraIntegrationReconnect.jiraAppInstalledComplete` | `boolean` | no |
| `jiraIntegrationReconnect.jiraInstallationId` | `string` | yes |
| `jiraIntegrationReconnect.lastUpdated` | `string` | yes |
| `jiraIntegrationReconnect.oauthInstallStepComplete` | `boolean` | no |
| `jiraIntegrationReconnect.oauthTokenActive` | `boolean` | no |
| `jiraIntegrationReconnect.spacesCount` | `integer` | yes |
| `jiraIntegrationReconnect.status` | `JiraIntegrationStatus` | no |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.mutation_jira_integration_reconnect()
        # Responses are typed Pydantic models: read fields as attributes.
        print(resp.jira_integration_reconnect.status)


if __name__ == "__main__":
    main()
```
