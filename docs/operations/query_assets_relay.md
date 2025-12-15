<!-- Generated file: do not edit by hand -->

# query_assets_relay

## Parameters

| name | type | required |
| --- | --- | --- |
| `assets_relay_args` | `AssetsRelayInput` | `true` |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    AssetsRelayInput,
    Cursor,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_assets_relay(assets_relay_args=AssetsRelayInput(cursor=Cursor()))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
