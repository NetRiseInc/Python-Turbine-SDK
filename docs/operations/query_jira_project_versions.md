<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# query_jira_project_versions

[Back to the index](../README.md)

List Jira project versions for a connected space.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |
| `jira_project_versions_args` | `JiraProjectVersionsInput` | `true` |

## Response fields

Typed attributes on the response model.

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
