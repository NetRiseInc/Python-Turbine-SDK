<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# mutation_remediate_secrets

[Back to the index](../README.md)

Set remediation status and justification on secrets.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |
| `remediate_secrets_args` | `CreateSecretsRemediationInput` | `true` |

## Response fields

Typed attributes on the response model.

| Field | Type | Nullable |
| --- | --- | --- |
| `remediateSecrets[]` | `object` | yes |
| `remediateSecrets[].author` | `string` | yes |
| `remediateSecrets[].createdAt` | `string` | yes |
| `remediateSecrets[].description` | `string` | yes |
| `remediateSecrets[].secretId` | `string` | yes |
| `remediateSecrets[].status` | `SecretRemediationStatus` | yes |

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
        resp = client.mutation_remediate_secrets(remediate_secrets_args=CreateSecretsRemediationInput(asset_id='asset_123', secret_ids=['value'], status=SecretRemediationStatus.UNSPECIFIED))
        # Responses are typed Pydantic models: read fields as attributes.
        for item in resp.remediate_secrets or []:
            print(item.status, item.author, item.created_at)


if __name__ == "__main__":
    main()
```
