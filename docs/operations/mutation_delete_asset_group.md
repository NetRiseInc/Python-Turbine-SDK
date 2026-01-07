<!-- Generated file: do not edit by hand -->

# mutation_delete_asset_group

Permanently remove an asset group while keeping contained assets intact.

## Parameters

| name | type | required |
| --- | --- | --- |
| `delete_asset_group_args` | `DeleteAssetGroupInput` | `true` |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    DeleteAssetGroupInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.mutation_delete_asset_group(delete_asset_group_args=DeleteAssetGroupInput(id='id_123'))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
