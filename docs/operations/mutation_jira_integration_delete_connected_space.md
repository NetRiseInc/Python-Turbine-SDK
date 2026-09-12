<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# mutation_jira_integration_delete_connected_space

[Back to the index](../README.md)

Disconnect a Jira space from the integration.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |
| `jira_integration_delete_connected_space_args` | `JiraIntegrationDeleteConnectedSpaceInput` | `true` |

## Response fields

Typed attributes on the response model.

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
