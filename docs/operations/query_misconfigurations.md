<!-- Generated file: do not edit by hand -->

# query_misconfigurations

## Parameters

| name | type | required |
| --- | --- | --- |
| `misconfigurations_args` | `MisconfigurationsInput` | `true` |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    Cursor,
    MisconfigurationsInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_misconfigurations(misconfigurations_args=MisconfigurationsInput(asset_id='asset_123', cursor=Cursor()))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
