<!-- Generated file: do not edit by hand -->

# query_notifications

List notification events and alerts for the organization or user.

## Parameters

| name | type | required |
| --- | --- | --- |
| `notifications_args` | `NotificationsInput` | `true` |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    NotificationsInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_notifications(notifications_args=NotificationsInput())
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
