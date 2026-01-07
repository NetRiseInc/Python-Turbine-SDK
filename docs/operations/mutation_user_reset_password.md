<!-- Generated file: do not edit by hand -->

# mutation_user_reset_password

Trigger a password reset email for a specific user account.

## Parameters

| name | type | required |
| --- | --- | --- |
| `user_reset_password_args` | `UserInput` | `true` |

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
        resp = client.mutation_user_reset_password(user_reset_password_args=UserInput(id='id_123'))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
