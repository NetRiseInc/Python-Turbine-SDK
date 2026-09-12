<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# mutation_user_remove

[Back to the index](../README.md)

Remove a user from the org without deleting the account.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |
| `user_remove_args` | `UserInput` | `true` |

## Response fields

Typed attributes on the response model.

| Field | Type | Nullable |
| --- | --- | --- |
| `user` | `object` | yes |
| `user.remove` | `object` | yes |
| `user.remove.err` | `string` | yes |

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
        resp = client.mutation_user_remove(user_remove_args=UserInput(id='id_123'))
        # Responses are typed Pydantic models: read fields as attributes.
        print(resp.user.remove.err)


if __name__ == "__main__":
    main()
```
