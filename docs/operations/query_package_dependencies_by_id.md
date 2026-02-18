<!-- Generated file: do not edit by hand -->

# query_package_dependencies_by_id

View the dependency tree hierarchy for a specific software package.

## Parameters

| name | type | required |
| --- | --- | --- |
| `package_dependencies_by_id_args` | `packageDependenciesByIdInput` | `true` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `packageDependenciesById` | `object` | yes |
| `packageDependenciesById.associatedFiles[]` | `object` | yes |
| `packageDependenciesById.associatedFiles[].badges[]` | `ComponentBadge` | yes |
| `packageDependenciesById.associatedFiles[].component` | `object` | no |
| `packageDependenciesById.associatedFiles[].component.id` | `string` | no |
| `packageDependenciesById.associatedFiles[].component.architecture` | `Architecture` | yes |
| `packageDependenciesById.associatedFiles[].component.confidence` | `Confidence` | yes |
| `packageDependenciesById.associatedFiles[].component.cpes[]` | `string` | yes |
| `packageDependenciesById.associatedFiles[].component.description` | `string` | yes |
| `packageDependenciesById.associatedFiles[].component.digest` | `object` | yes |
| `packageDependenciesById.associatedFiles[].component.digest.md5` | `string` | yes |
| `packageDependenciesById.associatedFiles[].component.digest.sha1` | `string` | yes |
| `packageDependenciesById.associatedFiles[].component.digest.sha256` | `string` | yes |
| `packageDependenciesById.associatedFiles[].component.file` | `object` | yes |
| `packageDependenciesById.associatedFiles[].component.file.assets[]` | `object` | yes |
| `packageDependenciesById.associatedFiles[].component.file.assets[].id` | `string` | yes |
| `packageDependenciesById.associatedFiles[].component.file.assets[].assetCpe` | `string` | yes |
| `packageDependenciesById.associatedFiles[].component.file.assets[].assetGroupCount` | `integer` | yes |
| `packageDependenciesById.associatedFiles[].component.file.assets[].assetGroupIds[]` | `string` | yes |
| `packageDependenciesById.associatedFiles[].component.file.assets[].createdAt` | `string` | yes |
| `packageDependenciesById.associatedFiles[].component.file.assets[].fileName` | `string` | yes |
| `packageDependenciesById.associatedFiles[].component.file.assets[].firstAnalysisTime` | `string` | yes |
| `packageDependenciesById.associatedFiles[].component.file.assets[].hasRemediation` | `boolean` | yes |
| `packageDependenciesById.associatedFiles[].component.file.assets[].name` | `string` | yes |
| `packageDependenciesById.associatedFiles[].component.file.assets[].orgId` | `string` | yes |
| `packageDependenciesById.associatedFiles[].component.file.assets[].product` | `string` | yes |
| `packageDependenciesById.associatedFiles[].component.file.assets[].quantumCapable` | `boolean` | yes |
| `packageDependenciesById.associatedFiles[].component.file.assets[].sha256` | `string` | yes |
| `packageDependenciesById.associatedFiles[].component.file.assets[].sizeBytes` | `integer` | yes |
| `packageDependenciesById.associatedFiles[].component.file.assets[].status` | `ProcessingStatus` | yes |
| `packageDependenciesById.associatedFiles[].component.file.assets[].type` | `AssetType` | yes |
| `packageDependenciesById.associatedFiles[].component.file.assets[].updatedAt` | `string` | yes |
| `packageDependenciesById.associatedFiles[].component.file.assets[].uploadedBy` | `string` | yes |
| `packageDependenciesById.associatedFiles[].component.file.assets[].vendor` | `string` | yes |
| `packageDependenciesById.associatedFiles[].component.file.assets[].version` | `string` | yes |
| `packageDependenciesById.associatedFiles[].component.file.createdAt` | `string` | yes |
| `packageDependenciesById.associatedFiles[].component.file.digest` | `object` | yes |
| `packageDependenciesById.associatedFiles[].component.file.digest.md5` | `string` | yes |
| `packageDependenciesById.associatedFiles[].component.file.digest.sha1` | `string` | yes |
| `packageDependenciesById.associatedFiles[].component.file.digest.sha256` | `string` | yes |
| `packageDependenciesById.associatedFiles[].component.file.hasChildren` | `boolean` | yes |
| `packageDependenciesById.associatedFiles[].component.file.mimeType` | `string` | yes |
| `packageDependenciesById.associatedFiles[].component.file.path` | `string` | yes |
| `packageDependenciesById.associatedFiles[].component.file.permissions` | `string` | yes |
| `packageDependenciesById.associatedFiles[].component.file.similarity` | `object` | yes |
| `packageDependenciesById.associatedFiles[].component.file.similarity.file` | `string` | yes |
| `packageDependenciesById.associatedFiles[].component.file.similarity.ordinal` | `integer` | yes |
| `packageDependenciesById.associatedFiles[].component.file.similarity.similarity` | `float` | yes |
| `packageDependenciesById.associatedFiles[].component.file.similarity.text` | `string` | yes |
| `packageDependenciesById.associatedFiles[].component.file.size` | `integer` | yes |
| `packageDependenciesById.associatedFiles[].component.file.updatedAt` | `string` | yes |
| `packageDependenciesById.associatedFiles[].component.identificationIds[]` | `string` | yes |
| `packageDependenciesById.associatedFiles[].component.identifiers[]` | `object` | yes |
| `packageDependenciesById.associatedFiles[].component.identifiers[].type` | `IdentifierFormat` | no |
| `packageDependenciesById.associatedFiles[].component.identifiers[].uri` | `string` | no |
| `packageDependenciesById.associatedFiles[].component.language[]` | `Language` | yes |
| `packageDependenciesById.associatedFiles[].component.license[]` | `string` | yes |
| `packageDependenciesById.associatedFiles[].component.name` | `string` | no |
| `packageDependenciesById.associatedFiles[].component.namespace` | `string` | yes |
| `packageDependenciesById.associatedFiles[].component.operatingSystem` | `string` | yes |
| `packageDependenciesById.associatedFiles[].component.operatingSystemKernelVersion` | `string` | yes |
| `packageDependenciesById.associatedFiles[].component.package` | `object` | yes |
| `packageDependenciesById.associatedFiles[].component.package.associatedFiles[]` | `object` | yes |
| `packageDependenciesById.associatedFiles[].component.package.associatedFiles[].fidelity` | `Fidelity` | no |
| `packageDependenciesById.associatedFiles[].component.package.associatedFiles[].method` | `string` | no |
| `packageDependenciesById.associatedFiles[].component.package.associatedFiles[].type` | `CoordinateType` | no |
| `packageDependenciesById.associatedFiles[].component.package.associatedFiles[].value` | `string` | no |
| `packageDependenciesById.associatedFiles[].component.package.authors[]` | `object` | yes |
| `packageDependenciesById.associatedFiles[].component.package.authors[].address` | `string` | no |
| `packageDependenciesById.associatedFiles[].component.package.authors[].title` | `string` | yes |
| `packageDependenciesById.associatedFiles[].component.package.dependencies[]` | `object` | yes |
| `packageDependenciesById.associatedFiles[].component.package.dependencies[].name` | `string` | no |
| `packageDependenciesById.associatedFiles[].component.package.language[]` | `Language` | yes |
| `packageDependenciesById.associatedFiles[].component.package.license` | `string` | yes |
| `packageDependenciesById.associatedFiles[].component.package.maintainers[]` | `object` | yes |
| `packageDependenciesById.associatedFiles[].component.package.maintainers[].address` | `string` | no |
| `packageDependenciesById.associatedFiles[].component.package.maintainers[].title` | `string` | yes |
| `packageDependenciesById.associatedFiles[].component.package.name` | `string` | no |
| `packageDependenciesById.associatedFiles[].component.package.provides[]` | `object` | yes |
| `packageDependenciesById.associatedFiles[].component.package.provides[].name` | `string` | no |
| `packageDependenciesById.associatedFiles[].component.package.rawVersion` | `object` | yes |
| `packageDependenciesById.associatedFiles[].component.package.rawVersion.id` | `string` | yes |
| `packageDependenciesById.associatedFiles[].component.package.rawVersion.alternatives[]` | `string` | yes |
| `packageDependenciesById.associatedFiles[].component.package.rawVersion.isConcrete` | `boolean` | no |
| `packageDependenciesById.associatedFiles[].component.package.referenceLinks[]` | `object` | yes |
| `packageDependenciesById.associatedFiles[].component.package.referenceLinks[].type` | `ReferenceLinkType` | no |
| `packageDependenciesById.associatedFiles[].component.package.referenceLinks[].url` | `string` | no |
| `packageDependenciesById.associatedFiles[].component.package.summary` | `string` | yes |
| `packageDependenciesById.associatedFiles[].component.package.type` | `string` | yes |
| `packageDependenciesById.associatedFiles[].component.package.version` | `object` | yes |
| `packageDependenciesById.associatedFiles[].component.package.version.id` | `string` | yes |
| `packageDependenciesById.associatedFiles[].component.package.version.alternatives[]` | `string` | yes |
| `packageDependenciesById.associatedFiles[].component.package.version.isConcrete` | `boolean` | no |
| `packageDependenciesById.associatedFiles[].component.path` | `string` | yes |
| `packageDependenciesById.associatedFiles[].component.product` | `string` | yes |
| `packageDependenciesById.associatedFiles[].component.purls[]` | `string` | yes |
| `packageDependenciesById.associatedFiles[].component.sbomDependenciesCount` | `integer` | yes |
| `packageDependenciesById.associatedFiles[].component.subtype` | `ComponentSubType` | yes |
| `packageDependenciesById.associatedFiles[].component.type` | `ComponentType` | no |
| `packageDependenciesById.associatedFiles[].component.vendor` | `string` | yes |
| `packageDependenciesById.associatedFiles[].component.version` | `object` | yes |
| `packageDependenciesById.associatedFiles[].component.version.id` | `string` | yes |
| `packageDependenciesById.associatedFiles[].component.version.alternatives[]` | `string` | yes |
| `packageDependenciesById.associatedFiles[].component.version.isConcrete` | `boolean` | no |
| `packageDependenciesById.associatedFiles[].isConcrete` | `boolean` | no |
| `packageDependenciesById.dependencies` | `object` | yes |
| `packageDependenciesById.dependencies.dependents[]` | `object` | yes |
| `packageDependenciesById.dependencies.dependents[].badges[]` | `ComponentBadge` | yes |
| `packageDependenciesById.dependencies.dependents[].component` | `object` | no |
| `packageDependenciesById.dependencies.dependents[].component.id` | `string` | no |
| `packageDependenciesById.dependencies.dependents[].component.architecture` | `Architecture` | yes |
| `packageDependenciesById.dependencies.dependents[].component.confidence` | `Confidence` | yes |
| `packageDependenciesById.dependencies.dependents[].component.cpes[]` | `string` | yes |
| `packageDependenciesById.dependencies.dependents[].component.description` | `string` | yes |
| `packageDependenciesById.dependencies.dependents[].component.digest` | `object` | yes |
| `packageDependenciesById.dependencies.dependents[].component.digest.md5` | `string` | yes |
| `packageDependenciesById.dependencies.dependents[].component.digest.sha1` | `string` | yes |
| `packageDependenciesById.dependencies.dependents[].component.digest.sha256` | `string` | yes |
| `packageDependenciesById.dependencies.dependents[].component.file` | `object` | yes |
| `packageDependenciesById.dependencies.dependents[].component.file.createdAt` | `string` | yes |
| `packageDependenciesById.dependencies.dependents[].component.file.hasChildren` | `boolean` | yes |
| `packageDependenciesById.dependencies.dependents[].component.file.mimeType` | `string` | yes |
| `packageDependenciesById.dependencies.dependents[].component.file.path` | `string` | yes |
| `packageDependenciesById.dependencies.dependents[].component.file.permissions` | `string` | yes |
| `packageDependenciesById.dependencies.dependents[].component.file.size` | `integer` | yes |
| `packageDependenciesById.dependencies.dependents[].component.file.updatedAt` | `string` | yes |
| `packageDependenciesById.dependencies.dependents[].component.identificationIds[]` | `string` | yes |
| `packageDependenciesById.dependencies.dependents[].component.identifiers[]` | `object` | yes |
| `packageDependenciesById.dependencies.dependents[].component.identifiers[].type` | `IdentifierFormat` | no |
| `packageDependenciesById.dependencies.dependents[].component.identifiers[].uri` | `string` | no |
| `packageDependenciesById.dependencies.dependents[].component.language[]` | `Language` | yes |
| `packageDependenciesById.dependencies.dependents[].component.license[]` | `string` | yes |
| `packageDependenciesById.dependencies.dependents[].component.name` | `string` | no |
| `packageDependenciesById.dependencies.dependents[].component.namespace` | `string` | yes |
| `packageDependenciesById.dependencies.dependents[].component.operatingSystem` | `string` | yes |
| `packageDependenciesById.dependencies.dependents[].component.operatingSystemKernelVersion` | `string` | yes |
| `packageDependenciesById.dependencies.dependents[].component.package` | `object` | yes |
| `packageDependenciesById.dependencies.dependents[].component.package.language[]` | `Language` | yes |
| `packageDependenciesById.dependencies.dependents[].component.package.license` | `string` | yes |
| `packageDependenciesById.dependencies.dependents[].component.package.name` | `string` | no |
| `packageDependenciesById.dependencies.dependents[].component.package.summary` | `string` | yes |
| `packageDependenciesById.dependencies.dependents[].component.package.type` | `string` | yes |
| `packageDependenciesById.dependencies.dependents[].component.path` | `string` | yes |
| `packageDependenciesById.dependencies.dependents[].component.product` | `string` | yes |
| `packageDependenciesById.dependencies.dependents[].component.purls[]` | `string` | yes |
| `packageDependenciesById.dependencies.dependents[].component.sbomDependenciesCount` | `integer` | yes |
| `packageDependenciesById.dependencies.dependents[].component.subtype` | `ComponentSubType` | yes |
| `packageDependenciesById.dependencies.dependents[].component.type` | `ComponentType` | no |
| `packageDependenciesById.dependencies.dependents[].component.vendor` | `string` | yes |
| `packageDependenciesById.dependencies.dependents[].component.version` | `object` | yes |
| `packageDependenciesById.dependencies.dependents[].component.version.id` | `string` | yes |
| `packageDependenciesById.dependencies.dependents[].component.version.alternatives[]` | `string` | yes |
| `packageDependenciesById.dependencies.dependents[].component.version.isConcrete` | `boolean` | no |
| `packageDependenciesById.dependencies.dependents[].isConcrete` | `boolean` | no |
| `packageDependenciesById.dependencies.direct[]` | `object` | yes |
| `packageDependenciesById.dependencies.direct[].badges[]` | `ComponentBadge` | yes |
| `packageDependenciesById.dependencies.direct[].component` | `object` | no |
| `packageDependenciesById.dependencies.direct[].component.id` | `string` | no |
| `packageDependenciesById.dependencies.direct[].component.architecture` | `Architecture` | yes |
| `packageDependenciesById.dependencies.direct[].component.confidence` | `Confidence` | yes |
| `packageDependenciesById.dependencies.direct[].component.cpes[]` | `string` | yes |
| `packageDependenciesById.dependencies.direct[].component.description` | `string` | yes |
| `packageDependenciesById.dependencies.direct[].component.digest` | `object` | yes |
| `packageDependenciesById.dependencies.direct[].component.digest.md5` | `string` | yes |
| `packageDependenciesById.dependencies.direct[].component.digest.sha1` | `string` | yes |
| `packageDependenciesById.dependencies.direct[].component.digest.sha256` | `string` | yes |
| `packageDependenciesById.dependencies.direct[].component.file` | `object` | yes |
| `packageDependenciesById.dependencies.direct[].component.file.createdAt` | `string` | yes |
| `packageDependenciesById.dependencies.direct[].component.file.hasChildren` | `boolean` | yes |
| `packageDependenciesById.dependencies.direct[].component.file.mimeType` | `string` | yes |
| `packageDependenciesById.dependencies.direct[].component.file.path` | `string` | yes |
| `packageDependenciesById.dependencies.direct[].component.file.permissions` | `string` | yes |
| `packageDependenciesById.dependencies.direct[].component.file.size` | `integer` | yes |
| `packageDependenciesById.dependencies.direct[].component.file.updatedAt` | `string` | yes |
| `packageDependenciesById.dependencies.direct[].component.identificationIds[]` | `string` | yes |
| `packageDependenciesById.dependencies.direct[].component.identifiers[]` | `object` | yes |
| `packageDependenciesById.dependencies.direct[].component.identifiers[].type` | `IdentifierFormat` | no |
| `packageDependenciesById.dependencies.direct[].component.identifiers[].uri` | `string` | no |
| `packageDependenciesById.dependencies.direct[].component.language[]` | `Language` | yes |
| `packageDependenciesById.dependencies.direct[].component.license[]` | `string` | yes |
| `packageDependenciesById.dependencies.direct[].component.name` | `string` | no |
| `packageDependenciesById.dependencies.direct[].component.namespace` | `string` | yes |
| `packageDependenciesById.dependencies.direct[].component.operatingSystem` | `string` | yes |
| `packageDependenciesById.dependencies.direct[].component.operatingSystemKernelVersion` | `string` | yes |
| `packageDependenciesById.dependencies.direct[].component.package` | `object` | yes |
| `packageDependenciesById.dependencies.direct[].component.package.language[]` | `Language` | yes |
| `packageDependenciesById.dependencies.direct[].component.package.license` | `string` | yes |
| `packageDependenciesById.dependencies.direct[].component.package.name` | `string` | no |
| `packageDependenciesById.dependencies.direct[].component.package.summary` | `string` | yes |
| `packageDependenciesById.dependencies.direct[].component.package.type` | `string` | yes |
| `packageDependenciesById.dependencies.direct[].component.path` | `string` | yes |
| `packageDependenciesById.dependencies.direct[].component.product` | `string` | yes |
| `packageDependenciesById.dependencies.direct[].component.purls[]` | `string` | yes |
| `packageDependenciesById.dependencies.direct[].component.sbomDependenciesCount` | `integer` | yes |
| `packageDependenciesById.dependencies.direct[].component.subtype` | `ComponentSubType` | yes |
| `packageDependenciesById.dependencies.direct[].component.type` | `ComponentType` | no |
| `packageDependenciesById.dependencies.direct[].component.vendor` | `string` | yes |
| `packageDependenciesById.dependencies.direct[].component.version` | `object` | yes |
| `packageDependenciesById.dependencies.direct[].component.version.id` | `string` | yes |
| `packageDependenciesById.dependencies.direct[].component.version.alternatives[]` | `string` | yes |
| `packageDependenciesById.dependencies.direct[].component.version.isConcrete` | `boolean` | no |
| `packageDependenciesById.dependencies.direct[].isConcrete` | `boolean` | no |
| `packageDependenciesById.dependencies.indirect[]` | `object` | yes |
| `packageDependenciesById.dependencies.indirect[].badges[]` | `ComponentBadge` | yes |
| `packageDependenciesById.dependencies.indirect[].component` | `object` | no |
| `packageDependenciesById.dependencies.indirect[].component.id` | `string` | no |
| `packageDependenciesById.dependencies.indirect[].component.architecture` | `Architecture` | yes |
| `packageDependenciesById.dependencies.indirect[].component.confidence` | `Confidence` | yes |
| `packageDependenciesById.dependencies.indirect[].component.cpes[]` | `string` | yes |
| `packageDependenciesById.dependencies.indirect[].component.description` | `string` | yes |
| `packageDependenciesById.dependencies.indirect[].component.digest` | `object` | yes |
| `packageDependenciesById.dependencies.indirect[].component.digest.md5` | `string` | yes |
| `packageDependenciesById.dependencies.indirect[].component.digest.sha1` | `string` | yes |
| `packageDependenciesById.dependencies.indirect[].component.digest.sha256` | `string` | yes |
| `packageDependenciesById.dependencies.indirect[].component.file` | `object` | yes |
| `packageDependenciesById.dependencies.indirect[].component.file.createdAt` | `string` | yes |
| `packageDependenciesById.dependencies.indirect[].component.file.hasChildren` | `boolean` | yes |
| `packageDependenciesById.dependencies.indirect[].component.file.mimeType` | `string` | yes |
| `packageDependenciesById.dependencies.indirect[].component.file.path` | `string` | yes |
| `packageDependenciesById.dependencies.indirect[].component.file.permissions` | `string` | yes |
| `packageDependenciesById.dependencies.indirect[].component.file.size` | `integer` | yes |
| `packageDependenciesById.dependencies.indirect[].component.file.updatedAt` | `string` | yes |
| `packageDependenciesById.dependencies.indirect[].component.identificationIds[]` | `string` | yes |
| `packageDependenciesById.dependencies.indirect[].component.identifiers[]` | `object` | yes |
| `packageDependenciesById.dependencies.indirect[].component.identifiers[].type` | `IdentifierFormat` | no |
| `packageDependenciesById.dependencies.indirect[].component.identifiers[].uri` | `string` | no |
| `packageDependenciesById.dependencies.indirect[].component.language[]` | `Language` | yes |
| `packageDependenciesById.dependencies.indirect[].component.license[]` | `string` | yes |
| `packageDependenciesById.dependencies.indirect[].component.name` | `string` | no |
| `packageDependenciesById.dependencies.indirect[].component.namespace` | `string` | yes |
| `packageDependenciesById.dependencies.indirect[].component.operatingSystem` | `string` | yes |
| `packageDependenciesById.dependencies.indirect[].component.operatingSystemKernelVersion` | `string` | yes |
| `packageDependenciesById.dependencies.indirect[].component.package` | `object` | yes |
| `packageDependenciesById.dependencies.indirect[].component.package.language[]` | `Language` | yes |
| `packageDependenciesById.dependencies.indirect[].component.package.license` | `string` | yes |
| `packageDependenciesById.dependencies.indirect[].component.package.name` | `string` | no |
| `packageDependenciesById.dependencies.indirect[].component.package.summary` | `string` | yes |
| `packageDependenciesById.dependencies.indirect[].component.package.type` | `string` | yes |
| `packageDependenciesById.dependencies.indirect[].component.path` | `string` | yes |
| `packageDependenciesById.dependencies.indirect[].component.product` | `string` | yes |
| `packageDependenciesById.dependencies.indirect[].component.purls[]` | `string` | yes |
| `packageDependenciesById.dependencies.indirect[].component.sbomDependenciesCount` | `integer` | yes |
| `packageDependenciesById.dependencies.indirect[].component.subtype` | `ComponentSubType` | yes |
| `packageDependenciesById.dependencies.indirect[].component.type` | `ComponentType` | no |
| `packageDependenciesById.dependencies.indirect[].component.vendor` | `string` | yes |
| `packageDependenciesById.dependencies.indirect[].component.version` | `object` | yes |
| `packageDependenciesById.dependencies.indirect[].component.version.id` | `string` | yes |
| `packageDependenciesById.dependencies.indirect[].component.version.alternatives[]` | `string` | yes |
| `packageDependenciesById.dependencies.indirect[].component.version.isConcrete` | `boolean` | no |
| `packageDependenciesById.dependencies.indirect[].isConcrete` | `boolean` | no |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    packageDependenciesByIdInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_package_dependencies_by_id(package_dependencies_by_id_args=packageDependenciesByIdInput(composed_asset_id='composed_asset_123'))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
