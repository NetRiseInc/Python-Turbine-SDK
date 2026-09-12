<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# query_jira_space_workflow_config

[Back to the index](../README.md)

Get status mappings and workflow config for a Jira space.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |
| `jira_space_workflow_config_args` | `JiraSpaceWorkflowConfigInput` | `true` |

## Response fields

Typed attributes on the response model.

| Field | Type | Nullable |
| --- | --- | --- |
| `jiraSpaceWorkflowConfig` | `object` | no |
| `jiraSpaceWorkflowConfig.issueTypeId` | `string` | no |
| `jiraSpaceWorkflowConfig.jiraStatuses[]` | `object` | no |
| `jiraSpaceWorkflowConfig.jiraStatuses[].id` | `string` | no |
| `jiraSpaceWorkflowConfig.jiraStatuses[].category` | `JiraStatusCategory` | no |
| `jiraSpaceWorkflowConfig.jiraStatuses[].name` | `string` | no |
| `jiraSpaceWorkflowConfig.mappings[]` | `object` | no |
| `jiraSpaceWorkflowConfig.mappings[].jiraStatusId` | `string` | no |
| `jiraSpaceWorkflowConfig.mappings[].netriseStatusId` | `string` | no |
| `jiraSpaceWorkflowConfig.netriseStatuses[]` | `VexStatus` | no |
| `jiraSpaceWorkflowConfig.resolutionStatusIds[]` | `string` | no |
| `jiraSpaceWorkflowConfig.spaceId` | `string` | no |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    JiraSpaceWorkflowConfigInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_jira_space_workflow_config(jira_space_workflow_config_args=JiraSpaceWorkflowConfigInput(space_id='id_123', issue_type_id='issue_123'))
        # Responses are typed Pydantic models: read fields as attributes.
        for item in resp.jira_space_workflow_config.jira_statuses or []:
            print(item.id, item.name, item.category)


if __name__ == "__main__":
    main()
```
