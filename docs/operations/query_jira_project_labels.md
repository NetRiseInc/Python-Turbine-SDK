<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# query_jira_project_labels

[Back to the index](../README.md)

Search Jira labels for a connected space.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |
| `jira_project_labels_args` | `JiraProjectLabelsInput` | `true` |

## Response fields

Typed attributes on the response model.

| Field | Type | Nullable |
| --- | --- | --- |
| `jiraProjectLabels[]` | `object` | no |
| `jiraProjectLabels[].name` | `string` | no |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    JiraProjectLabelsInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_jira_project_labels(jira_project_labels_args=JiraProjectLabelsInput(space_id='id_123', query='search_term'))
        # Responses are typed Pydantic models: read fields as attributes.
        for item in resp.jira_project_labels or []:
            print(item.name)


if __name__ == "__main__":
    main()
```
