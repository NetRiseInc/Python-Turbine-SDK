<!-- Generated file: do not edit by hand -->

# query_private_keys

Detect private cryptographic keys stored insecurely on the asset filesystem.

## Parameters

| name | type | required |
| --- | --- | --- |
| `private_keys_args` | `PrivateKeysInput` | `true` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `privateKeys` | `object` | yes |
| `privateKeys.edges[]` | `object` | yes |
| `privateKeys.edges[].cursor` | `string` | no |
| `privateKeys.edges[].node` | `object` | yes |
| `privateKeys.edges[].node.id` | `string` | yes |
| `privateKeys.edges[].node.algorithm` | `string` | yes |
| `privateKeys.edges[].node.algorithmType` | `CryptoAlgorithmType` | yes |
| `privateKeys.edges[].node.bitSize` | `string` | yes |
| `privateKeys.edges[].node.correlations[]` | `object` | yes |
| `privateKeys.edges[].node.correlations[].artifact` | `string` | yes |
| `privateKeys.edges[].node.correlations[].assetId` | `string` | yes |
| `privateKeys.edges[].node.correlations[].assetName` | `string` | yes |
| `privateKeys.edges[].node.correlations[].location` | `string` | yes |
| `privateKeys.edges[].node.correlations[].risk` | `object` | yes |
| `privateKeys.edges[].node.correlations[].risk.category` | `RiskCategory` | yes |
| `privateKeys.edges[].node.correlations[].risk.rawScore` | `float` | yes |
| `privateKeys.edges[].node.correlations[].risk.score` | `float` | yes |
| `privateKeys.edges[].node.correlations[].updatedAt` | `string` | yes |
| `privateKeys.edges[].node.correlationsCount` | `integer` | yes |
| `privateKeys.edges[].node.currentRemediation` | `object` | yes |
| `privateKeys.edges[].node.currentRemediation.author` | `string` | yes |
| `privateKeys.edges[].node.currentRemediation.createdAt` | `string` | yes |
| `privateKeys.edges[].node.currentRemediation.description` | `string` | yes |
| `privateKeys.edges[].node.currentRemediation.errorMessage` | `string` | yes |
| `privateKeys.edges[].node.currentRemediation.privateKey` | `object` | no |
| `privateKeys.edges[].node.currentRemediation.privateKey.filePath` | `string` | no |
| `privateKeys.edges[].node.currentRemediation.privateKey.matchHash` | `string` | no |
| `privateKeys.edges[].node.currentRemediation.status` | `CryptoRemediationStatus` | no |
| `privateKeys.edges[].node.decapsulationKey` | `string` | yes |
| `privateKeys.edges[].node.e` | `string` | yes |
| `privateKeys.edges[].node.effectivePermissions` | `string` | yes |
| `privateKeys.edges[].node.encapsulationKey` | `string` | yes |
| `privateKeys.edges[].node.fileOffset` | `integer` | yes |
| `privateKeys.edges[].node.filePath` | `string` | yes |
| `privateKeys.edges[].node.foundPublicKey` | `boolean` | yes |
| `privateKeys.edges[].node.foundPublicKeyCount` | `integer` | yes |
| `privateKeys.edges[].node.matchHash` | `string` | yes |
| `privateKeys.edges[].node.privateDsaKey` | `string` | yes |
| `privateKeys.edges[].node.publicDsaKey` | `string` | yes |
| `privateKeys.edges[].node.seed` | `string` | yes |
| `privateKeys.edges[].node.uniqueHash` | `string` | yes |
| `privateKeys.pageInfo` | `object` | yes |
| `privateKeys.pageInfo.endCursor` | `string` | yes |
| `privateKeys.pageInfo.hasNextPage` | `boolean` | no |
| `privateKeys.pageInfo.hasPreviousPage` | `boolean` | no |
| `privateKeys.pageInfo.startCursor` | `string` | yes |
| `privateKeys.pageInfo.totalCount` | `integer` | yes |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    Cursor,
    PrivateKeysInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_private_keys(private_keys_args=PrivateKeysInput(asset_id='asset_123', cursor=Cursor()))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
