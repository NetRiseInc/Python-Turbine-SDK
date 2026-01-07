<!-- Generated file: do not edit by hand -->

# mutation_user_remove

Remove a user from the organization without deleting their account.

## Parameters

| name | type | required |
| --- | --- | --- |
| `user_remove_args` | `UserInput` | `true` |

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
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
