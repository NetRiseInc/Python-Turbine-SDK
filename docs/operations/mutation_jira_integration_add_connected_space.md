<!-- Generated file: do not edit by hand -->

# mutation_jira_integration_add_connected_space

Add a Jira space to the integration's connected spaces list.

## Parameters

| name | type | required |
| --- | --- | --- |
| `jira_integration_add_connected_space_args` | `JiraIntegrationAddConnectedSpaceInput` | `true` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `jiraIntegrationAddConnectedSpace` | `object` | no |
| `jiraIntegrationAddConnectedSpace.error` | `string` | yes |
| `jiraIntegrationAddConnectedSpace.success` | `boolean` | no |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    JiraIntegrationAddConnectedSpaceInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.mutation_jira_integration_add_connected_space(jira_integration_add_connected_space_args=JiraIntegrationAddConnectedSpaceInput())
        # Responses are typed Pydantic models: read fields as attributes.
        print(resp.jira_integration_add_connected_space.error, resp.jira_integration_add_connected_space.success)


if __name__ == "__main__":
    main()
```
