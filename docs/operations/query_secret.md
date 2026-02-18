<!-- Generated file: do not edit by hand -->

# query_secret

Retrieve detailed information about a specific discovered secret.

## Parameters

| name | type | required |
| --- | --- | --- |
| `secret_args` | `SecretInput` | `true` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `secret` | `object` | yes |
| `secret.id` | `string` | no |
| `secret.category` | `SecretCategory` | no |
| `secret.categoryLabel` | `string` | yes |
| `secret.correlations[]` | `object` | yes |
| `secret.correlations[].artifact` | `string` | yes |
| `secret.correlations[].assetId` | `string` | yes |
| `secret.correlations[].assetName` | `string` | yes |
| `secret.correlations[].location` | `string` | yes |
| `secret.correlations[].risk` | `object` | yes |
| `secret.correlations[].risk.category` | `RiskCategory` | yes |
| `secret.correlations[].risk.rawScore` | `float` | yes |
| `secret.correlations[].risk.score` | `float` | yes |
| `secret.correlations[].updatedAt` | `string` | yes |
| `secret.correlationsCount` | `integer` | no |
| `secret.currentRemediation` | `object` | yes |
| `secret.currentRemediation.author` | `string` | yes |
| `secret.currentRemediation.createdAt` | `string` | yes |
| `secret.currentRemediation.description` | `string` | yes |
| `secret.currentRemediation.secretId` | `string` | yes |
| `secret.currentRemediation.status` | `SecretRemediationStatus` | yes |
| `secret.description` | `string` | yes |
| `secret.filePath` | `string` | yes |
| `secret.rawSecret` | `string` | yes |
| `secret.remediationStatus` | `SecretRemediationStatus` | yes |
| `secret.sanitizedSecret` | `string` | yes |
| `secret.severity` | `SecretSeverity` | no |
| `secret.subtype` | `string` | yes |
| `secret.type` | `SecretType` | yes |

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
