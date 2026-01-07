<!-- Generated file: do not edit by hand -->

# query_assets_overview

View high-level risk and threat exposure metrics for multiple assets.

## Parameters

| name | type | required |
| --- | --- | --- |
| `assets_overview_args` | `AssetOverviewInput` | `true` |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    AssetOverviewInput,
    Cursor,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_assets_overview(assets_overview_args=AssetOverviewInput(cursor=Cursor()))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
