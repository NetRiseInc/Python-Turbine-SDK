<!-- Generated file: do not edit by hand -->

# mutation_remediate_public_keys

Update remediation status for public key issues identified in assets.

## Parameters

| name | type | required |
| --- | --- | --- |
| `remediate_public_keys_args` | `RemediatePublicKeysInput` | `true` |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    PublicKeyIdentifierInput,
    RemediatePublicKeysInput,
)
from netrise_turbine_sdk_graphql.enums import (
    CryptoRemediationStatus,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.mutation_remediate_public_keys(remediate_public_keys_args=RemediatePublicKeysInput(asset_id='asset_123', public_keys=[PublicKeyIdentifierInput(file_path=None  # TODO: fill, match_hash=None  # TODO: fill)], status=CryptoRemediationStatus.UNSPECIFIED))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
