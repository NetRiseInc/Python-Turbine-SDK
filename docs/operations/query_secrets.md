<!-- Generated file: do not edit by hand -->

# query_secrets

List all secrets and sensitive data discovered within an asset.

## Parameters

| name | type | required |
| --- | --- | --- |
| `secrets_args` | `SecretsInput` | `true` |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    Cursor,
    SecretsInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_secrets(secrets_args=SecretsInput(asset_id='asset_123', cursor=Cursor()))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
