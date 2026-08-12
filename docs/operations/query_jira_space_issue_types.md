<!-- Generated file: do not edit by hand -->

# query_jira_space_issue_types

Retrieve the issue types available for a connected Jira space.

## Parameters

| name | type | required |
| --- | --- | --- |
| `jira_space_issue_types_args` | `JiraSpaceIssueTypesInput` | `true` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `jiraSpaceIssueTypes[]` | `object` | no |
| `jiraSpaceIssueTypes[].id` | `string` | no |
| `jiraSpaceIssueTypes[].iconUrl` | `string` | yes |
| `jiraSpaceIssueTypes[].name` | `string` | no |
| `jiraSpaceIssueTypes[].subtask` | `boolean` | no |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    JiraSpaceIssueTypesInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_jira_space_issue_types(jira_space_issue_types_args=JiraSpaceIssueTypesInput(space_id='id_123'))
        # Responses are typed Pydantic models: read fields as attributes.
        for item in resp.jira_space_issue_types or []:
            print(item.id, item.name, item.icon_url)


if __name__ == "__main__":
    main()
```
