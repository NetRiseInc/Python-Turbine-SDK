<!-- Generated file: do not edit by hand -->

# query_public_keys

## Parameters

| name | type | required |
| --- | --- | --- |
| `public_keys_args` | `PublicKeysInput` | `true` |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    Cursor,
    PublicKeysInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_public_keys(public_keys_args=PublicKeysInput(asset_id='asset_123', cursor=Cursor()))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
