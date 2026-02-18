<!-- Generated file: do not edit by hand -->

# query_dependencies

List all software components and libraries identified in the asset.

## Parameters

| name | type | required |
| --- | --- | --- |
| `dependencies_args` | `DependencyInput` | `true` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `dependencies` | `object` | yes |
| `dependencies.edges[]` | `object` | yes |
| `dependencies.edges[].cursor` | `string` | yes |
| `dependencies.edges[].node` | `object` | yes |
| `dependencies.edges[].node.id` | `string` | no |
| `dependencies.edges[].node.analytic` | `object` | no |
| `dependencies.edges[].node.analytic.binaries` | `integer` | no |
| `dependencies.edges[].node.analytic.components` | `object` | no |
| `dependencies.edges[].node.analytic.components.application` | `integer` | no |
| `dependencies.edges[].node.analytic.components.container` | `integer` | no |
| `dependencies.edges[].node.analytic.components.device` | `integer` | no |
| `dependencies.edges[].node.analytic.components.framework` | `integer` | no |
| `dependencies.edges[].node.analytic.components.kernel` | `integer` | no |
| `dependencies.edges[].node.analytic.components.kernelModule` | `integer` | no |
| `dependencies.edges[].node.analytic.components.library` | `integer` | no |
| `dependencies.edges[].node.analytic.components.os` | `integer` | no |
| `dependencies.edges[].node.analytic.components.package` | `integer` | no |
| `dependencies.edges[].node.analytic.credentials` | `object` | no |
| `dependencies.edges[].node.analytic.credentials.crackedCred` | `integer` | yes |
| `dependencies.edges[].node.analytic.credentials.crackedHash` | `integer` | yes |
| `dependencies.edges[].node.analytic.credentials.credential` | `integer` | no |
| `dependencies.edges[].node.analytic.credentials.hash` | `integer` | no |
| `dependencies.edges[].node.analytic.credentials.secrets` | `integer` | yes |
| `dependencies.edges[].node.analytic.cryptography` | `object` | no |
| `dependencies.edges[].node.analytic.cryptography.certificate` | `integer` | no |
| `dependencies.edges[].node.analytic.cryptography.privateKey` | `integer` | no |
| `dependencies.edges[].node.analytic.cryptography.publicKey` | `integer` | no |
| `dependencies.edges[].node.analytic.exploit` | `object` | no |
| `dependencies.edges[].node.analytic.exploit.botnet` | `integer` | no |
| `dependencies.edges[].node.analytic.exploit.exploitCode` | `integer` | yes |
| `dependencies.edges[].node.analytic.exploit.inKnownExploitedVulnerabilities` | `integer` | yes |
| `dependencies.edges[].node.analytic.exploit.inTheWild` | `integer` | no |
| `dependencies.edges[].node.analytic.exploit.knownAttacks` | `integer` | no |
| `dependencies.edges[].node.analytic.exploit.ransomware` | `integer` | no |
| `dependencies.edges[].node.analytic.exploit.threatActor` | `integer` | no |
| `dependencies.edges[].node.analytic.files` | `integer` | no |
| `dependencies.edges[].node.analytic.licenseIssues` | `integer` | no |
| `dependencies.edges[].node.analytic.misconfigurations` | `object` | no |
| `dependencies.edges[].node.analytic.misconfigurations.failed` | `integer` | no |
| `dependencies.edges[].node.analytic.misconfigurations.notApplicable` | `integer` | no |
| `dependencies.edges[].node.analytic.misconfigurations.passed` | `integer` | no |
| `dependencies.edges[].node.analytic.vulnerability` | `object` | no |
| `dependencies.edges[].node.analytic.vulnerability.critical` | `integer` | no |
| `dependencies.edges[].node.analytic.vulnerability.high` | `integer` | no |
| `dependencies.edges[].node.analytic.vulnerability.low` | `integer` | no |
| `dependencies.edges[].node.analytic.vulnerability.medium` | `integer` | no |
| `dependencies.edges[].node.associatedFiles[]` | `object` | yes |
| `dependencies.edges[].node.associatedFiles[].badges[]` | `ComponentBadge` | yes |
| `dependencies.edges[].node.associatedFiles[].component` | `object` | no |
| `dependencies.edges[].node.associatedFiles[].component.id` | `string` | no |
| `dependencies.edges[].node.associatedFiles[].component.architecture` | `Architecture` | yes |
| `dependencies.edges[].node.associatedFiles[].component.confidence` | `Confidence` | yes |
| `dependencies.edges[].node.associatedFiles[].component.cpes[]` | `string` | yes |
| `dependencies.edges[].node.associatedFiles[].component.description` | `string` | yes |
| `dependencies.edges[].node.associatedFiles[].component.identificationIds[]` | `string` | yes |
| `dependencies.edges[].node.associatedFiles[].component.language[]` | `Language` | yes |
| `dependencies.edges[].node.associatedFiles[].component.license[]` | `string` | yes |
| `dependencies.edges[].node.associatedFiles[].component.name` | `string` | no |
| `dependencies.edges[].node.associatedFiles[].component.namespace` | `string` | yes |
| `dependencies.edges[].node.associatedFiles[].component.operatingSystem` | `string` | yes |
| `dependencies.edges[].node.associatedFiles[].component.operatingSystemKernelVersion` | `string` | yes |
| `dependencies.edges[].node.associatedFiles[].component.path` | `string` | yes |
| `dependencies.edges[].node.associatedFiles[].component.product` | `string` | yes |
| `dependencies.edges[].node.associatedFiles[].component.purls[]` | `string` | yes |
| `dependencies.edges[].node.associatedFiles[].component.sbomDependenciesCount` | `integer` | yes |
| `dependencies.edges[].node.associatedFiles[].component.subtype` | `ComponentSubType` | yes |
| `dependencies.edges[].node.associatedFiles[].component.type` | `ComponentType` | no |
| `dependencies.edges[].node.associatedFiles[].component.vendor` | `string` | yes |
| `dependencies.edges[].node.associatedFiles[].isConcrete` | `boolean` | no |
| `dependencies.edges[].node.correlations[]` | `object` | yes |
| `dependencies.edges[].node.correlations[].artifact` | `string` | yes |
| `dependencies.edges[].node.correlations[].assetId` | `string` | yes |
| `dependencies.edges[].node.correlations[].assetName` | `string` | yes |
| `dependencies.edges[].node.correlations[].location` | `string` | yes |
| `dependencies.edges[].node.correlations[].risk` | `object` | yes |
| `dependencies.edges[].node.correlations[].risk.category` | `RiskCategory` | yes |
| `dependencies.edges[].node.correlations[].risk.rawScore` | `float` | yes |
| `dependencies.edges[].node.correlations[].risk.score` | `float` | yes |
| `dependencies.edges[].node.correlations[].updatedAt` | `string` | yes |
| `dependencies.edges[].node.correlationsCount` | `integer` | yes |
| `dependencies.edges[].node.dependencies` | `object` | no |
| `dependencies.edges[].node.dependencies.dependents[]` | `object` | yes |
| `dependencies.edges[].node.dependencies.dependents[].badges[]` | `ComponentBadge` | yes |
| `dependencies.edges[].node.dependencies.dependents[].isConcrete` | `boolean` | no |
| `dependencies.edges[].node.dependencies.direct[]` | `object` | yes |
| `dependencies.edges[].node.dependencies.direct[].badges[]` | `ComponentBadge` | yes |
| `dependencies.edges[].node.dependencies.direct[].isConcrete` | `boolean` | no |
| `dependencies.edges[].node.dependencies.indirect[]` | `object` | yes |
| `dependencies.edges[].node.dependencies.indirect[].badges[]` | `ComponentBadge` | yes |
| `dependencies.edges[].node.dependencies.indirect[].isConcrete` | `boolean` | no |
| `dependencies.edges[].node.dependency` | `object` | no |
| `dependencies.edges[].node.dependency.id` | `string` | no |
| `dependencies.edges[].node.dependency.architecture` | `Architecture` | yes |
| `dependencies.edges[].node.dependency.confidence` | `Confidence` | yes |
| `dependencies.edges[].node.dependency.cpes[]` | `string` | yes |
| `dependencies.edges[].node.dependency.description` | `string` | yes |
| `dependencies.edges[].node.dependency.digest` | `object` | yes |
| `dependencies.edges[].node.dependency.digest.md5` | `string` | yes |
| `dependencies.edges[].node.dependency.digest.sha1` | `string` | yes |
| `dependencies.edges[].node.dependency.digest.sha256` | `string` | yes |
| `dependencies.edges[].node.dependency.file` | `object` | yes |
| `dependencies.edges[].node.dependency.file.createdAt` | `string` | yes |
| `dependencies.edges[].node.dependency.file.hasChildren` | `boolean` | yes |
| `dependencies.edges[].node.dependency.file.mimeType` | `string` | yes |
| `dependencies.edges[].node.dependency.file.path` | `string` | yes |
| `dependencies.edges[].node.dependency.file.permissions` | `string` | yes |
| `dependencies.edges[].node.dependency.file.size` | `integer` | yes |
| `dependencies.edges[].node.dependency.file.updatedAt` | `string` | yes |
| `dependencies.edges[].node.dependency.identificationIds[]` | `string` | yes |
| `dependencies.edges[].node.dependency.identifiers[]` | `object` | yes |
| `dependencies.edges[].node.dependency.identifiers[].type` | `IdentifierFormat` | no |
| `dependencies.edges[].node.dependency.identifiers[].uri` | `string` | no |
| `dependencies.edges[].node.dependency.language[]` | `Language` | yes |
| `dependencies.edges[].node.dependency.license[]` | `string` | yes |
| `dependencies.edges[].node.dependency.name` | `string` | no |
| `dependencies.edges[].node.dependency.namespace` | `string` | yes |
| `dependencies.edges[].node.dependency.operatingSystem` | `string` | yes |
| `dependencies.edges[].node.dependency.operatingSystemKernelVersion` | `string` | yes |
| `dependencies.edges[].node.dependency.package` | `object` | yes |
| `dependencies.edges[].node.dependency.package.language[]` | `Language` | yes |
| `dependencies.edges[].node.dependency.package.license` | `string` | yes |
| `dependencies.edges[].node.dependency.package.name` | `string` | no |
| `dependencies.edges[].node.dependency.package.summary` | `string` | yes |
| `dependencies.edges[].node.dependency.package.type` | `string` | yes |
| `dependencies.edges[].node.dependency.path` | `string` | yes |
| `dependencies.edges[].node.dependency.product` | `string` | yes |
| `dependencies.edges[].node.dependency.purls[]` | `string` | yes |
| `dependencies.edges[].node.dependency.sbomDependenciesCount` | `integer` | yes |
| `dependencies.edges[].node.dependency.subtype` | `ComponentSubType` | yes |
| `dependencies.edges[].node.dependency.type` | `ComponentType` | no |
| `dependencies.edges[].node.dependency.vendor` | `string` | yes |
| `dependencies.edges[].node.dependency.version` | `object` | yes |
| `dependencies.edges[].node.dependency.version.id` | `string` | yes |
| `dependencies.edges[].node.dependency.version.alternatives[]` | `string` | yes |
| `dependencies.edges[].node.dependency.version.isConcrete` | `boolean` | no |
| `dependencies.edges[].node.identifiedVia[]` | `IdentifiedViaCategory` | yes |
| `dependencies.edges[].node.latestRemediation` | `object` | yes |
| `dependencies.edges[].node.latestRemediation.author` | `string` | yes |
| `dependencies.edges[].node.latestRemediation.createdAt` | `string` | yes |
| `dependencies.edges[].node.latestRemediation.identificationId` | `string` | yes |
| `dependencies.edges[].node.latestRemediation.operationId` | `string` | yes |
| `dependencies.edges[].node.latestRemediation.operationType` | `IdentificationRemediationOperationType` | yes |
| `dependencies.edges[].node.latestRemediation.reason` | `string` | yes |
| `dependencies.edges[].node.latestRemediation.remediationAction` | `IdentificationRemediationAction` | yes |
| `dependencies.edges[].node.submitDatetime` | `typing.Annotated[datetime.datetime, BeforeValidator(func=<function parse_datetime at 0x1090d31a0>, json_schema_input_type=PydanticUndefined)]` | yes |
| `dependencies.edges[].node.verification` | `object` | no |
| `dependencies.edges[].node.verification.cryptographic` | `boolean` | no |
| `dependencies.edges[].node.verification.functionHashing` | `boolean` | no |
| `dependencies.edges[].node.verification.heuristic` | `boolean` | no |
| `dependencies.edges[].node.verification.package` | `boolean` | no |
| `dependencies.edges[].node.verification.symIndex` | `boolean` | no |
| `dependencies.edges[].node.verification.userModified` | `boolean` | no |
| `dependencies.pageInfo` | `object` | no |
| `dependencies.pageInfo.endCursor` | `string` | yes |
| `dependencies.pageInfo.hasNextPage` | `boolean` | no |
| `dependencies.pageInfo.hasPreviousPage` | `boolean` | no |
| `dependencies.pageInfo.startCursor` | `string` | yes |
| `dependencies.pageInfo.totalCount` | `integer` | yes |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    DependencyInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_dependencies(dependencies_args=DependencyInput(composed_asset_id='composed_asset_123'))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
