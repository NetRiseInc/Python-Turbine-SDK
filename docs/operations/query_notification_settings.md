<!-- Generated file: do not edit by hand -->

# query_notification_settings

Retrieve current notification configuration and alert preferences.

## Parameters

| name | type | required |
| --- | --- | --- |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_notification_settings()
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
