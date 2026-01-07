<!-- Generated file: do not edit by hand -->

# query_activity

Retrieve a comprehensive log of actions and events for assets.

## Parameters

| name | type | required |
| --- | --- | --- |
| `activity_args` | `ActivityInput` | `true` |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    ActivityInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_activity(activity_args=ActivityInput(asset_id='asset_123'))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
