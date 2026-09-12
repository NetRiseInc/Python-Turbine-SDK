<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# mutation_jira_integration_set_status_mapping_auto_sync

[Back to the index](../README.md)

Enable or disable auto-sync for Jira status mappings.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |
| `jira_integration_set_status_mapping_auto_sync_args` | `JiraIntegrationSetStatusMappingAutoSyncInput` | `true` |

## Response fields

Typed attributes on the response model.

| Field | Type | Nullable |
| --- | --- | --- |
| `jiraIntegrationSetStatusMappingAutoSync` | `object` | no |
| `jiraIntegrationSetStatusMappingAutoSync.error` | `string` | yes |
| `jiraIntegrationSetStatusMappingAutoSync.success` | `boolean` | no |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    JiraIntegrationSetStatusMappingAutoSyncInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.mutation_jira_integration_set_status_mapping_auto_sync(jira_integration_set_status_mapping_auto_sync_args=JiraIntegrationSetStatusMappingAutoSyncInput(enabled=True))
        # Responses are typed Pydantic models: read fields as attributes.
        print(resp.jira_integration_set_status_mapping_auto_sync.error, resp.jira_integration_set_status_mapping_auto_sync.success)


if __name__ == "__main__":
    main()
```
