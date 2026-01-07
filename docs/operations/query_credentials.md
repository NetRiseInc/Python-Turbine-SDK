<!-- Generated file: do not edit by hand -->

# query_credentials

Identify user accounts and password hashes discovered within the filesystem.

## Parameters

| name | type | required |
| --- | --- | --- |
| `credentials_args` | `CredentialsInput` | `true` |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    CredentialsInput,
    Cursor,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_credentials(credentials_args=CredentialsInput(asset_id='asset_123', cursor=Cursor()))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
