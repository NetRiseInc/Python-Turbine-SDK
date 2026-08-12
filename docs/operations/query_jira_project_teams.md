<!-- Generated file: do not edit by hand -->

# query_jira_project_teams

Search the Atlassian Teams available for a connected Jira space.

## Parameters

| name | type | required |
| --- | --- | --- |
| `jira_project_teams_args` | `JiraProjectTeamsInput` | `true` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `jiraProjectTeams[]` | `object` | no |
| `jiraProjectTeams[].id` | `string` | no |
| `jiraProjectTeams[].avatarUrl` | `string` | yes |
| `jiraProjectTeams[].displayName` | `string` | no |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    JiraProjectTeamsInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_jira_project_teams(jira_project_teams_args=JiraProjectTeamsInput(space_id='id_123', query='search_term'))
        # Responses are typed Pydantic models: read fields as attributes.
        for item in resp.jira_project_teams or []:
            print(item.id, item.avatar_url, item.display_name)


if __name__ == "__main__":
    main()
```
