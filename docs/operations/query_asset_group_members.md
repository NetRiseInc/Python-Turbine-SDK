<!-- Generated file: do not edit by hand -->

# query_asset_group_members

List all assets associated with a specific asset group container.

## Parameters

| name | type | required |
| --- | --- | --- |
| `asset_group_members_args` | `AssetGroupMembersInput` | `true` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `assetGroupMembers` | `object` | no |
| `assetGroupMembers.edges[]` | `object` | yes |
| `assetGroupMembers.edges[].cursor` | `string` | yes |
| `assetGroupMembers.edges[].node` | `object` | yes |
| `assetGroupMembers.edges[].node.id` | `string` | yes |
| `assetGroupMembers.edges[].node.analytic` | `object` | yes |
| `assetGroupMembers.edges[].node.analytic.binaries` | `integer` | no |
| `assetGroupMembers.edges[].node.analytic.components` | `object` | no |
| `assetGroupMembers.edges[].node.analytic.components.application` | `integer` | no |
| `assetGroupMembers.edges[].node.analytic.components.container` | `integer` | no |
| `assetGroupMembers.edges[].node.analytic.components.device` | `integer` | no |
| `assetGroupMembers.edges[].node.analytic.components.framework` | `integer` | no |
| `assetGroupMembers.edges[].node.analytic.components.kernel` | `integer` | no |
| `assetGroupMembers.edges[].node.analytic.components.kernelModule` | `integer` | no |
| `assetGroupMembers.edges[].node.analytic.components.library` | `integer` | no |
| `assetGroupMembers.edges[].node.analytic.components.os` | `integer` | no |
| `assetGroupMembers.edges[].node.analytic.components.package` | `integer` | no |
| `assetGroupMembers.edges[].node.analytic.credentials` | `object` | no |
| `assetGroupMembers.edges[].node.analytic.credentials.crackedCred` | `integer` | yes |
| `assetGroupMembers.edges[].node.analytic.credentials.crackedHash` | `integer` | yes |
| `assetGroupMembers.edges[].node.analytic.credentials.credential` | `integer` | no |
| `assetGroupMembers.edges[].node.analytic.credentials.hash` | `integer` | no |
| `assetGroupMembers.edges[].node.analytic.credentials.secrets` | `integer` | yes |
| `assetGroupMembers.edges[].node.analytic.cryptography` | `object` | no |
| `assetGroupMembers.edges[].node.analytic.cryptography.certificate` | `integer` | no |
| `assetGroupMembers.edges[].node.analytic.cryptography.privateKey` | `integer` | no |
| `assetGroupMembers.edges[].node.analytic.cryptography.publicKey` | `integer` | no |
| `assetGroupMembers.edges[].node.analytic.exploit` | `object` | no |
| `assetGroupMembers.edges[].node.analytic.exploit.botnet` | `integer` | no |
| `assetGroupMembers.edges[].node.analytic.exploit.exploitCode` | `integer` | yes |
| `assetGroupMembers.edges[].node.analytic.exploit.inKnownExploitedVulnerabilities` | `integer` | yes |
| `assetGroupMembers.edges[].node.analytic.exploit.inTheWild` | `integer` | no |
| `assetGroupMembers.edges[].node.analytic.exploit.knownAttacks` | `integer` | no |
| `assetGroupMembers.edges[].node.analytic.exploit.ransomware` | `integer` | no |
| `assetGroupMembers.edges[].node.analytic.exploit.threatActor` | `integer` | no |
| `assetGroupMembers.edges[].node.analytic.files` | `integer` | no |
| `assetGroupMembers.edges[].node.analytic.licenseIssues` | `integer` | no |
| `assetGroupMembers.edges[].node.analytic.misconfigurations` | `object` | no |
| `assetGroupMembers.edges[].node.analytic.misconfigurations.failed` | `integer` | no |
| `assetGroupMembers.edges[].node.analytic.misconfigurations.notApplicable` | `integer` | no |
| `assetGroupMembers.edges[].node.analytic.misconfigurations.passed` | `integer` | no |
| `assetGroupMembers.edges[].node.analytic.vulnerability` | `object` | no |
| `assetGroupMembers.edges[].node.analytic.vulnerability.critical` | `integer` | no |
| `assetGroupMembers.edges[].node.analytic.vulnerability.high` | `integer` | no |
| `assetGroupMembers.edges[].node.analytic.vulnerability.low` | `integer` | no |
| `assetGroupMembers.edges[].node.analytic.vulnerability.medium` | `integer` | no |
| `assetGroupMembers.edges[].node.assetCpe` | `string` | yes |
| `assetGroupMembers.edges[].node.assetGroupCount` | `integer` | yes |
| `assetGroupMembers.edges[].node.assetGroupIds[]` | `string` | yes |
| `assetGroupMembers.edges[].node.createdAt` | `string` | yes |
| `assetGroupMembers.edges[].node.fileName` | `string` | yes |
| `assetGroupMembers.edges[].node.filesystems[]` | `object` | yes |
| `assetGroupMembers.edges[].node.filesystems[].id` | `string` | no |
| `assetGroupMembers.edges[].node.firstAnalysisTime` | `string` | yes |
| `assetGroupMembers.edges[].node.hasRemediation` | `boolean` | yes |
| `assetGroupMembers.edges[].node.name` | `string` | yes |
| `assetGroupMembers.edges[].node.orgId` | `string` | yes |
| `assetGroupMembers.edges[].node.product` | `string` | yes |
| `assetGroupMembers.edges[].node.quantumCapable` | `boolean` | yes |
| `assetGroupMembers.edges[].node.risk` | `object` | yes |
| `assetGroupMembers.edges[].node.risk.category` | `RiskCategory` | yes |
| `assetGroupMembers.edges[].node.risk.rawScore` | `float` | yes |
| `assetGroupMembers.edges[].node.risk.score` | `float` | yes |
| `assetGroupMembers.edges[].node.sha256` | `string` | yes |
| `assetGroupMembers.edges[].node.sizeBytes` | `integer` | yes |
| `assetGroupMembers.edges[].node.status` | `ProcessingStatus` | yes |
| `assetGroupMembers.edges[].node.type` | `AssetType` | yes |
| `assetGroupMembers.edges[].node.updatedAt` | `string` | yes |
| `assetGroupMembers.edges[].node.uploadedBy` | `string` | yes |
| `assetGroupMembers.edges[].node.vendor` | `string` | yes |
| `assetGroupMembers.edges[].node.version` | `string` | yes |
| `assetGroupMembers.pageInfo` | `object` | no |
| `assetGroupMembers.pageInfo.endCursor` | `string` | yes |
| `assetGroupMembers.pageInfo.hasNextPage` | `boolean` | no |
| `assetGroupMembers.pageInfo.hasPreviousPage` | `boolean` | no |
| `assetGroupMembers.pageInfo.startCursor` | `string` | yes |
| `assetGroupMembers.pageInfo.totalCount` | `integer` | yes |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    AssetGroupMembersInput,
    Cursor,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_asset_group_members(asset_group_members_args=AssetGroupMembersInput(group_id='group_123', cursor=Cursor()))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
