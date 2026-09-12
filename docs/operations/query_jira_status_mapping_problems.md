<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# query_jira_status_mapping_problems

[Back to the index](../README.md)

List status-mapping problems across connected Jira spaces.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |
| `jira_status_mapping_problems_args` | `Union[JiraStatusMappingProblemsInput, None, UnsetType]` | `false` |

## Response fields

Typed attributes on the response model.

| Field | Type | Nullable |
| --- | --- | --- |
| `jiraStatusMappingProblems[]` | `object` | no |
| `jiraStatusMappingProblems[].jiraSpaceId` | `string` | no |
| `jiraStatusMappingProblems[].mappingProblems[]` | `object` | no |
| `jiraStatusMappingProblems[].mappingProblems[].code` | `string` | no |
| `jiraStatusMappingProblems[].mappingProblems[].detail` | `string` | yes |
| `jiraStatusMappingProblems[].mappingProblems[].detectedAt` | `string` | yes |
| `jiraStatusMappingProblems[].mappingProblems[].jiraIssueTypeId` | `string` | yes |
| `jiraStatusMappingProblems[].mappingProblems[].jiraIssueTypeName` | `string` | yes |
| `jiraStatusMappingProblems[].mappingProblems[].jiraIssueTypeSubtask` | `boolean` | no |
| `jiraStatusMappingProblems[].mappingProblems[].jiraStatusId` | `string` | yes |
| `jiraStatusMappingProblems[].mappingProblems[].jiraStatusMappingId` | `string` | yes |
| `jiraStatusMappingProblems[].mappingProblems[].jiraStatusName` | `string` | yes |
| `jiraStatusMappingProblems[].projectKey` | `string` | no |
| `jiraStatusMappingProblems[].projectName` | `string` | no |
| `jiraStatusMappingProblems[].spaceProblems[]` | `object` | no |
| `jiraStatusMappingProblems[].spaceProblems[].code` | `string` | no |
| `jiraStatusMappingProblems[].spaceProblems[].detail` | `string` | yes |
| `jiraStatusMappingProblems[].spaceProblems[].detectedAt` | `string` | yes |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    JiraStatusMappingProblemsInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_jira_status_mapping_problems(jira_status_mapping_problems_args=JiraStatusMappingProblemsInput())
        # Responses are typed Pydantic models: read fields as attributes.
        for item in resp.jira_status_mapping_problems or []:
            print(item.jira_space_id, item.project_key, item.project_name)


if __name__ == "__main__":
    main()
```
