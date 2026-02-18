<!-- Generated file: do not edit by hand -->

# mutation_remediate_certificates

Update remediation status and notes for certificate issues found in assets.

## Parameters

| name | type | required |
| --- | --- | --- |
| `remediate_certificates_args` | `RemediateCertificatesInput` | `true` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `remediateCertificates[]` | `object` | yes |
| `remediateCertificates[].author` | `string` | yes |
| `remediateCertificates[].certificate` | `object` | no |
| `remediateCertificates[].certificate.filePath` | `string` | no |
| `remediateCertificates[].certificate.sha256` | `string` | no |
| `remediateCertificates[].createdAt` | `string` | yes |
| `remediateCertificates[].description` | `string` | yes |
| `remediateCertificates[].errorMessage` | `string` | yes |
| `remediateCertificates[].status` | `CryptoRemediationStatus` | no |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    RemediateCertificatesInput,
)
from netrise_turbine_sdk_graphql.enums import (
    CryptoRemediationStatus,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.mutation_remediate_certificates(remediate_certificates_args=RemediateCertificatesInput(asset_id='asset_123', certificates=[None], status=CryptoRemediationStatus.UNSPECIFIED))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
