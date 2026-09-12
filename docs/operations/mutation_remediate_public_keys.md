<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# mutation_remediate_public_keys

[Back to the index](../README.md)

Set remediation status on public key findings.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |
| `remediate_public_keys_args` | `RemediatePublicKeysInput` | `true` |

## Response fields

Typed attributes on the response model.

| Field | Type | Nullable |
| --- | --- | --- |
| `remediatePublicKeys[]` | `object` | yes |
| `remediatePublicKeys[].assetId` | `string` | yes |
| `remediatePublicKeys[].author` | `string` | no |
| `remediatePublicKeys[].createdAt` | `string` | no |
| `remediatePublicKeys[].description` | `string` | yes |
| `remediatePublicKeys[].publicKey` | `object` | no |
| `remediatePublicKeys[].publicKey.filePath` | `string` | no |
| `remediatePublicKeys[].publicKey.matchHash` | `string` | no |
| `remediatePublicKeys[].publicKeyId` | `string` | no |
| `remediatePublicKeys[].status` | `CryptoRemediationStatus` | no |

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
        resp = client.mutation_remediate_public_keys(remediate_public_keys_args=RemediatePublicKeysInput(asset_id='asset_123', public_keys=[PublicKeyIdentifierInput(file_path='./path/to/file', match_hash='value')], status=CryptoRemediationStatus.UNSPECIFIED))
        # Responses are typed Pydantic models: read fields as attributes.
        for item in resp.remediate_public_keys or []:
            print(item.status, item.asset_id, item.author)


if __name__ == "__main__":
    main()
```
