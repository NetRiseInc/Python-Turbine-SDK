<!-- Generated file: do not edit by hand -->

# mutation_jira_integration_delete_connected_space

Remove a connected Jira space from the integration.

## Parameters

| name | type | required |
| --- | --- | --- |
| `jira_integration_delete_connected_space_args` | `JiraIntegrationDeleteConnectedSpaceInput` | `true` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `jiraIntegrationDeleteConnectedSpace` | `object` | no |
| `jiraIntegrationDeleteConnectedSpace.error` | `string` | yes |
| `jiraIntegrationDeleteConnectedSpace.success` | `boolean` | no |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    JiraIntegrationDeleteConnectedSpaceInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.mutation_jira_integration_delete_connected_space(jira_integration_delete_connected_space_args=JiraIntegrationDeleteConnectedSpaceInput(space_id='id_123'))
        # Responses are typed Pydantic models: read fields as attributes.
        print(resp.jira_integration_delete_connected_space.error, resp.jira_integration_delete_connected_space.success)


if __name__ == "__main__":
    main()
```
