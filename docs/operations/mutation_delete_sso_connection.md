<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# mutation_delete_sso_connection

[Back to the index](../README.md)

Delete the SSO connection and its group mappings.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |
| `delete_sso_connection_args` | `DeleteSsoConnectionInput` | `true` |

## Response fields

Typed attributes on the response model.

| Field | Type | Nullable |
| --- | --- | --- |
| `deleteSsoConnection` | `object` | no |
| `deleteSsoConnection.success` | `boolean` | no |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    DeleteSsoConnectionInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.mutation_delete_sso_connection(delete_sso_connection_args=DeleteSsoConnectionInput())
        # Responses are typed Pydantic models: read fields as attributes.
        print(resp.delete_sso_connection.success)


if __name__ == "__main__":
    main()
```
