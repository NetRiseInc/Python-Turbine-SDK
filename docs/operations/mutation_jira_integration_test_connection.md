<!-- Generated file: do not edit by hand -->

# mutation_jira_integration_test_connection

Verify that the Jira integration connection is healthy.

## Parameters

| name | type | required |
| --- | --- | --- |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `jiraIntegrationTestConnection` | `object` | no |
| `jiraIntegrationTestConnection.error` | `string` | yes |
| `jiraIntegrationTestConnection.success` | `boolean` | no |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.mutation_jira_integration_test_connection()
        # Responses are typed Pydantic models: read fields as attributes.
        print(resp.jira_integration_test_connection.error, resp.jira_integration_test_connection.success)


if __name__ == "__main__":
    main()
```
