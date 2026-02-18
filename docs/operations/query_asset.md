<!-- Generated file: do not edit by hand -->

# query_asset

Retrieve detailed metadata and risk information for a single asset.

## Parameters

| name | type | required |
| --- | --- | --- |
| `asset_args` | `Union[AssetInput, None, UnsetType]` | `false` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `asset` | `object` | yes |
| `asset.id` | `string` | yes |
| `asset.analytic` | `object` | yes |
| `asset.analytic.binaries` | `integer` | no |
| `asset.analytic.components` | `object` | no |
| `asset.analytic.components.application` | `integer` | no |
| `asset.analytic.components.container` | `integer` | no |
| `asset.analytic.components.device` | `integer` | no |
| `asset.analytic.components.framework` | `integer` | no |
| `asset.analytic.components.kernel` | `integer` | no |
| `asset.analytic.components.kernelModule` | `integer` | no |
| `asset.analytic.components.library` | `integer` | no |
| `asset.analytic.components.os` | `integer` | no |
| `asset.analytic.components.package` | `integer` | no |
| `asset.analytic.credentials` | `object` | no |
| `asset.analytic.credentials.crackedCred` | `integer` | yes |
| `asset.analytic.credentials.crackedHash` | `integer` | yes |
| `asset.analytic.credentials.credential` | `integer` | no |
| `asset.analytic.credentials.hash` | `integer` | no |
| `asset.analytic.credentials.secrets` | `integer` | yes |
| `asset.analytic.cryptography` | `object` | no |
| `asset.analytic.cryptography.certificate` | `integer` | no |
| `asset.analytic.cryptography.privateKey` | `integer` | no |
| `asset.analytic.cryptography.publicKey` | `integer` | no |
| `asset.analytic.exploit` | `object` | no |
| `asset.analytic.exploit.botnet` | `integer` | no |
| `asset.analytic.exploit.exploitCode` | `integer` | yes |
| `asset.analytic.exploit.inKnownExploitedVulnerabilities` | `integer` | yes |
| `asset.analytic.exploit.inTheWild` | `integer` | no |
| `asset.analytic.exploit.knownAttacks` | `integer` | no |
| `asset.analytic.exploit.ransomware` | `integer` | no |
| `asset.analytic.exploit.threatActor` | `integer` | no |
| `asset.analytic.files` | `integer` | no |
| `asset.analytic.licenseIssues` | `integer` | no |
| `asset.analytic.misconfigurations` | `object` | no |
| `asset.analytic.misconfigurations.failed` | `integer` | no |
| `asset.analytic.misconfigurations.notApplicable` | `integer` | no |
| `asset.analytic.misconfigurations.passed` | `integer` | no |
| `asset.analytic.vulnerability` | `object` | no |
| `asset.analytic.vulnerability.critical` | `integer` | no |
| `asset.analytic.vulnerability.high` | `integer` | no |
| `asset.analytic.vulnerability.low` | `integer` | no |
| `asset.analytic.vulnerability.medium` | `integer` | no |
| `asset.assetCpe` | `string` | yes |
| `asset.assetGroupCount` | `integer` | yes |
| `asset.assetGroupIds[]` | `string` | yes |
| `asset.createdAt` | `string` | yes |
| `asset.fileName` | `string` | yes |
| `asset.filesystems[]` | `object` | yes |
| `asset.filesystems[].id` | `string` | no |
| `asset.filesystems[].files` | `object` | yes |
| `asset.filesystems[].files.filesList[]` | `object` | yes |
| `asset.filesystems[].files.filesList[].file` | `object` | yes |
| `asset.filesystems[].files.filesList[].file.createdAt` | `string` | yes |
| `asset.filesystems[].files.filesList[].file.hasChildren` | `boolean` | yes |
| `asset.filesystems[].files.filesList[].file.mimeType` | `string` | yes |
| `asset.filesystems[].files.filesList[].file.path` | `string` | yes |
| `asset.filesystems[].files.filesList[].file.permissions` | `string` | yes |
| `asset.filesystems[].files.filesList[].file.size` | `integer` | yes |
| `asset.filesystems[].files.filesList[].file.updatedAt` | `string` | yes |
| `asset.filesystems[].files.filesList[].fileId` | `string` | yes |
| `asset.filesystems[].files.pageInfo` | `object` | yes |
| `asset.filesystems[].files.pageInfo.nextPageToken` | `string` | yes |
| `asset.filesystems[].files.pageInfo.prevPageToken` | `string` | yes |
| `asset.filesystems[].files.pageInfo.totalSize` | `integer` | yes |
| `asset.firstAnalysisTime` | `string` | yes |
| `asset.hasRemediation` | `boolean` | yes |
| `asset.name` | `string` | yes |
| `asset.orgId` | `string` | yes |
| `asset.product` | `string` | yes |
| `asset.quantumCapable` | `boolean` | yes |
| `asset.risk` | `object` | yes |
| `asset.risk.category` | `RiskCategory` | yes |
| `asset.risk.rawScore` | `float` | yes |
| `asset.risk.score` | `float` | yes |
| `asset.sha256` | `string` | yes |
| `asset.sizeBytes` | `integer` | yes |
| `asset.status` | `ProcessingStatus` | yes |
| `asset.type` | `AssetType` | yes |
| `asset.updatedAt` | `string` | yes |
| `asset.uploadedBy` | `string` | yes |
| `asset.vendor` | `string` | yes |
| `asset.version` | `string` | yes |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    AssetInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_asset(asset_args=AssetInput())
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
