<!-- Generated file: do not edit by hand -->

# query_secrets

List all secrets and sensitive data discovered within an asset.

## Parameters

| name | type | required |
| --- | --- | --- |
| `secrets_args` | `SecretsInput` | `true` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `secrets` | `object` | yes |
| `secrets.edges[]` | `object` | yes |
| `secrets.edges[].cursor` | `string` | yes |
| `secrets.edges[].node` | `object` | yes |
| `secrets.edges[].node.id` | `string` | no |
| `secrets.edges[].node.category` | `SecretCategory` | no |
| `secrets.edges[].node.categoryLabel` | `string` | yes |
| `secrets.edges[].node.correlations[]` | `object` | yes |
| `secrets.edges[].node.correlations[].artifact` | `string` | yes |
| `secrets.edges[].node.correlations[].assetId` | `string` | yes |
| `secrets.edges[].node.correlations[].assetName` | `string` | yes |
| `secrets.edges[].node.correlations[].location` | `string` | yes |
| `secrets.edges[].node.correlations[].risk` | `object` | yes |
| `secrets.edges[].node.correlations[].risk.category` | `RiskCategory` | yes |
| `secrets.edges[].node.correlations[].risk.rawScore` | `float` | yes |
| `secrets.edges[].node.correlations[].risk.score` | `float` | yes |
| `secrets.edges[].node.correlations[].updatedAt` | `string` | yes |
| `secrets.edges[].node.correlationsCount` | `integer` | no |
| `secrets.edges[].node.currentRemediation` | `object` | yes |
| `secrets.edges[].node.currentRemediation.author` | `string` | yes |
| `secrets.edges[].node.currentRemediation.createdAt` | `string` | yes |
| `secrets.edges[].node.currentRemediation.description` | `string` | yes |
| `secrets.edges[].node.currentRemediation.secretId` | `string` | yes |
| `secrets.edges[].node.currentRemediation.status` | `SecretRemediationStatus` | yes |
| `secrets.edges[].node.description` | `string` | yes |
| `secrets.edges[].node.filePath` | `string` | yes |
| `secrets.edges[].node.rawSecret` | `string` | yes |
| `secrets.edges[].node.remediationStatus` | `SecretRemediationStatus` | yes |
| `secrets.edges[].node.sanitizedSecret` | `string` | yes |
| `secrets.edges[].node.severity` | `SecretSeverity` | no |
| `secrets.edges[].node.subtype` | `string` | yes |
| `secrets.edges[].node.type` | `SecretType` | yes |
| `secrets.pageInfo` | `object` | no |
| `secrets.pageInfo.endCursor` | `string` | yes |
| `secrets.pageInfo.hasNextPage` | `boolean` | no |
| `secrets.pageInfo.hasPreviousPage` | `boolean` | no |
| `secrets.pageInfo.startCursor` | `string` | yes |
| `secrets.pageInfo.totalCount` | `integer` | yes |

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
