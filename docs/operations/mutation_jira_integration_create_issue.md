<!-- Generated file: do not edit by hand -->

# mutation_jira_integration_create_issue

Create a Jira issue and optionally link it to a vulnerability finding.

## Parameters

| name | type | required |
| --- | --- | --- |
| `jira_integration_create_issue_args` | `JiraIntegrationCreateIssueInput` | `true` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `jiraIntegrationCreateIssue` | `object` | no |
| `jiraIntegrationCreateIssue.error` | `string` | yes |
| `jiraIntegrationCreateIssue.success` | `boolean` | no |
| `jiraIntegrationCreateIssue.ticket` | `object` | yes |
| `jiraIntegrationCreateIssue.ticket.id` | `string` | no |
| `jiraIntegrationCreateIssue.ticket.assignee` | `string` | yes |
| `jiraIntegrationCreateIssue.ticket.projectId` | `string` | no |
| `jiraIntegrationCreateIssue.ticket.status` | `string` | no |
| `jiraIntegrationCreateIssue.ticket.ticketKey` | `string` | no |
| `jiraIntegrationCreateIssue.ticket.updatedAt` | `string` | no |
| `jiraIntegrationCreateIssue.ticket.url` | `string` | no |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    JiraIntegrationCreateIssueInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.mutation_jira_integration_create_issue(jira_integration_create_issue_args=JiraIntegrationCreateIssueInput(space_id='id_123', issue_type_id='issue_123', summary='value', description='value'))
        # Responses are typed Pydantic models: read fields as attributes.
        print(resp.jira_integration_create_issue.ticket.id, resp.jira_integration_create_issue.ticket.status)


if __name__ == "__main__":
    main()
```
