<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# mutation_jira_integration_create_issue

[Back to the index](../README.md)

Create a Jira issue, optionally linked to a finding.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |
| `jira_integration_create_issue_args` | `JiraIntegrationCreateIssueInput` | `true` |

## Response fields

Typed attributes on the response model.

| Field | Type | Nullable |
| --- | --- | --- |
| `jiraIntegrationCreateIssue` | `object` | no |
| `jiraIntegrationCreateIssue.error` | `string` | yes |
| `jiraIntegrationCreateIssue.success` | `boolean` | no |
| `jiraIntegrationCreateIssue.ticket` | `object` | yes |
| `jiraIntegrationCreateIssue.ticket.id` | `string` | no |
| `jiraIntegrationCreateIssue.ticket.assignee` | `string` | yes |
| `jiraIntegrationCreateIssue.ticket.assigneeAvatarUrl` | `string` | yes |
| `jiraIntegrationCreateIssue.ticket.issueType` | `string` | yes |
| `jiraIntegrationCreateIssue.ticket.issueTypeIconUrl` | `string` | yes |
| `jiraIntegrationCreateIssue.ticket.projectId` | `string` | no |
| `jiraIntegrationCreateIssue.ticket.spaceName` | `string` | no |
| `jiraIntegrationCreateIssue.ticket.status` | `string` | no |
| `jiraIntegrationCreateIssue.ticket.statusCategory` | `string` | yes |
| `jiraIntegrationCreateIssue.ticket.statusCategoryColor` | `string` | yes |
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
