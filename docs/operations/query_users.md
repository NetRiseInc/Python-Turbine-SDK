<!-- Generated file: do not edit by hand -->

# query_users

Retrieve a detailed list of all users and their assigned roles.

## Parameters

| name | type | required |
| --- | --- | --- |
| `users_args` | `UsersInput` | `true` |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    Cursor,
    UsersInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_users(users_args=UsersInput(cursor=Cursor()))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
