<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# query_jira_project_users

[Back to the index](../README.md)

Search assignable Jira users for a connected space.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |
| `jira_project_users_args` | `JiraProjectUsersInput` | `true` |

## Response fields

Typed attributes on the response model.

| Field | Type | Nullable |
| --- | --- | --- |
| `jiraProjectUsers[]` | `object` | no |
| `jiraProjectUsers[].accountId` | `string` | no |
| `jiraProjectUsers[].active` | `boolean` | no |
| `jiraProjectUsers[].avatarUrl` | `string` | yes |
| `jiraProjectUsers[].displayName` | `string` | no |
| `jiraProjectUsers[].emailAddress` | `string` | yes |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    JiraProjectUsersInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_jira_project_users(jira_project_users_args=JiraProjectUsersInput(space_id='id_123', query='search_term'))
        # Responses are typed Pydantic models: read fields as attributes.
        for item in resp.jira_project_users or []:
            print(item.account_id, item.active, item.avatar_url)


if __name__ == "__main__":
    main()
```
