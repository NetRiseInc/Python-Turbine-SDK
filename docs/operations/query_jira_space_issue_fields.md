<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# query_jira_space_issue_fields

[Back to the index](../README.md)

List creatable fields for a Jira space and issue type.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |
| `jira_space_issue_fields_args` | `JiraSpaceIssueFieldsInput` | `true` |

## Response fields

Typed attributes on the response model.

| Field | Type | Nullable |
| --- | --- | --- |
| `jiraSpaceIssueFields[]` | `object` | no |
| `jiraSpaceIssueFields[].allowedValues[]` | `object` | no |
| `jiraSpaceIssueFields[].allowedValues[].id` | `string` | no |
| `jiraSpaceIssueFields[].allowedValues[].value` | `string` | no |
| `jiraSpaceIssueFields[].itemType` | `string` | no |
| `jiraSpaceIssueFields[].key` | `string` | no |
| `jiraSpaceIssueFields[].name` | `string` | no |
| `jiraSpaceIssueFields[].required` | `boolean` | no |
| `jiraSpaceIssueFields[].schemaCustom` | `string` | yes |
| `jiraSpaceIssueFields[].schemaType` | `string` | no |
| `jiraSpaceIssueFields[].supported` | `boolean` | no |
| `jiraSpaceIssueFields[].unsupportedRequired` | `boolean` | no |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    JiraSpaceIssueFieldsInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_jira_space_issue_fields(jira_space_issue_fields_args=JiraSpaceIssueFieldsInput(space_id='id_123', issue_type_id='issue_123'))
        # Responses are typed Pydantic models: read fields as attributes.
        for item in resp.jira_space_issue_fields or []:
            print(item.name, item.item_type, item.key)


if __name__ == "__main__":
    main()
```
