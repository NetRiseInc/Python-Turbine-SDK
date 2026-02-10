<!-- Generated file: do not edit by hand -->

# query_secret_types_and_count

List secret types discovered with their occurrence counts.

## Parameters

| name | type | required |
| --- | --- | --- |
| `secret_types_and_count_args` | `SecretTypesAndCountInput` | `true` |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    SecretTypesAndCountInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_secret_types_and_count(secret_types_and_count_args=SecretTypesAndCountInput(asset_id='asset_123'))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
