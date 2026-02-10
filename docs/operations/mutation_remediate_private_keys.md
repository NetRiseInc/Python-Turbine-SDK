<!-- Generated file: do not edit by hand -->

# mutation_remediate_private_keys

Apply remediation status to private key exposures discovered in assets.

## Parameters

| name | type | required |
| --- | --- | --- |
| `remediate_private_keys_args` | `RemediatePrivateKeysInput` | `true` |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    PrivateKeyIdentifierInput,
    RemediatePrivateKeysInput,
)
from netrise_turbine_sdk_graphql.enums import (
    CryptoRemediationStatus,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.mutation_remediate_private_keys(remediate_private_keys_args=RemediatePrivateKeysInput(asset_id='asset_123', private_keys=[PrivateKeyIdentifierInput(file_path=None  # TODO: fill, match_hash=None  # TODO: fill)], status=CryptoRemediationStatus.UNSPECIFIED))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
