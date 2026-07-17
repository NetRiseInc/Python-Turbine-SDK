<!-- Generated file: do not edit by hand -->

# mutation_remove_org_user

Permanently remove a user from the current organization.

## Parameters

| name | type | required |
| --- | --- | --- |
| `remove_org_user_args` | `RemoveOrgUserInput` | `true` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `removeOrgUser` | `object` | no |
| `removeOrgUser.success` | `boolean` | no |
| `removeOrgUser.userId` | `string` | no |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    RemoveOrgUserInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.mutation_remove_org_user(remove_org_user_args=RemoveOrgUserInput(user_id='user_123'))
        # Responses are typed Pydantic models: read fields as attributes.
        print(resp.remove_org_user.success, resp.remove_org_user.user_id)


if __name__ == "__main__":
    main()
```
