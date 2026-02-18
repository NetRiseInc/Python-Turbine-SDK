<!-- Generated file: do not edit by hand -->

# mutation_asset_update

Modify metadata such as name, vendor, or version for assets.

## Parameters

| name | type | required |
| --- | --- | --- |
| `asset_update_args` | `Union[UpdateAssetInput, None, UnsetType]` | `false` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `asset` | `object` | yes |
| `asset.update` | `object` | yes |
| `asset.update.id` | `string` | yes |
| `asset.update.analytic` | `object` | yes |
| `asset.update.analytic.binaries` | `integer` | no |
| `asset.update.analytic.components` | `object` | no |
| `asset.update.analytic.components.application` | `integer` | no |
| `asset.update.analytic.components.container` | `integer` | no |
| `asset.update.analytic.components.device` | `integer` | no |
| `asset.update.analytic.components.framework` | `integer` | no |
| `asset.update.analytic.components.kernel` | `integer` | no |
| `asset.update.analytic.components.kernelModule` | `integer` | no |
| `asset.update.analytic.components.library` | `integer` | no |
| `asset.update.analytic.components.os` | `integer` | no |
| `asset.update.analytic.components.package` | `integer` | no |
| `asset.update.analytic.credentials` | `object` | no |
| `asset.update.analytic.credentials.crackedCred` | `integer` | yes |
| `asset.update.analytic.credentials.crackedHash` | `integer` | yes |
| `asset.update.analytic.credentials.credential` | `integer` | no |
| `asset.update.analytic.credentials.hash` | `integer` | no |
| `asset.update.analytic.credentials.secrets` | `integer` | yes |
| `asset.update.analytic.cryptography` | `object` | no |
| `asset.update.analytic.cryptography.certificate` | `integer` | no |
| `asset.update.analytic.cryptography.privateKey` | `integer` | no |
| `asset.update.analytic.cryptography.publicKey` | `integer` | no |
| `asset.update.analytic.exploit` | `object` | no |
| `asset.update.analytic.exploit.botnet` | `integer` | no |
| `asset.update.analytic.exploit.exploitCode` | `integer` | yes |
| `asset.update.analytic.exploit.inKnownExploitedVulnerabilities` | `integer` | yes |
| `asset.update.analytic.exploit.inTheWild` | `integer` | no |
| `asset.update.analytic.exploit.knownAttacks` | `integer` | no |
| `asset.update.analytic.exploit.ransomware` | `integer` | no |
| `asset.update.analytic.exploit.threatActor` | `integer` | no |
| `asset.update.analytic.files` | `integer` | no |
| `asset.update.analytic.licenseIssues` | `integer` | no |
| `asset.update.analytic.misconfigurations` | `object` | no |
| `asset.update.analytic.misconfigurations.failed` | `integer` | no |
| `asset.update.analytic.misconfigurations.notApplicable` | `integer` | no |
| `asset.update.analytic.misconfigurations.passed` | `integer` | no |
| `asset.update.analytic.vulnerability` | `object` | no |
| `asset.update.analytic.vulnerability.critical` | `integer` | no |
| `asset.update.analytic.vulnerability.high` | `integer` | no |
| `asset.update.analytic.vulnerability.low` | `integer` | no |
| `asset.update.analytic.vulnerability.medium` | `integer` | no |
| `asset.update.assetCpe` | `string` | yes |
| `asset.update.assetGroupCount` | `integer` | yes |
| `asset.update.assetGroupIds[]` | `string` | yes |
| `asset.update.createdAt` | `string` | yes |
| `asset.update.fileName` | `string` | yes |
| `asset.update.filesystems[]` | `object` | yes |
| `asset.update.filesystems[].id` | `string` | no |
| `asset.update.filesystems[].files` | `object` | yes |
| `asset.update.filesystems[].files.filesList[]` | `object` | yes |
| `asset.update.filesystems[].files.filesList[].file` | `object` | yes |
| `asset.update.filesystems[].files.filesList[].fileId` | `string` | yes |
| `asset.update.filesystems[].files.pageInfo` | `object` | yes |
| `asset.update.filesystems[].files.pageInfo.nextPageToken` | `string` | yes |
| `asset.update.filesystems[].files.pageInfo.prevPageToken` | `string` | yes |
| `asset.update.filesystems[].files.pageInfo.totalSize` | `integer` | yes |
| `asset.update.firstAnalysisTime` | `string` | yes |
| `asset.update.hasRemediation` | `boolean` | yes |
| `asset.update.name` | `string` | yes |
| `asset.update.orgId` | `string` | yes |
| `asset.update.product` | `string` | yes |
| `asset.update.quantumCapable` | `boolean` | yes |
| `asset.update.risk` | `object` | yes |
| `asset.update.risk.category` | `RiskCategory` | yes |
| `asset.update.risk.rawScore` | `float` | yes |
| `asset.update.risk.score` | `float` | yes |
| `asset.update.sha256` | `string` | yes |
| `asset.update.sizeBytes` | `integer` | yes |
| `asset.update.status` | `ProcessingStatus` | yes |
| `asset.update.type` | `AssetType` | yes |
| `asset.update.updatedAt` | `string` | yes |
| `asset.update.uploadedBy` | `string` | yes |
| `asset.update.vendor` | `string` | yes |
| `asset.update.version` | `string` | yes |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    UpdateAssetInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.mutation_asset_update(asset_update_args=UpdateAssetInput(id='id_123'))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
