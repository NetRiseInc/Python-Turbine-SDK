<!-- Generated file: do not edit by hand -->

# mutation_user_set_user_role

## Parameters

| name | type | required |
| --- | --- | --- |
| `user_set_user_role_args` | `SetUserRoleInput` | `true` |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    SetUserRoleInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.mutation_user_set_user_role(user_set_user_role_args=SetUserRoleInput(next_role='example', user_id='user_123'))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
