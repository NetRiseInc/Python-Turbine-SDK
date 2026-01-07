<!-- Generated file: do not edit by hand -->

# mutation_user_update_user

Modify user profile information including name and contact email details.

## Parameters

| name | type | required |
| --- | --- | --- |
| `user_update_user_args` | `UpdateUserInput` | `true` |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    UpdateUserInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.mutation_user_update_user(user_update_user_args=UpdateUserInput(user_id='user_123'))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
