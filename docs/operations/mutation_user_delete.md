<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# mutation_user_delete

[Back to the index](../README.md)

Delete a user account and revoke access.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |
| `user_delete_args` | `UserInput` | `true` |

## Response fields

Typed attributes on the response model.

| Field | Type | Nullable |
| --- | --- | --- |
| `user` | `object` | yes |
| `user.delete` | `object` | yes |
| `user.delete.err` | `string` | yes |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    UserInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.mutation_user_delete(user_delete_args=UserInput(id='id_123'))
        # Responses are typed Pydantic models: read fields as attributes.
        print(resp.user.delete.err)


if __name__ == "__main__":
    main()
```
