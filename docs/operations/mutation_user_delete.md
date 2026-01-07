<!-- Generated file: do not edit by hand -->

# mutation_user_delete

Permanently delete a user account and remove their access rights.

## Parameters

| name | type | required |
| --- | --- | --- |
| `user_delete_args` | `UserInput` | `true` |

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
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
