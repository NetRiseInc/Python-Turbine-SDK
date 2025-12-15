<!-- Generated file: do not edit by hand -->

# mutation_user_action

## Parameters

| name | type | required |
| --- | --- | --- |
| `user_action_args` | `UserActionInput` | `true` |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    UserActionInput,
)
from netrise_turbine_sdk_graphql.enums import (
    UserActionEnum,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.mutation_user_action(user_action_args=UserActionInput(type=UserActionEnum.DISABLE, user_id='user_123'))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
