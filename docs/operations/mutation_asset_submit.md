<!-- Generated file: do not edit by hand -->

# mutation_asset_submit

Upload firmware or SBOMs with metadata, group assignments, and CPEs.

## Parameters

| name | type | required |
| --- | --- | --- |
| `asset_submit_file_name` | `str` | `true` |
| `asset_submit_args` | `Union[SubmitAssetInput, None, UnsetType]` | `false` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `asset` | `object` | yes |
| `asset.submit` | `object` | no |
| `asset.submit.asset` | `object` | yes |
| `asset.submit.asset.id` | `string` | yes |
| `asset.submit.asset.analytic` | `object` | yes |
| `asset.submit.asset.analytic.binaries` | `integer` | no |
| `asset.submit.asset.analytic.components` | `object` | no |
| `asset.submit.asset.analytic.components.application` | `integer` | no |
| `asset.submit.asset.analytic.components.container` | `integer` | no |
| `asset.submit.asset.analytic.components.device` | `integer` | no |
| `asset.submit.asset.analytic.components.framework` | `integer` | no |
| `asset.submit.asset.analytic.components.kernel` | `integer` | no |
| `asset.submit.asset.analytic.components.kernelModule` | `integer` | no |
| `asset.submit.asset.analytic.components.library` | `integer` | no |
| `asset.submit.asset.analytic.components.os` | `integer` | no |
| `asset.submit.asset.analytic.components.package` | `integer` | no |
| `asset.submit.asset.analytic.credentials` | `object` | no |
| `asset.submit.asset.analytic.credentials.crackedCred` | `integer` | yes |
| `asset.submit.asset.analytic.credentials.crackedHash` | `integer` | yes |
| `asset.submit.asset.analytic.credentials.credential` | `integer` | no |
| `asset.submit.asset.analytic.credentials.hash` | `integer` | no |
| `asset.submit.asset.analytic.credentials.secrets` | `integer` | yes |
| `asset.submit.asset.analytic.cryptography` | `object` | no |
| `asset.submit.asset.analytic.cryptography.certificate` | `integer` | no |
| `asset.submit.asset.analytic.cryptography.privateKey` | `integer` | no |
| `asset.submit.asset.analytic.cryptography.publicKey` | `integer` | no |
| `asset.submit.asset.analytic.exploit` | `object` | no |
| `asset.submit.asset.analytic.exploit.botnet` | `integer` | no |
| `asset.submit.asset.analytic.exploit.exploitCode` | `integer` | yes |
| `asset.submit.asset.analytic.exploit.inKnownExploitedVulnerabilities` | `integer` | yes |
| `asset.submit.asset.analytic.exploit.inTheWild` | `integer` | no |
| `asset.submit.asset.analytic.exploit.knownAttacks` | `integer` | no |
| `asset.submit.asset.analytic.exploit.ransomware` | `integer` | no |
| `asset.submit.asset.analytic.exploit.threatActor` | `integer` | no |
| `asset.submit.asset.analytic.files` | `integer` | no |
| `asset.submit.asset.analytic.licenseIssues` | `integer` | no |
| `asset.submit.asset.analytic.misconfigurations` | `object` | no |
| `asset.submit.asset.analytic.misconfigurations.failed` | `integer` | no |
| `asset.submit.asset.analytic.misconfigurations.notApplicable` | `integer` | no |
| `asset.submit.asset.analytic.misconfigurations.passed` | `integer` | no |
| `asset.submit.asset.analytic.vulnerability` | `object` | no |
| `asset.submit.asset.analytic.vulnerability.critical` | `integer` | no |
| `asset.submit.asset.analytic.vulnerability.high` | `integer` | no |
| `asset.submit.asset.analytic.vulnerability.low` | `integer` | no |
| `asset.submit.asset.analytic.vulnerability.medium` | `integer` | no |
| `asset.submit.asset.assetCpe` | `string` | yes |
| `asset.submit.asset.assetGroupCount` | `integer` | yes |
| `asset.submit.asset.assetGroupIds[]` | `string` | yes |
| `asset.submit.asset.createdAt` | `string` | yes |
| `asset.submit.asset.fileName` | `string` | yes |
| `asset.submit.asset.filesystems[]` | `object` | yes |
| `asset.submit.asset.filesystems[].id` | `string` | no |
| `asset.submit.asset.filesystems[].files` | `object` | yes |
| `asset.submit.asset.filesystems[].files.filesList[]` | `object` | yes |
| `asset.submit.asset.filesystems[].files.pageInfo` | `object` | yes |
| `asset.submit.asset.firstAnalysisTime` | `string` | yes |
| `asset.submit.asset.hasRemediation` | `boolean` | yes |
| `asset.submit.asset.name` | `string` | yes |
| `asset.submit.asset.orgId` | `string` | yes |
| `asset.submit.asset.product` | `string` | yes |
| `asset.submit.asset.quantumCapable` | `boolean` | yes |
| `asset.submit.asset.risk` | `object` | yes |
| `asset.submit.asset.risk.category` | `RiskCategory` | yes |
| `asset.submit.asset.risk.rawScore` | `float` | yes |
| `asset.submit.asset.risk.score` | `float` | yes |
| `asset.submit.asset.sha256` | `string` | yes |
| `asset.submit.asset.sizeBytes` | `integer` | yes |
| `asset.submit.asset.status` | `ProcessingStatus` | yes |
| `asset.submit.asset.type` | `AssetType` | yes |
| `asset.submit.asset.updatedAt` | `string` | yes |
| `asset.submit.asset.uploadedBy` | `string` | yes |
| `asset.submit.asset.vendor` | `string` | yes |
| `asset.submit.asset.version` | `string` | yes |
| `asset.submit.uploadId` | `string` | no |
| `asset.submit.uploadUrl` | `string` | no |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    SubmitAssetInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.mutation_asset_submit(asset_submit_file_name='firmware.bin', asset_submit_args=SubmitAssetInput())
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
