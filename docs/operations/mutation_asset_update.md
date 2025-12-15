<!-- Generated file: do not edit by hand -->

# mutation_asset_update

## Parameters

| name | type | required |
| --- | --- | --- |
| `asset_update_args` | `Union[UpdateAssetInput, None, UnsetType]` | `false` |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.mutation_asset_update()
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
