<!-- Generated file: do not edit by hand -->

# mutation_user_invite

Invite a new user to the organization with a specific role.

## Parameters

| name | type | required |
| --- | --- | --- |
| `user_invite_args` | `InviteUserInput` | `true` |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    InviteUserInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.mutation_user_invite(user_invite_args=InviteUserInput(email='user@example.com', role='example'))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
