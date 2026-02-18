<!-- Generated file: do not edit by hand -->

# query_assets_relay

Retrieve a paginated, sortable list of assets with filtering options.

## Parameters

| name | type | required |
| --- | --- | --- |
| `assets_relay_args` | `AssetsRelayInput` | `true` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `assetsRelay` | `object` | yes |
| `assetsRelay.edges[]` | `object` | yes |
| `assetsRelay.edges[].cursor` | `string` | yes |
| `assetsRelay.edges[].node` | `object` | yes |
| `assetsRelay.edges[].node.id` | `string` | yes |
| `assetsRelay.edges[].node.analytic` | `object` | yes |
| `assetsRelay.edges[].node.analytic.binaries` | `integer` | no |
| `assetsRelay.edges[].node.analytic.components` | `object` | no |
| `assetsRelay.edges[].node.analytic.components.application` | `integer` | no |
| `assetsRelay.edges[].node.analytic.components.container` | `integer` | no |
| `assetsRelay.edges[].node.analytic.components.device` | `integer` | no |
| `assetsRelay.edges[].node.analytic.components.framework` | `integer` | no |
| `assetsRelay.edges[].node.analytic.components.kernel` | `integer` | no |
| `assetsRelay.edges[].node.analytic.components.kernelModule` | `integer` | no |
| `assetsRelay.edges[].node.analytic.components.library` | `integer` | no |
| `assetsRelay.edges[].node.analytic.components.os` | `integer` | no |
| `assetsRelay.edges[].node.analytic.components.package` | `integer` | no |
| `assetsRelay.edges[].node.analytic.credentials` | `object` | no |
| `assetsRelay.edges[].node.analytic.credentials.crackedCred` | `integer` | yes |
| `assetsRelay.edges[].node.analytic.credentials.crackedHash` | `integer` | yes |
| `assetsRelay.edges[].node.analytic.credentials.credential` | `integer` | no |
| `assetsRelay.edges[].node.analytic.credentials.hash` | `integer` | no |
| `assetsRelay.edges[].node.analytic.credentials.secrets` | `integer` | yes |
| `assetsRelay.edges[].node.analytic.cryptography` | `object` | no |
| `assetsRelay.edges[].node.analytic.cryptography.certificate` | `integer` | no |
| `assetsRelay.edges[].node.analytic.cryptography.privateKey` | `integer` | no |
| `assetsRelay.edges[].node.analytic.cryptography.publicKey` | `integer` | no |
| `assetsRelay.edges[].node.analytic.exploit` | `object` | no |
| `assetsRelay.edges[].node.analytic.exploit.botnet` | `integer` | no |
| `assetsRelay.edges[].node.analytic.exploit.exploitCode` | `integer` | yes |
| `assetsRelay.edges[].node.analytic.exploit.inKnownExploitedVulnerabilities` | `integer` | yes |
| `assetsRelay.edges[].node.analytic.exploit.inTheWild` | `integer` | no |
| `assetsRelay.edges[].node.analytic.exploit.knownAttacks` | `integer` | no |
| `assetsRelay.edges[].node.analytic.exploit.ransomware` | `integer` | no |
| `assetsRelay.edges[].node.analytic.exploit.threatActor` | `integer` | no |
| `assetsRelay.edges[].node.analytic.files` | `integer` | no |
| `assetsRelay.edges[].node.analytic.licenseIssues` | `integer` | no |
| `assetsRelay.edges[].node.analytic.misconfigurations` | `object` | no |
| `assetsRelay.edges[].node.analytic.misconfigurations.failed` | `integer` | no |
| `assetsRelay.edges[].node.analytic.misconfigurations.notApplicable` | `integer` | no |
| `assetsRelay.edges[].node.analytic.misconfigurations.passed` | `integer` | no |
| `assetsRelay.edges[].node.analytic.vulnerability` | `object` | no |
| `assetsRelay.edges[].node.analytic.vulnerability.critical` | `integer` | no |
| `assetsRelay.edges[].node.analytic.vulnerability.high` | `integer` | no |
| `assetsRelay.edges[].node.analytic.vulnerability.low` | `integer` | no |
| `assetsRelay.edges[].node.analytic.vulnerability.medium` | `integer` | no |
| `assetsRelay.edges[].node.assetCpe` | `string` | yes |
| `assetsRelay.edges[].node.assetGroupCount` | `integer` | yes |
| `assetsRelay.edges[].node.assetGroupIds[]` | `string` | yes |
| `assetsRelay.edges[].node.createdAt` | `string` | yes |
| `assetsRelay.edges[].node.fileName` | `string` | yes |
| `assetsRelay.edges[].node.filesystems[]` | `object` | yes |
| `assetsRelay.edges[].node.filesystems[].id` | `string` | no |
| `assetsRelay.edges[].node.firstAnalysisTime` | `string` | yes |
| `assetsRelay.edges[].node.hasRemediation` | `boolean` | yes |
| `assetsRelay.edges[].node.name` | `string` | yes |
| `assetsRelay.edges[].node.orgId` | `string` | yes |
| `assetsRelay.edges[].node.product` | `string` | yes |
| `assetsRelay.edges[].node.quantumCapable` | `boolean` | yes |
| `assetsRelay.edges[].node.risk` | `object` | yes |
| `assetsRelay.edges[].node.risk.category` | `RiskCategory` | yes |
| `assetsRelay.edges[].node.risk.rawScore` | `float` | yes |
| `assetsRelay.edges[].node.risk.score` | `float` | yes |
| `assetsRelay.edges[].node.sha256` | `string` | yes |
| `assetsRelay.edges[].node.sizeBytes` | `integer` | yes |
| `assetsRelay.edges[].node.status` | `ProcessingStatus` | yes |
| `assetsRelay.edges[].node.type` | `AssetType` | yes |
| `assetsRelay.edges[].node.updatedAt` | `string` | yes |
| `assetsRelay.edges[].node.uploadedBy` | `string` | yes |
| `assetsRelay.edges[].node.vendor` | `string` | yes |
| `assetsRelay.edges[].node.version` | `string` | yes |
| `assetsRelay.pageInfo` | `object` | no |
| `assetsRelay.pageInfo.endCursor` | `string` | yes |
| `assetsRelay.pageInfo.hasNextPage` | `boolean` | no |
| `assetsRelay.pageInfo.hasPreviousPage` | `boolean` | no |
| `assetsRelay.pageInfo.startCursor` | `string` | yes |
| `assetsRelay.pageInfo.totalCount` | `integer` | yes |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    AssetsRelayInput,
    Cursor,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_assets_relay(assets_relay_args=AssetsRelayInput(cursor=Cursor()))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
