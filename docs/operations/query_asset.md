<!-- Generated file: do not edit by hand -->

# query_asset

Retrieve detailed metadata and risk information for a single asset.

## Parameters

| name | type | required |
| --- | --- | --- |
| `asset_args` | `Union[AssetInput, None, UnsetType]` | `false` |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_asset()
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
