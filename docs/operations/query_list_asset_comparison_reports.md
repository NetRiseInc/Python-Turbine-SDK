<!-- Generated file: do not edit by hand -->

# query_list_asset_comparison_reports

List all asset comparison reports with pagination, filtering, and sorting.

## Parameters

| name | type | required |
| --- | --- | --- |
| `list_asset_comparison_reports_args` | `ListAssetComparisonReportsInput` | `true` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `listAssetComparisonReports` | `object` | no |
| `listAssetComparisonReports.edges[]` | `object` | no |
| `listAssetComparisonReports.edges[].cursor` | `string` | no |
| `listAssetComparisonReports.edges[].node` | `object` | no |
| `listAssetComparisonReports.edges[].node.assetAInfo` | `object` | yes |
| `listAssetComparisonReports.edges[].node.assetAInfo.analysisCreatedAt` | `string` | yes |
| `listAssetComparisonReports.edges[].node.assetAInfo.analysisId` | `string` | yes |
| `listAssetComparisonReports.edges[].node.assetAInfo.assetCreatedAt` | `string` | yes |
| `listAssetComparisonReports.edges[].node.assetAInfo.assetId` | `string` | yes |
| `listAssetComparisonReports.edges[].node.assetAInfo.assetType` | `string` | yes |
| `listAssetComparisonReports.edges[].node.assetAInfo.name` | `string` | yes |
| `listAssetComparisonReports.edges[].node.assetAInfo.orgId` | `string` | yes |
| `listAssetComparisonReports.edges[].node.assetAInfo.product` | `string` | yes |
| `listAssetComparisonReports.edges[].node.assetAInfo.uploadedBy` | `string` | yes |
| `listAssetComparisonReports.edges[].node.assetAInfo.vendor` | `string` | yes |
| `listAssetComparisonReports.edges[].node.assetAInfo.version` | `string` | yes |
| `listAssetComparisonReports.edges[].node.assetBInfo` | `object` | yes |
| `listAssetComparisonReports.edges[].node.assetBInfo.analysisCreatedAt` | `string` | yes |
| `listAssetComparisonReports.edges[].node.assetBInfo.analysisId` | `string` | yes |
| `listAssetComparisonReports.edges[].node.assetBInfo.assetCreatedAt` | `string` | yes |
| `listAssetComparisonReports.edges[].node.assetBInfo.assetId` | `string` | yes |
| `listAssetComparisonReports.edges[].node.assetBInfo.assetType` | `string` | yes |
| `listAssetComparisonReports.edges[].node.assetBInfo.name` | `string` | yes |
| `listAssetComparisonReports.edges[].node.assetBInfo.orgId` | `string` | yes |
| `listAssetComparisonReports.edges[].node.assetBInfo.product` | `string` | yes |
| `listAssetComparisonReports.edges[].node.assetBInfo.uploadedBy` | `string` | yes |
| `listAssetComparisonReports.edges[].node.assetBInfo.vendor` | `string` | yes |
| `listAssetComparisonReports.edges[].node.assetBInfo.version` | `string` | yes |
| `listAssetComparisonReports.edges[].node.comparisonReportSummary` | `object` | yes |
| `listAssetComparisonReports.edges[].node.comparisonReportSummary.assetACredentialsSummary` | `object` | yes |
| `listAssetComparisonReports.edges[].node.comparisonReportSummary.assetACredentialsSummary.totalCrackedAccounts` | `integer` | yes |
| `listAssetComparisonReports.edges[].node.comparisonReportSummary.assetACredentialsSummary.totalCrackedHashes` | `integer` | yes |
| `listAssetComparisonReports.edges[].node.comparisonReportSummary.assetACredentialsSummary.totalExposedSecrets` | `integer` | yes |
| `listAssetComparisonReports.edges[].node.comparisonReportSummary.assetACryptographySummary` | `object` | yes |
| `listAssetComparisonReports.edges[].node.comparisonReportSummary.assetACryptographySummary.totalFailed` | `integer` | yes |
| `listAssetComparisonReports.edges[].node.comparisonReportSummary.assetACryptographySummary.totalNotApplicable` | `integer` | yes |
| `listAssetComparisonReports.edges[].node.comparisonReportSummary.assetACryptographySummary.totalPassed` | `integer` | yes |
| `listAssetComparisonReports.edges[].node.comparisonReportSummary.assetALicenseIssueSummary` | `object` | yes |
| `listAssetComparisonReports.edges[].node.comparisonReportSummary.assetALicenseIssueSummary.totalCopyleft` | `integer` | yes |
| `listAssetComparisonReports.edges[].node.comparisonReportSummary.assetALicenseIssueSummary.totalLicenses` | `integer` | yes |
| `listAssetComparisonReports.edges[].node.comparisonReportSummary.assetALicenseIssueSummary.totalRelationalConflict` | `integer` | yes |
| `listAssetComparisonReports.edges[].node.comparisonReportSummary.assetAMisconfigurationsSummary` | `object` | yes |
| `listAssetComparisonReports.edges[].node.comparisonReportSummary.assetAMisconfigurationsSummary.totalFailed` | `integer` | yes |
| `listAssetComparisonReports.edges[].node.comparisonReportSummary.assetAMisconfigurationsSummary.totalPassed` | `integer` | yes |
| `listAssetComparisonReports.edges[].node.comparisonReportSummary.assetAVulnerabilitySummary` | `object` | yes |
| `listAssetComparisonReports.edges[].node.comparisonReportSummary.assetAVulnerabilitySummary.totalCritical` | `integer` | yes |
| `listAssetComparisonReports.edges[].node.comparisonReportSummary.assetAVulnerabilitySummary.totalHigh` | `integer` | yes |
| `listAssetComparisonReports.edges[].node.comparisonReportSummary.assetAVulnerabilitySummary.totalKev` | `integer` | yes |
| `listAssetComparisonReports.edges[].node.comparisonReportSummary.assetAVulnerabilitySummary.totalLow` | `integer` | yes |
| `listAssetComparisonReports.edges[].node.comparisonReportSummary.assetAVulnerabilitySummary.totalMedium` | `integer` | yes |
| `listAssetComparisonReports.edges[].node.comparisonReportSummary.assetAVulnerabilitySummary.totalPoc` | `integer` | yes |
| `listAssetComparisonReports.edges[].node.comparisonReportSummary.assetAVulnerabilitySummary.totalReachable` | `integer` | yes |
| `listAssetComparisonReports.edges[].node.comparisonReportSummary.assetAVulnerabilitySummary.totalWeaponized` | `integer` | yes |
| `listAssetComparisonReports.edges[].node.comparisonReportSummary.assetBCredentialsSummary` | `object` | yes |
| `listAssetComparisonReports.edges[].node.comparisonReportSummary.assetBCredentialsSummary.totalCrackedAccounts` | `integer` | yes |
| `listAssetComparisonReports.edges[].node.comparisonReportSummary.assetBCredentialsSummary.totalCrackedHashes` | `integer` | yes |
| `listAssetComparisonReports.edges[].node.comparisonReportSummary.assetBCredentialsSummary.totalExposedSecrets` | `integer` | yes |
| `listAssetComparisonReports.edges[].node.comparisonReportSummary.assetBCryptographySummary` | `object` | yes |
| `listAssetComparisonReports.edges[].node.comparisonReportSummary.assetBCryptographySummary.totalFailed` | `integer` | yes |
| `listAssetComparisonReports.edges[].node.comparisonReportSummary.assetBCryptographySummary.totalNotApplicable` | `integer` | yes |
| `listAssetComparisonReports.edges[].node.comparisonReportSummary.assetBCryptographySummary.totalPassed` | `integer` | yes |
| `listAssetComparisonReports.edges[].node.comparisonReportSummary.assetBLicenseIssueSummary` | `object` | yes |
| `listAssetComparisonReports.edges[].node.comparisonReportSummary.assetBLicenseIssueSummary.totalCopyleft` | `integer` | yes |
| `listAssetComparisonReports.edges[].node.comparisonReportSummary.assetBLicenseIssueSummary.totalLicenses` | `integer` | yes |
| `listAssetComparisonReports.edges[].node.comparisonReportSummary.assetBLicenseIssueSummary.totalRelationalConflict` | `integer` | yes |
| `listAssetComparisonReports.edges[].node.comparisonReportSummary.assetBMisconfigurationsSummary` | `object` | yes |
| `listAssetComparisonReports.edges[].node.comparisonReportSummary.assetBMisconfigurationsSummary.totalFailed` | `integer` | yes |
| `listAssetComparisonReports.edges[].node.comparisonReportSummary.assetBMisconfigurationsSummary.totalPassed` | `integer` | yes |
| `listAssetComparisonReports.edges[].node.comparisonReportSummary.assetBVulnerabilitySummary` | `object` | yes |
| `listAssetComparisonReports.edges[].node.comparisonReportSummary.assetBVulnerabilitySummary.totalCritical` | `integer` | yes |
| `listAssetComparisonReports.edges[].node.comparisonReportSummary.assetBVulnerabilitySummary.totalHigh` | `integer` | yes |
| `listAssetComparisonReports.edges[].node.comparisonReportSummary.assetBVulnerabilitySummary.totalKev` | `integer` | yes |
| `listAssetComparisonReports.edges[].node.comparisonReportSummary.assetBVulnerabilitySummary.totalLow` | `integer` | yes |
| `listAssetComparisonReports.edges[].node.comparisonReportSummary.assetBVulnerabilitySummary.totalMedium` | `integer` | yes |
| `listAssetComparisonReports.edges[].node.comparisonReportSummary.assetBVulnerabilitySummary.totalPoc` | `integer` | yes |
| `listAssetComparisonReports.edges[].node.comparisonReportSummary.assetBVulnerabilitySummary.totalReachable` | `integer` | yes |
| `listAssetComparisonReports.edges[].node.comparisonReportSummary.assetBVulnerabilitySummary.totalWeaponized` | `integer` | yes |
| `listAssetComparisonReports.edges[].node.comparisonReportSummary.inventoryComparisonSummary` | `object` | yes |
| `listAssetComparisonReports.edges[].node.comparisonReportSummary.inventoryComparisonSummary.binariesInANotInB` | `integer` | yes |
| `listAssetComparisonReports.edges[].node.comparisonReportSummary.inventoryComparisonSummary.binariesInBNotInA` | `integer` | yes |
| `listAssetComparisonReports.edges[].node.comparisonReportSummary.inventoryComparisonSummary.componentsInANotInB` | `integer` | yes |
| `listAssetComparisonReports.edges[].node.comparisonReportSummary.inventoryComparisonSummary.componentsInBNotInA` | `integer` | yes |
| `listAssetComparisonReports.edges[].node.comparisonReportSummary.inventoryComparisonSummary.filesInANotInB` | `integer` | yes |
| `listAssetComparisonReports.edges[].node.comparisonReportSummary.inventoryComparisonSummary.filesInBNotInA` | `integer` | yes |
| `listAssetComparisonReports.edges[].node.comparisonReportSummary.inventoryComparisonSummary.licensesInANotInB` | `integer` | yes |
| `listAssetComparisonReports.edges[].node.comparisonReportSummary.inventoryComparisonSummary.licensesInBNotInA` | `integer` | yes |
| `listAssetComparisonReports.edges[].node.comparisonReportSummary.inventoryComparisonSummary.totalOverlappingBinaries` | `integer` | yes |
| `listAssetComparisonReports.edges[].node.comparisonReportSummary.inventoryComparisonSummary.totalOverlappingComponents` | `integer` | yes |
| `listAssetComparisonReports.edges[].node.comparisonReportSummary.inventoryComparisonSummary.totalOverlappingFiles` | `integer` | yes |
| `listAssetComparisonReports.edges[].node.comparisonReportSummary.inventoryComparisonSummary.totalOverlappingLicenses` | `integer` | yes |
| `listAssetComparisonReports.edges[].node.completedAt` | `string` | yes |
| `listAssetComparisonReports.edges[].node.componentDiff` | `object` | yes |
| `listAssetComparisonReports.edges[].node.componentDiff.assetATypeCounts` | `object` | yes |
| `listAssetComparisonReports.edges[].node.componentDiff.assetATypeCounts.aiModel` | `integer` | no |
| `listAssetComparisonReports.edges[].node.componentDiff.assetATypeCounts.application` | `integer` | no |
| `listAssetComparisonReports.edges[].node.componentDiff.assetATypeCounts.container` | `integer` | no |
| `listAssetComparisonReports.edges[].node.componentDiff.assetATypeCounts.device` | `integer` | no |
| `listAssetComparisonReports.edges[].node.componentDiff.assetATypeCounts.framework` | `integer` | no |
| `listAssetComparisonReports.edges[].node.componentDiff.assetATypeCounts.kernel` | `integer` | no |
| `listAssetComparisonReports.edges[].node.componentDiff.assetATypeCounts.kernelModule` | `integer` | no |
| `listAssetComparisonReports.edges[].node.componentDiff.assetATypeCounts.library` | `integer` | no |
| `listAssetComparisonReports.edges[].node.componentDiff.assetATypeCounts.os` | `integer` | no |
| `listAssetComparisonReports.edges[].node.componentDiff.assetATypeCounts.package` | `integer` | no |
| `listAssetComparisonReports.edges[].node.componentDiff.assetBTypeCounts` | `object` | yes |
| `listAssetComparisonReports.edges[].node.componentDiff.assetBTypeCounts.aiModel` | `integer` | no |
| `listAssetComparisonReports.edges[].node.componentDiff.assetBTypeCounts.application` | `integer` | no |
| `listAssetComparisonReports.edges[].node.componentDiff.assetBTypeCounts.container` | `integer` | no |
| `listAssetComparisonReports.edges[].node.componentDiff.assetBTypeCounts.device` | `integer` | no |
| `listAssetComparisonReports.edges[].node.componentDiff.assetBTypeCounts.framework` | `integer` | no |
| `listAssetComparisonReports.edges[].node.componentDiff.assetBTypeCounts.kernel` | `integer` | no |
| `listAssetComparisonReports.edges[].node.componentDiff.assetBTypeCounts.kernelModule` | `integer` | no |
| `listAssetComparisonReports.edges[].node.componentDiff.assetBTypeCounts.library` | `integer` | no |
| `listAssetComparisonReports.edges[].node.componentDiff.assetBTypeCounts.os` | `integer` | no |
| `listAssetComparisonReports.edges[].node.componentDiff.assetBTypeCounts.package` | `integer` | no |
| `listAssetComparisonReports.edges[].node.componentDiff.inANotInB[]` | `object` | yes |
| `listAssetComparisonReports.edges[].node.componentDiff.inANotInB[].criticalSevs` | `integer` | yes |
| `listAssetComparisonReports.edges[].node.componentDiff.inANotInB[].highSevs` | `integer` | yes |
| `listAssetComparisonReports.edges[].node.componentDiff.inANotInB[].licenses[]` | `string` | yes |
| `listAssetComparisonReports.edges[].node.componentDiff.inANotInB[].lowSevs` | `integer` | yes |
| `listAssetComparisonReports.edges[].node.componentDiff.inANotInB[].mediumSevs` | `integer` | yes |
| `listAssetComparisonReports.edges[].node.componentDiff.inANotInB[].name` | `string` | yes |
| `listAssetComparisonReports.edges[].node.componentDiff.inANotInB[].packageType` | `string` | yes |
| `listAssetComparisonReports.edges[].node.componentDiff.inANotInB[].reachable` | `boolean` | yes |
| `listAssetComparisonReports.edges[].node.componentDiff.inANotInB[].totalVulns` | `integer` | yes |
| `listAssetComparisonReports.edges[].node.componentDiff.inANotInB[].type` | `string` | yes |
| `listAssetComparisonReports.edges[].node.componentDiff.inANotInB[].version` | `string` | yes |
| `listAssetComparisonReports.edges[].node.componentDiff.inANotInBReachableCount` | `integer` | yes |
| `listAssetComparisonReports.edges[].node.componentDiff.inBNotInA[]` | `object` | yes |
| `listAssetComparisonReports.edges[].node.componentDiff.inBNotInA[].criticalSevs` | `integer` | yes |
| `listAssetComparisonReports.edges[].node.componentDiff.inBNotInA[].highSevs` | `integer` | yes |
| `listAssetComparisonReports.edges[].node.componentDiff.inBNotInA[].licenses[]` | `string` | yes |
| `listAssetComparisonReports.edges[].node.componentDiff.inBNotInA[].lowSevs` | `integer` | yes |
| `listAssetComparisonReports.edges[].node.componentDiff.inBNotInA[].mediumSevs` | `integer` | yes |
| `listAssetComparisonReports.edges[].node.componentDiff.inBNotInA[].name` | `string` | yes |
| `listAssetComparisonReports.edges[].node.componentDiff.inBNotInA[].packageType` | `string` | yes |
| `listAssetComparisonReports.edges[].node.componentDiff.inBNotInA[].reachable` | `boolean` | yes |
| `listAssetComparisonReports.edges[].node.componentDiff.inBNotInA[].totalVulns` | `integer` | yes |
| `listAssetComparisonReports.edges[].node.componentDiff.inBNotInA[].type` | `string` | yes |
| `listAssetComparisonReports.edges[].node.componentDiff.inBNotInA[].version` | `string` | yes |
| `listAssetComparisonReports.edges[].node.componentDiff.inBNotInAReachableCount` | `integer` | yes |
| `listAssetComparisonReports.edges[].node.componentDiff.overlap[]` | `object` | yes |
| `listAssetComparisonReports.edges[].node.componentDiff.overlap[].criticalSevs` | `integer` | yes |
| `listAssetComparisonReports.edges[].node.componentDiff.overlap[].highSevs` | `integer` | yes |
| `listAssetComparisonReports.edges[].node.componentDiff.overlap[].licenses[]` | `string` | yes |
| `listAssetComparisonReports.edges[].node.componentDiff.overlap[].lowSevs` | `integer` | yes |
| `listAssetComparisonReports.edges[].node.componentDiff.overlap[].mediumSevs` | `integer` | yes |
| `listAssetComparisonReports.edges[].node.componentDiff.overlap[].name` | `string` | yes |
| `listAssetComparisonReports.edges[].node.componentDiff.overlap[].packageType` | `string` | yes |
| `listAssetComparisonReports.edges[].node.componentDiff.overlap[].reachable` | `boolean` | yes |
| `listAssetComparisonReports.edges[].node.componentDiff.overlap[].totalVulns` | `integer` | yes |
| `listAssetComparisonReports.edges[].node.componentDiff.overlap[].type` | `string` | yes |
| `listAssetComparisonReports.edges[].node.componentDiff.overlap[].version` | `string` | yes |
| `listAssetComparisonReports.edges[].node.componentDiff.overlapReachableCount` | `integer` | yes |
| `listAssetComparisonReports.edges[].node.createdAt` | `string` | yes |
| `listAssetComparisonReports.edges[].node.createdBy` | `string` | yes |
| `listAssetComparisonReports.edges[].node.reportId` | `string` | no |
| `listAssetComparisonReports.edges[].node.riverJobId` | `string` | yes |
| `listAssetComparisonReports.edges[].node.vulnerabilityDiff` | `object` | yes |
| `listAssetComparisonReports.edges[].node.vulnerabilityDiff.assetVulnerabilityRemediationDiff` | `object` | yes |
| `listAssetComparisonReports.edges[].node.vulnerabilityDiff.assetVulnerabilityRemediationDiff.totalResolvedA` | `integer` | yes |
| `listAssetComparisonReports.edges[].node.vulnerabilityDiff.assetVulnerabilityRemediationDiff.totalResolvedANotPresentInB` | `integer` | yes |
| `listAssetComparisonReports.edges[].node.vulnerabilityDiff.assetVulnerabilityRemediationDiff.totalResolvedB` | `integer` | yes |
| `listAssetComparisonReports.edges[].node.vulnerabilityDiff.assetVulnerabilityRemediationDiff.totalResolvedBNotPresentInA` | `integer` | yes |
| `listAssetComparisonReports.edges[].node.vulnerabilityDiff.assetVulnerabilityRemediationDiff.totalResolvedInAPresentInB` | `integer` | yes |
| `listAssetComparisonReports.edges[].node.vulnerabilityDiff.assetVulnerabilityRemediationDiff.totalResolvedInBPresentInA` | `integer` | yes |
| `listAssetComparisonReports.edges[].node.vulnerabilityDiff.assetVulnerabilityRemediationDiff.totalTrackedA` | `integer` | yes |
| `listAssetComparisonReports.edges[].node.vulnerabilityDiff.assetVulnerabilityRemediationDiff.totalTrackedB` | `integer` | yes |
| `listAssetComparisonReports.edges[].node.vulnerabilityDiff.inANotInB[]` | `object` | yes |
| `listAssetComparisonReports.edges[].node.vulnerabilityDiff.inANotInB[].cisaKev` | `boolean` | yes |
| `listAssetComparisonReports.edges[].node.vulnerabilityDiff.inANotInB[].componentName` | `string` | yes |
| `listAssetComparisonReports.edges[].node.vulnerabilityDiff.inANotInB[].componentVersion` | `string` | yes |
| `listAssetComparisonReports.edges[].node.vulnerabilityDiff.inANotInB[].cveId` | `string` | yes |
| `listAssetComparisonReports.edges[].node.vulnerabilityDiff.inANotInB[].cvssScore` | `float` | yes |
| `listAssetComparisonReports.edges[].node.vulnerabilityDiff.inANotInB[].exploitMaturity` | `string` | yes |
| `listAssetComparisonReports.edges[].node.vulnerabilityDiff.inANotInB[].reachable` | `boolean` | yes |
| `listAssetComparisonReports.edges[].node.vulnerabilityDiff.inANotInB[].severity` | `string` | yes |
| `listAssetComparisonReports.edges[].node.vulnerabilityDiff.inANotInBKevCount` | `integer` | yes |
| `listAssetComparisonReports.edges[].node.vulnerabilityDiff.inANotInBReachableCount` | `integer` | yes |
| `listAssetComparisonReports.edges[].node.vulnerabilityDiff.inBNotInA[]` | `object` | yes |
| `listAssetComparisonReports.edges[].node.vulnerabilityDiff.inBNotInA[].cisaKev` | `boolean` | yes |
| `listAssetComparisonReports.edges[].node.vulnerabilityDiff.inBNotInA[].componentName` | `string` | yes |
| `listAssetComparisonReports.edges[].node.vulnerabilityDiff.inBNotInA[].componentVersion` | `string` | yes |
| `listAssetComparisonReports.edges[].node.vulnerabilityDiff.inBNotInA[].cveId` | `string` | yes |
| `listAssetComparisonReports.edges[].node.vulnerabilityDiff.inBNotInA[].cvssScore` | `float` | yes |
| `listAssetComparisonReports.edges[].node.vulnerabilityDiff.inBNotInA[].exploitMaturity` | `string` | yes |
| `listAssetComparisonReports.edges[].node.vulnerabilityDiff.inBNotInA[].reachable` | `boolean` | yes |
| `listAssetComparisonReports.edges[].node.vulnerabilityDiff.inBNotInA[].severity` | `string` | yes |
| `listAssetComparisonReports.edges[].node.vulnerabilityDiff.inBNotInAKevCount` | `integer` | yes |
| `listAssetComparisonReports.edges[].node.vulnerabilityDiff.inBNotInAReachableCount` | `integer` | yes |
| `listAssetComparisonReports.edges[].node.vulnerabilityDiff.overlap[]` | `object` | yes |
| `listAssetComparisonReports.edges[].node.vulnerabilityDiff.overlap[].cisaKev` | `boolean` | yes |
| `listAssetComparisonReports.edges[].node.vulnerabilityDiff.overlap[].componentName` | `string` | yes |
| `listAssetComparisonReports.edges[].node.vulnerabilityDiff.overlap[].componentVersion` | `string` | yes |
| `listAssetComparisonReports.edges[].node.vulnerabilityDiff.overlap[].cveId` | `string` | yes |
| `listAssetComparisonReports.edges[].node.vulnerabilityDiff.overlap[].cvssScore` | `float` | yes |
| `listAssetComparisonReports.edges[].node.vulnerabilityDiff.overlap[].exploitMaturity` | `string` | yes |
| `listAssetComparisonReports.edges[].node.vulnerabilityDiff.overlap[].reachable` | `boolean` | yes |
| `listAssetComparisonReports.edges[].node.vulnerabilityDiff.overlap[].severity` | `string` | yes |
| `listAssetComparisonReports.edges[].node.vulnerabilityDiff.overlapKevCount` | `integer` | yes |
| `listAssetComparisonReports.edges[].node.vulnerabilityDiff.overlapReachableCount` | `integer` | yes |
| `listAssetComparisonReports.pageInfo` | `object` | no |
| `listAssetComparisonReports.pageInfo.endCursor` | `string` | yes |
| `listAssetComparisonReports.pageInfo.hasNextPage` | `boolean` | no |
| `listAssetComparisonReports.pageInfo.hasPreviousPage` | `boolean` | no |
| `listAssetComparisonReports.pageInfo.startCursor` | `string` | yes |
| `listAssetComparisonReports.pageInfo.totalCount` | `integer` | yes |
| `listAssetComparisonReports.totalCount` | `integer` | no |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    ListAssetComparisonReportsInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_list_asset_comparison_reports(list_asset_comparison_reports_args=ListAssetComparisonReportsInput())
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
