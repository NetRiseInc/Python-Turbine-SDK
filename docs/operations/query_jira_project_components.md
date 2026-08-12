<!-- Generated file: do not edit by hand -->

# query_jira_project_components

List the Jira project components available for a connected space.

## Parameters

| name | type | required |
| --- | --- | --- |
| `jira_project_components_args` | `JiraProjectComponentsInput` | `true` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `jiraProjectComponents[]` | `object` | no |
| `jiraProjectComponents[].id` | `string` | no |
| `jiraProjectComponents[].description` | `string` | yes |
| `jiraProjectComponents[].name` | `string` | no |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    JiraProjectComponentsInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_jira_project_components(jira_project_components_args=JiraProjectComponentsInput(space_id='id_123'))
        # Responses are typed Pydantic models: read fields as attributes.
        for item in resp.jira_project_components or []:
            print(item.id, item.name, item.description)


if __name__ == "__main__":
    main()
```
