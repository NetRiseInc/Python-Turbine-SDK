<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# mutation_save_jira_space_workflow_config

[Back to the index](../README.md)

Save status mappings and workflow config for a Jira space.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |
| `save_jira_space_workflow_config_args` | `SaveJiraSpaceWorkflowConfigInput` | `true` |

## Response fields

Typed attributes on the response model.

| Field | Type | Nullable |
| --- | --- | --- |
| `saveJiraSpaceWorkflowConfig` | `object` | no |
| `saveJiraSpaceWorkflowConfig.error` | `string` | yes |
| `saveJiraSpaceWorkflowConfig.success` | `boolean` | no |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    JiraStatusMappingInput,
    SaveJiraSpaceWorkflowConfigInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.mutation_save_jira_space_workflow_config(save_jira_space_workflow_config_args=SaveJiraSpaceWorkflowConfigInput(space_id='id_123', issue_type_id='issue_123', mappings=[JiraStatusMappingInput(jira_status_id='id_123')], resolution_status_ids=['value']))
        # Responses are typed Pydantic models: read fields as attributes.
        print(resp.save_jira_space_workflow_config.error, resp.save_jira_space_workflow_config.success)


if __name__ == "__main__":
    main()
```
