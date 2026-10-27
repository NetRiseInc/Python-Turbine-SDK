<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# mutation_start_sso_connection_test

[Back to the index](../README.md)

Start an SSO login test and get the URL to open.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |
| `start_sso_connection_test_args` | `StartSsoConnectionTestInput` | `true` |

## Response fields

Typed attributes on the response model.

| Field | Type | Nullable |
| --- | --- | --- |
| `startSsoConnectionTest` | `object` | no |
| `startSsoConnectionTest.authorizeUrl` | `string` | no |
| `startSsoConnectionTest.expiresAt` | `string` | yes |
| `startSsoConnectionTest.testId` | `string` | no |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    StartSsoConnectionTestInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.mutation_start_sso_connection_test(start_sso_connection_test_args=StartSsoConnectionTestInput())
        # Responses are typed Pydantic models: read fields as attributes.
        print(resp.start_sso_connection_test.authorize_url, resp.start_sso_connection_test.expires_at)


if __name__ == "__main__":
    main()
```
