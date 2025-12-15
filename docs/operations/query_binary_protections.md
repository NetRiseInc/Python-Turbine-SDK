<!-- Generated file: do not edit by hand -->

# query_binary_protections

## Parameters

| name | type | required |
| --- | --- | --- |
| `binary_protections_args` | `BinaryProtectionsInput` | `true` |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    BinaryProtectionsInput,
    Cursor,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_binary_protections(binary_protections_args=BinaryProtectionsInput(asset_id='asset_123', cursor=Cursor()))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
