<!-- Generated file: do not edit by hand -->

# query_public_keys

List public cryptographic keys found within the asset's file system.

## Parameters

| name | type | required |
| --- | --- | --- |
| `public_keys_args` | `PublicKeysInput` | `true` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `publicKeys` | `object` | yes |
| `publicKeys.edges[]` | `object` | yes |
| `publicKeys.edges[].cursor` | `string` | no |
| `publicKeys.edges[].node` | `object` | yes |
| `publicKeys.edges[].node.algorithm` | `string` | yes |
| `publicKeys.edges[].node.algorithmType` | `CryptoAlgorithmType` | yes |
| `publicKeys.edges[].node.bitSize` | `string` | yes |
| `publicKeys.edges[].node.correlations[]` | `object` | yes |
| `publicKeys.edges[].node.correlations[].artifact` | `string` | yes |
| `publicKeys.edges[].node.correlations[].assetId` | `string` | yes |
| `publicKeys.edges[].node.correlations[].assetName` | `string` | yes |
| `publicKeys.edges[].node.correlations[].location` | `string` | yes |
| `publicKeys.edges[].node.correlations[].risk` | `object` | yes |
| `publicKeys.edges[].node.correlations[].risk.category` | `RiskCategory` | yes |
| `publicKeys.edges[].node.correlations[].risk.rawScore` | `float` | yes |
| `publicKeys.edges[].node.correlations[].risk.score` | `float` | yes |
| `publicKeys.edges[].node.correlations[].updatedAt` | `string` | yes |
| `publicKeys.edges[].node.correlationsCount` | `integer` | yes |
| `publicKeys.edges[].node.currentRemediation` | `object` | yes |
| `publicKeys.edges[].node.currentRemediation.assetId` | `string` | yes |
| `publicKeys.edges[].node.currentRemediation.author` | `string` | no |
| `publicKeys.edges[].node.currentRemediation.createdAt` | `string` | no |
| `publicKeys.edges[].node.currentRemediation.description` | `string` | yes |
| `publicKeys.edges[].node.currentRemediation.publicKey` | `object` | no |
| `publicKeys.edges[].node.currentRemediation.publicKey.filePath` | `string` | no |
| `publicKeys.edges[].node.currentRemediation.publicKey.matchHash` | `string` | no |
| `publicKeys.edges[].node.currentRemediation.publicKeyId` | `string` | no |
| `publicKeys.edges[].node.currentRemediation.status` | `CryptoRemediationStatus` | no |
| `publicKeys.edges[].node.e` | `string` | yes |
| `publicKeys.edges[].node.effectivePermissions` | `string` | yes |
| `publicKeys.edges[].node.fileOffset` | `integer` | yes |
| `publicKeys.edges[].node.filePath` | `string` | yes |
| `publicKeys.edges[].node.foundPrivateKey` | `boolean` | yes |
| `publicKeys.edges[].node.foundPrivateKeyCount` | `integer` | yes |
| `publicKeys.edges[].node.matchHash` | `string` | yes |
| `publicKeys.edges[].node.uniqueHash` | `string` | yes |
| `publicKeys.pageInfo` | `object` | yes |
| `publicKeys.pageInfo.endCursor` | `string` | yes |
| `publicKeys.pageInfo.hasNextPage` | `boolean` | no |
| `publicKeys.pageInfo.hasPreviousPage` | `boolean` | no |
| `publicKeys.pageInfo.startCursor` | `string` | yes |
| `publicKeys.pageInfo.totalCount` | `integer` | yes |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    Cursor,
    PublicKeysInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_public_keys(public_keys_args=PublicKeysInput(asset_id='asset_123', cursor=Cursor()))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
