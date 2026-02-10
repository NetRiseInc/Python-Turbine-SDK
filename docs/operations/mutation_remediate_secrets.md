<!-- Generated file: do not edit by hand -->

# mutation_remediate_secrets

Apply remediation status and justification to exposed secrets in assets.

## Parameters

| name | type | required |
| --- | --- | --- |
| `remediate_secrets_args` | `CreateSecretsRemediationInput` | `true` |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    CreateSecretsRemediationInput,
)
from netrise_turbine_sdk_graphql.enums import (
    SecretRemediationStatus,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.mutation_remediate_secrets(remediate_secrets_args=CreateSecretsRemediationInput(asset_id='asset_123', secret_ids=['example'], status=SecretRemediationStatus.UNSPECIFIED))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
