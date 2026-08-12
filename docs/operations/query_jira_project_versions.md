<!-- Generated file: do not edit by hand -->

# query_jira_project_versions

List the Jira project versions available for a connected space.

## Parameters

| name | type | required |
| --- | --- | --- |
| `jira_project_versions_args` | `JiraProjectVersionsInput` | `true` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `jiraProjectVersions[]` | `object` | no |
| `jiraProjectVersions[].id` | `string` | no |
| `jiraProjectVersions[].archived` | `boolean` | no |
| `jiraProjectVersions[].description` | `string` | yes |
| `jiraProjectVersions[].name` | `string` | no |
| `jiraProjectVersions[].releaseDate` | `string` | yes |
| `jiraProjectVersions[].released` | `boolean` | no |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    JiraProjectVersionsInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_jira_project_versions(jira_project_versions_args=JiraProjectVersionsInput(space_id='id_123'))
        # Responses are typed Pydantic models: read fields as attributes.
        for item in resp.jira_project_versions or []:
            print(item.id, item.name, item.archived)


if __name__ == "__main__":
    main()
```
