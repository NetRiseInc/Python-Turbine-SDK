<!-- Generated file: do not edit by hand -->

# query_secret

Retrieve detailed information about a specific discovered secret.

## Parameters

| name | type | required |
| --- | --- | --- |
| `secret_args` | `SecretInput` | `true` |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    SecretInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_secret(secret_args=SecretInput(id='id_123'))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
