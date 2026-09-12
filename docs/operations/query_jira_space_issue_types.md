<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# query_jira_space_issue_types

[Back to the index](../README.md)

List issue types for a connected Jira space.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |
| `jira_space_issue_types_args` | `JiraSpaceIssueTypesInput` | `true` |

## Response fields

Typed attributes on the response model.

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
