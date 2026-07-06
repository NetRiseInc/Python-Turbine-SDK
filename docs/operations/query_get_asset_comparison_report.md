<!-- Generated file: do not edit by hand -->

# query_get_asset_comparison_report

Retrieve a completed asset comparison report including vulnerability, component, and summary diffs.

## Parameters

| name | type | required |
| --- | --- | --- |
| `get_asset_comparison_report_args` | `GetAssetComparisonReportInput` | `true` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `getAssetComparisonReport` | `object` | yes |
| `getAssetComparisonReport.assetAInfo` | `object` | yes |
| `getAssetComparisonReport.assetAInfo.analysisCreatedAt` | `string` | yes |
| `getAssetComparisonReport.assetAInfo.analysisId` | `string` | yes |
| `getAssetComparisonReport.assetAInfo.assetCreatedAt` | `string` | yes |
| `getAssetComparisonReport.assetAInfo.assetId` | `string` | yes |
| `getAssetComparisonReport.assetAInfo.assetType` | `string` | yes |
| `getAssetComparisonReport.assetAInfo.name` | `string` | yes |
| `getAssetComparisonReport.assetAInfo.orgId` | `string` | yes |
| `getAssetComparisonReport.assetAInfo.product` | `string` | yes |
| `getAssetComparisonReport.assetAInfo.uploadedBy` | `string` | yes |
| `getAssetComparisonReport.assetAInfo.vendor` | `string` | yes |
| `getAssetComparisonReport.assetAInfo.version` | `string` | yes |
| `getAssetComparisonReport.assetBInfo` | `object` | yes |
| `getAssetComparisonReport.assetBInfo.analysisCreatedAt` | `string` | yes |
| `getAssetComparisonReport.assetBInfo.analysisId` | `string` | yes |
| `getAssetComparisonReport.assetBInfo.assetCreatedAt` | `string` | yes |
| `getAssetComparisonReport.assetBInfo.assetId` | `string` | yes |
| `getAssetComparisonReport.assetBInfo.assetType` | `string` | yes |
| `getAssetComparisonReport.assetBInfo.name` | `string` | yes |
| `getAssetComparisonReport.assetBInfo.orgId` | `string` | yes |
| `getAssetComparisonReport.assetBInfo.product` | `string` | yes |
| `getAssetComparisonReport.assetBInfo.uploadedBy` | `string` | yes |
| `getAssetComparisonReport.assetBInfo.vendor` | `string` | yes |
| `getAssetComparisonReport.assetBInfo.version` | `string` | yes |
| `getAssetComparisonReport.comparisonReportSummary` | `object` | yes |
| `getAssetComparisonReport.comparisonReportSummary.assetACredentialsSummary` | `object` | yes |
| `getAssetComparisonReport.comparisonReportSummary.assetACredentialsSummary.totalCrackedAccounts` | `integer` | yes |
| `getAssetComparisonReport.comparisonReportSummary.assetACredentialsSummary.totalCrackedHashes` | `integer` | yes |
| `getAssetComparisonReport.comparisonReportSummary.assetACredentialsSummary.totalExposedSecrets` | `integer` | yes |
| `getAssetComparisonReport.comparisonReportSummary.assetACryptographySummary` | `object` | yes |
| `getAssetComparisonReport.comparisonReportSummary.assetACryptographySummary.totalFailed` | `integer` | yes |
| `getAssetComparisonReport.comparisonReportSummary.assetACryptographySummary.totalNotApplicable` | `integer` | yes |
| `getAssetComparisonReport.comparisonReportSummary.assetACryptographySummary.totalPassed` | `integer` | yes |
| `getAssetComparisonReport.comparisonReportSummary.assetALicenseIssueSummary` | `object` | yes |
| `getAssetComparisonReport.comparisonReportSummary.assetALicenseIssueSummary.totalCopyleft` | `integer` | yes |
| `getAssetComparisonReport.comparisonReportSummary.assetALicenseIssueSummary.totalLicenses` | `integer` | yes |
| `getAssetComparisonReport.comparisonReportSummary.assetALicenseIssueSummary.totalRelationalConflict` | `integer` | yes |
| `getAssetComparisonReport.comparisonReportSummary.assetAMisconfigurationsSummary` | `object` | yes |
| `getAssetComparisonReport.comparisonReportSummary.assetAMisconfigurationsSummary.totalFailed` | `integer` | yes |
| `getAssetComparisonReport.comparisonReportSummary.assetAMisconfigurationsSummary.totalPassed` | `integer` | yes |
| `getAssetComparisonReport.comparisonReportSummary.assetAVulnerabilitySummary` | `object` | yes |
| `getAssetComparisonReport.comparisonReportSummary.assetAVulnerabilitySummary.totalCritical` | `integer` | yes |
| `getAssetComparisonReport.comparisonReportSummary.assetAVulnerabilitySummary.totalHigh` | `integer` | yes |
| `getAssetComparisonReport.comparisonReportSummary.assetAVulnerabilitySummary.totalKev` | `integer` | yes |
| `getAssetComparisonReport.comparisonReportSummary.assetAVulnerabilitySummary.totalLow` | `integer` | yes |
| `getAssetComparisonReport.comparisonReportSummary.assetAVulnerabilitySummary.totalMedium` | `integer` | yes |
| `getAssetComparisonReport.comparisonReportSummary.assetAVulnerabilitySummary.totalPoc` | `integer` | yes |
| `getAssetComparisonReport.comparisonReportSummary.assetAVulnerabilitySummary.totalReachable` | `integer` | yes |
| `getAssetComparisonReport.comparisonReportSummary.assetAVulnerabilitySummary.totalWeaponized` | `integer` | yes |
| `getAssetComparisonReport.comparisonReportSummary.assetBCredentialsSummary` | `object` | yes |
| `getAssetComparisonReport.comparisonReportSummary.assetBCredentialsSummary.totalCrackedAccounts` | `integer` | yes |
| `getAssetComparisonReport.comparisonReportSummary.assetBCredentialsSummary.totalCrackedHashes` | `integer` | yes |
| `getAssetComparisonReport.comparisonReportSummary.assetBCredentialsSummary.totalExposedSecrets` | `integer` | yes |
| `getAssetComparisonReport.comparisonReportSummary.assetBCryptographySummary` | `object` | yes |
| `getAssetComparisonReport.comparisonReportSummary.assetBCryptographySummary.totalFailed` | `integer` | yes |
| `getAssetComparisonReport.comparisonReportSummary.assetBCryptographySummary.totalNotApplicable` | `integer` | yes |
| `getAssetComparisonReport.comparisonReportSummary.assetBCryptographySummary.totalPassed` | `integer` | yes |
| `getAssetComparisonReport.comparisonReportSummary.assetBLicenseIssueSummary` | `object` | yes |
| `getAssetComparisonReport.comparisonReportSummary.assetBLicenseIssueSummary.totalCopyleft` | `integer` | yes |
| `getAssetComparisonReport.comparisonReportSummary.assetBLicenseIssueSummary.totalLicenses` | `integer` | yes |
| `getAssetComparisonReport.comparisonReportSummary.assetBLicenseIssueSummary.totalRelationalConflict` | `integer` | yes |
| `getAssetComparisonReport.comparisonReportSummary.assetBMisconfigurationsSummary` | `object` | yes |
| `getAssetComparisonReport.comparisonReportSummary.assetBMisconfigurationsSummary.totalFailed` | `integer` | yes |
| `getAssetComparisonReport.comparisonReportSummary.assetBMisconfigurationsSummary.totalPassed` | `integer` | yes |
| `getAssetComparisonReport.comparisonReportSummary.assetBVulnerabilitySummary` | `object` | yes |
| `getAssetComparisonReport.comparisonReportSummary.assetBVulnerabilitySummary.totalCritical` | `integer` | yes |
| `getAssetComparisonReport.comparisonReportSummary.assetBVulnerabilitySummary.totalHigh` | `integer` | yes |
| `getAssetComparisonReport.comparisonReportSummary.assetBVulnerabilitySummary.totalKev` | `integer` | yes |
| `getAssetComparisonReport.comparisonReportSummary.assetBVulnerabilitySummary.totalLow` | `integer` | yes |
| `getAssetComparisonReport.comparisonReportSummary.assetBVulnerabilitySummary.totalMedium` | `integer` | yes |
| `getAssetComparisonReport.comparisonReportSummary.assetBVulnerabilitySummary.totalPoc` | `integer` | yes |
| `getAssetComparisonReport.comparisonReportSummary.assetBVulnerabilitySummary.totalReachable` | `integer` | yes |
| `getAssetComparisonReport.comparisonReportSummary.assetBVulnerabilitySummary.totalWeaponized` | `integer` | yes |
| `getAssetComparisonReport.comparisonReportSummary.inventoryComparisonSummary` | `object` | yes |
| `getAssetComparisonReport.comparisonReportSummary.inventoryComparisonSummary.binariesInANotInB` | `integer` | yes |
| `getAssetComparisonReport.comparisonReportSummary.inventoryComparisonSummary.binariesInBNotInA` | `integer` | yes |
| `getAssetComparisonReport.comparisonReportSummary.inventoryComparisonSummary.componentsInANotInB` | `integer` | yes |
| `getAssetComparisonReport.comparisonReportSummary.inventoryComparisonSummary.componentsInBNotInA` | `integer` | yes |
| `getAssetComparisonReport.comparisonReportSummary.inventoryComparisonSummary.filesInANotInB` | `integer` | yes |
| `getAssetComparisonReport.comparisonReportSummary.inventoryComparisonSummary.filesInBNotInA` | `integer` | yes |
| `getAssetComparisonReport.comparisonReportSummary.inventoryComparisonSummary.licensesInANotInB` | `integer` | yes |
| `getAssetComparisonReport.comparisonReportSummary.inventoryComparisonSummary.licensesInBNotInA` | `integer` | yes |
| `getAssetComparisonReport.comparisonReportSummary.inventoryComparisonSummary.totalOverlappingBinaries` | `integer` | yes |
| `getAssetComparisonReport.comparisonReportSummary.inventoryComparisonSummary.totalOverlappingComponents` | `integer` | yes |
| `getAssetComparisonReport.comparisonReportSummary.inventoryComparisonSummary.totalOverlappingFiles` | `integer` | yes |
| `getAssetComparisonReport.comparisonReportSummary.inventoryComparisonSummary.totalOverlappingLicenses` | `integer` | yes |
| `getAssetComparisonReport.completedAt` | `string` | yes |
| `getAssetComparisonReport.componentDiff` | `object` | yes |
| `getAssetComparisonReport.componentDiff.assetATypeCounts` | `object` | yes |
| `getAssetComparisonReport.componentDiff.assetATypeCounts.aiModel` | `integer` | no |
| `getAssetComparisonReport.componentDiff.assetATypeCounts.application` | `integer` | no |
| `getAssetComparisonReport.componentDiff.assetATypeCounts.container` | `integer` | no |
| `getAssetComparisonReport.componentDiff.assetATypeCounts.device` | `integer` | no |
| `getAssetComparisonReport.componentDiff.assetATypeCounts.framework` | `integer` | no |
| `getAssetComparisonReport.componentDiff.assetATypeCounts.kernel` | `integer` | no |
| `getAssetComparisonReport.componentDiff.assetATypeCounts.kernelModule` | `integer` | no |
| `getAssetComparisonReport.componentDiff.assetATypeCounts.library` | `integer` | no |
| `getAssetComparisonReport.componentDiff.assetATypeCounts.os` | `integer` | no |
| `getAssetComparisonReport.componentDiff.assetATypeCounts.package` | `integer` | no |
| `getAssetComparisonReport.componentDiff.assetBTypeCounts` | `object` | yes |
| `getAssetComparisonReport.componentDiff.assetBTypeCounts.aiModel` | `integer` | no |
| `getAssetComparisonReport.componentDiff.assetBTypeCounts.application` | `integer` | no |
| `getAssetComparisonReport.componentDiff.assetBTypeCounts.container` | `integer` | no |
| `getAssetComparisonReport.componentDiff.assetBTypeCounts.device` | `integer` | no |
| `getAssetComparisonReport.componentDiff.assetBTypeCounts.framework` | `integer` | no |
| `getAssetComparisonReport.componentDiff.assetBTypeCounts.kernel` | `integer` | no |
| `getAssetComparisonReport.componentDiff.assetBTypeCounts.kernelModule` | `integer` | no |
| `getAssetComparisonReport.componentDiff.assetBTypeCounts.library` | `integer` | no |
| `getAssetComparisonReport.componentDiff.assetBTypeCounts.os` | `integer` | no |
| `getAssetComparisonReport.componentDiff.assetBTypeCounts.package` | `integer` | no |
| `getAssetComparisonReport.componentDiff.inANotInB[]` | `object` | yes |
| `getAssetComparisonReport.componentDiff.inANotInB[].criticalSevs` | `integer` | yes |
| `getAssetComparisonReport.componentDiff.inANotInB[].highSevs` | `integer` | yes |
| `getAssetComparisonReport.componentDiff.inANotInB[].licenses[]` | `string` | yes |
| `getAssetComparisonReport.componentDiff.inANotInB[].lowSevs` | `integer` | yes |
| `getAssetComparisonReport.componentDiff.inANotInB[].mediumSevs` | `integer` | yes |
| `getAssetComparisonReport.componentDiff.inANotInB[].name` | `string` | yes |
| `getAssetComparisonReport.componentDiff.inANotInB[].packageType` | `string` | yes |
| `getAssetComparisonReport.componentDiff.inANotInB[].reachable` | `boolean` | yes |
| `getAssetComparisonReport.componentDiff.inANotInB[].totalVulns` | `integer` | yes |
| `getAssetComparisonReport.componentDiff.inANotInB[].type` | `string` | yes |
| `getAssetComparisonReport.componentDiff.inANotInB[].version` | `string` | yes |
| `getAssetComparisonReport.componentDiff.inANotInBReachableCount` | `integer` | yes |
| `getAssetComparisonReport.componentDiff.inBNotInA[]` | `object` | yes |
| `getAssetComparisonReport.componentDiff.inBNotInA[].criticalSevs` | `integer` | yes |
| `getAssetComparisonReport.componentDiff.inBNotInA[].highSevs` | `integer` | yes |
| `getAssetComparisonReport.componentDiff.inBNotInA[].licenses[]` | `string` | yes |
| `getAssetComparisonReport.componentDiff.inBNotInA[].lowSevs` | `integer` | yes |
| `getAssetComparisonReport.componentDiff.inBNotInA[].mediumSevs` | `integer` | yes |
| `getAssetComparisonReport.componentDiff.inBNotInA[].name` | `string` | yes |
| `getAssetComparisonReport.componentDiff.inBNotInA[].packageType` | `string` | yes |
| `getAssetComparisonReport.componentDiff.inBNotInA[].reachable` | `boolean` | yes |
| `getAssetComparisonReport.componentDiff.inBNotInA[].totalVulns` | `integer` | yes |
| `getAssetComparisonReport.componentDiff.inBNotInA[].type` | `string` | yes |
| `getAssetComparisonReport.componentDiff.inBNotInA[].version` | `string` | yes |
| `getAssetComparisonReport.componentDiff.inBNotInAReachableCount` | `integer` | yes |
| `getAssetComparisonReport.componentDiff.overlap[]` | `object` | yes |
| `getAssetComparisonReport.componentDiff.overlap[].criticalSevs` | `integer` | yes |
| `getAssetComparisonReport.componentDiff.overlap[].highSevs` | `integer` | yes |
| `getAssetComparisonReport.componentDiff.overlap[].licenses[]` | `string` | yes |
| `getAssetComparisonReport.componentDiff.overlap[].lowSevs` | `integer` | yes |
| `getAssetComparisonReport.componentDiff.overlap[].mediumSevs` | `integer` | yes |
| `getAssetComparisonReport.componentDiff.overlap[].name` | `string` | yes |
| `getAssetComparisonReport.componentDiff.overlap[].packageType` | `string` | yes |
| `getAssetComparisonReport.componentDiff.overlap[].reachable` | `boolean` | yes |
| `getAssetComparisonReport.componentDiff.overlap[].totalVulns` | `integer` | yes |
| `getAssetComparisonReport.componentDiff.overlap[].type` | `string` | yes |
| `getAssetComparisonReport.componentDiff.overlap[].version` | `string` | yes |
| `getAssetComparisonReport.componentDiff.overlapReachableCount` | `integer` | yes |
| `getAssetComparisonReport.createdAt` | `string` | yes |
| `getAssetComparisonReport.createdBy` | `string` | yes |
| `getAssetComparisonReport.reportId` | `string` | no |
| `getAssetComparisonReport.riverJobId` | `string` | yes |
| `getAssetComparisonReport.vulnerabilityDiff` | `object` | yes |
| `getAssetComparisonReport.vulnerabilityDiff.assetVulnerabilityRemediationDiff` | `object` | yes |
| `getAssetComparisonReport.vulnerabilityDiff.assetVulnerabilityRemediationDiff.totalResolvedA` | `integer` | yes |
| `getAssetComparisonReport.vulnerabilityDiff.assetVulnerabilityRemediationDiff.totalResolvedANotPresentInB` | `integer` | yes |
| `getAssetComparisonReport.vulnerabilityDiff.assetVulnerabilityRemediationDiff.totalResolvedB` | `integer` | yes |
| `getAssetComparisonReport.vulnerabilityDiff.assetVulnerabilityRemediationDiff.totalResolvedBNotPresentInA` | `integer` | yes |
| `getAssetComparisonReport.vulnerabilityDiff.assetVulnerabilityRemediationDiff.totalResolvedInAPresentInB` | `integer` | yes |
| `getAssetComparisonReport.vulnerabilityDiff.assetVulnerabilityRemediationDiff.totalResolvedInBPresentInA` | `integer` | yes |
| `getAssetComparisonReport.vulnerabilityDiff.assetVulnerabilityRemediationDiff.totalTrackedA` | `integer` | yes |
| `getAssetComparisonReport.vulnerabilityDiff.assetVulnerabilityRemediationDiff.totalTrackedB` | `integer` | yes |
| `getAssetComparisonReport.vulnerabilityDiff.assetVulnerabilityRemediationDiff.vulnerabilitiesMarkedResolvedInA[]` | `object` | yes |
| `getAssetComparisonReport.vulnerabilityDiff.assetVulnerabilityRemediationDiff.vulnerabilitiesMarkedResolvedInA[].cisaKev` | `boolean` | yes |
| `getAssetComparisonReport.vulnerabilityDiff.assetVulnerabilityRemediationDiff.vulnerabilitiesMarkedResolvedInA[].componentName` | `string` | yes |
| `getAssetComparisonReport.vulnerabilityDiff.assetVulnerabilityRemediationDiff.vulnerabilitiesMarkedResolvedInA[].componentVersion` | `string` | yes |
| `getAssetComparisonReport.vulnerabilityDiff.assetVulnerabilityRemediationDiff.vulnerabilitiesMarkedResolvedInA[].cveId` | `string` | yes |
| `getAssetComparisonReport.vulnerabilityDiff.assetVulnerabilityRemediationDiff.vulnerabilitiesMarkedResolvedInA[].cvssScore` | `float` | yes |
| `getAssetComparisonReport.vulnerabilityDiff.assetVulnerabilityRemediationDiff.vulnerabilitiesMarkedResolvedInA[].exploitMaturity` | `string` | yes |
| `getAssetComparisonReport.vulnerabilityDiff.assetVulnerabilityRemediationDiff.vulnerabilitiesMarkedResolvedInA[].reachable` | `boolean` | yes |
| `getAssetComparisonReport.vulnerabilityDiff.assetVulnerabilityRemediationDiff.vulnerabilitiesMarkedResolvedInA[].severity` | `string` | yes |
| `getAssetComparisonReport.vulnerabilityDiff.assetVulnerabilityRemediationDiff.vulnerabilitiesMarkedResolvedInB[]` | `object` | yes |
| `getAssetComparisonReport.vulnerabilityDiff.assetVulnerabilityRemediationDiff.vulnerabilitiesMarkedResolvedInB[].cisaKev` | `boolean` | yes |
| `getAssetComparisonReport.vulnerabilityDiff.assetVulnerabilityRemediationDiff.vulnerabilitiesMarkedResolvedInB[].componentName` | `string` | yes |
| `getAssetComparisonReport.vulnerabilityDiff.assetVulnerabilityRemediationDiff.vulnerabilitiesMarkedResolvedInB[].componentVersion` | `string` | yes |
| `getAssetComparisonReport.vulnerabilityDiff.assetVulnerabilityRemediationDiff.vulnerabilitiesMarkedResolvedInB[].cveId` | `string` | yes |
| `getAssetComparisonReport.vulnerabilityDiff.assetVulnerabilityRemediationDiff.vulnerabilitiesMarkedResolvedInB[].cvssScore` | `float` | yes |
| `getAssetComparisonReport.vulnerabilityDiff.assetVulnerabilityRemediationDiff.vulnerabilitiesMarkedResolvedInB[].exploitMaturity` | `string` | yes |
| `getAssetComparisonReport.vulnerabilityDiff.assetVulnerabilityRemediationDiff.vulnerabilitiesMarkedResolvedInB[].reachable` | `boolean` | yes |
| `getAssetComparisonReport.vulnerabilityDiff.assetVulnerabilityRemediationDiff.vulnerabilitiesMarkedResolvedInB[].severity` | `string` | yes |
| `getAssetComparisonReport.vulnerabilityDiff.assetVulnerabilityRemediationDiff.vulnerabilitiesResolvedInA[]` | `object` | yes |
| `getAssetComparisonReport.vulnerabilityDiff.assetVulnerabilityRemediationDiff.vulnerabilitiesResolvedInA[].cisaKev` | `boolean` | yes |
| `getAssetComparisonReport.vulnerabilityDiff.assetVulnerabilityRemediationDiff.vulnerabilitiesResolvedInA[].componentName` | `string` | yes |
| `getAssetComparisonReport.vulnerabilityDiff.assetVulnerabilityRemediationDiff.vulnerabilitiesResolvedInA[].componentVersion` | `string` | yes |
| `getAssetComparisonReport.vulnerabilityDiff.assetVulnerabilityRemediationDiff.vulnerabilitiesResolvedInA[].cveId` | `string` | yes |
| `getAssetComparisonReport.vulnerabilityDiff.assetVulnerabilityRemediationDiff.vulnerabilitiesResolvedInA[].cvssScore` | `float` | yes |
| `getAssetComparisonReport.vulnerabilityDiff.assetVulnerabilityRemediationDiff.vulnerabilitiesResolvedInA[].exploitMaturity` | `string` | yes |
| `getAssetComparisonReport.vulnerabilityDiff.assetVulnerabilityRemediationDiff.vulnerabilitiesResolvedInA[].reachable` | `boolean` | yes |
| `getAssetComparisonReport.vulnerabilityDiff.assetVulnerabilityRemediationDiff.vulnerabilitiesResolvedInA[].severity` | `string` | yes |
| `getAssetComparisonReport.vulnerabilityDiff.assetVulnerabilityRemediationDiff.vulnerabilitiesResolvedInAPresentInB[]` | `object` | yes |
| `getAssetComparisonReport.vulnerabilityDiff.assetVulnerabilityRemediationDiff.vulnerabilitiesResolvedInAPresentInB[].cisaKev` | `boolean` | yes |
| `getAssetComparisonReport.vulnerabilityDiff.assetVulnerabilityRemediationDiff.vulnerabilitiesResolvedInAPresentInB[].componentName` | `string` | yes |
| `getAssetComparisonReport.vulnerabilityDiff.assetVulnerabilityRemediationDiff.vulnerabilitiesResolvedInAPresentInB[].componentVersion` | `string` | yes |
| `getAssetComparisonReport.vulnerabilityDiff.assetVulnerabilityRemediationDiff.vulnerabilitiesResolvedInAPresentInB[].cveId` | `string` | yes |
| `getAssetComparisonReport.vulnerabilityDiff.assetVulnerabilityRemediationDiff.vulnerabilitiesResolvedInAPresentInB[].cvssScore` | `float` | yes |
| `getAssetComparisonReport.vulnerabilityDiff.assetVulnerabilityRemediationDiff.vulnerabilitiesResolvedInAPresentInB[].exploitMaturity` | `string` | yes |
| `getAssetComparisonReport.vulnerabilityDiff.assetVulnerabilityRemediationDiff.vulnerabilitiesResolvedInAPresentInB[].reachable` | `boolean` | yes |
| `getAssetComparisonReport.vulnerabilityDiff.assetVulnerabilityRemediationDiff.vulnerabilitiesResolvedInAPresentInB[].severity` | `string` | yes |
| `getAssetComparisonReport.vulnerabilityDiff.assetVulnerabilityRemediationDiff.vulnerabilitiesResolvedInB[]` | `object` | yes |
| `getAssetComparisonReport.vulnerabilityDiff.assetVulnerabilityRemediationDiff.vulnerabilitiesResolvedInB[].cisaKev` | `boolean` | yes |
| `getAssetComparisonReport.vulnerabilityDiff.assetVulnerabilityRemediationDiff.vulnerabilitiesResolvedInB[].componentName` | `string` | yes |
| `getAssetComparisonReport.vulnerabilityDiff.assetVulnerabilityRemediationDiff.vulnerabilitiesResolvedInB[].componentVersion` | `string` | yes |
| `getAssetComparisonReport.vulnerabilityDiff.assetVulnerabilityRemediationDiff.vulnerabilitiesResolvedInB[].cveId` | `string` | yes |
| `getAssetComparisonReport.vulnerabilityDiff.assetVulnerabilityRemediationDiff.vulnerabilitiesResolvedInB[].cvssScore` | `float` | yes |
| `getAssetComparisonReport.vulnerabilityDiff.assetVulnerabilityRemediationDiff.vulnerabilitiesResolvedInB[].exploitMaturity` | `string` | yes |
| `getAssetComparisonReport.vulnerabilityDiff.assetVulnerabilityRemediationDiff.vulnerabilitiesResolvedInB[].reachable` | `boolean` | yes |
| `getAssetComparisonReport.vulnerabilityDiff.assetVulnerabilityRemediationDiff.vulnerabilitiesResolvedInB[].severity` | `string` | yes |
| `getAssetComparisonReport.vulnerabilityDiff.assetVulnerabilityRemediationDiff.vulnerabilitiesResolvedInBPresentInA[]` | `object` | yes |
| `getAssetComparisonReport.vulnerabilityDiff.assetVulnerabilityRemediationDiff.vulnerabilitiesResolvedInBPresentInA[].cisaKev` | `boolean` | yes |
| `getAssetComparisonReport.vulnerabilityDiff.assetVulnerabilityRemediationDiff.vulnerabilitiesResolvedInBPresentInA[].componentName` | `string` | yes |
| `getAssetComparisonReport.vulnerabilityDiff.assetVulnerabilityRemediationDiff.vulnerabilitiesResolvedInBPresentInA[].componentVersion` | `string` | yes |
| `getAssetComparisonReport.vulnerabilityDiff.assetVulnerabilityRemediationDiff.vulnerabilitiesResolvedInBPresentInA[].cveId` | `string` | yes |
| `getAssetComparisonReport.vulnerabilityDiff.assetVulnerabilityRemediationDiff.vulnerabilitiesResolvedInBPresentInA[].cvssScore` | `float` | yes |
| `getAssetComparisonReport.vulnerabilityDiff.assetVulnerabilityRemediationDiff.vulnerabilitiesResolvedInBPresentInA[].exploitMaturity` | `string` | yes |
| `getAssetComparisonReport.vulnerabilityDiff.assetVulnerabilityRemediationDiff.vulnerabilitiesResolvedInBPresentInA[].reachable` | `boolean` | yes |
| `getAssetComparisonReport.vulnerabilityDiff.assetVulnerabilityRemediationDiff.vulnerabilitiesResolvedInBPresentInA[].severity` | `string` | yes |
| `getAssetComparisonReport.vulnerabilityDiff.inANotInB[]` | `object` | yes |
| `getAssetComparisonReport.vulnerabilityDiff.inANotInB[].cisaKev` | `boolean` | yes |
| `getAssetComparisonReport.vulnerabilityDiff.inANotInB[].componentName` | `string` | yes |
| `getAssetComparisonReport.vulnerabilityDiff.inANotInB[].componentVersion` | `string` | yes |
| `getAssetComparisonReport.vulnerabilityDiff.inANotInB[].cveId` | `string` | yes |
| `getAssetComparisonReport.vulnerabilityDiff.inANotInB[].cvssScore` | `float` | yes |
| `getAssetComparisonReport.vulnerabilityDiff.inANotInB[].exploitMaturity` | `string` | yes |
| `getAssetComparisonReport.vulnerabilityDiff.inANotInB[].reachable` | `boolean` | yes |
| `getAssetComparisonReport.vulnerabilityDiff.inANotInB[].severity` | `string` | yes |
| `getAssetComparisonReport.vulnerabilityDiff.inANotInBKevCount` | `integer` | yes |
| `getAssetComparisonReport.vulnerabilityDiff.inANotInBReachableCount` | `integer` | yes |
| `getAssetComparisonReport.vulnerabilityDiff.inBNotInA[]` | `object` | yes |
| `getAssetComparisonReport.vulnerabilityDiff.inBNotInA[].cisaKev` | `boolean` | yes |
| `getAssetComparisonReport.vulnerabilityDiff.inBNotInA[].componentName` | `string` | yes |
| `getAssetComparisonReport.vulnerabilityDiff.inBNotInA[].componentVersion` | `string` | yes |
| `getAssetComparisonReport.vulnerabilityDiff.inBNotInA[].cveId` | `string` | yes |
| `getAssetComparisonReport.vulnerabilityDiff.inBNotInA[].cvssScore` | `float` | yes |
| `getAssetComparisonReport.vulnerabilityDiff.inBNotInA[].exploitMaturity` | `string` | yes |
| `getAssetComparisonReport.vulnerabilityDiff.inBNotInA[].reachable` | `boolean` | yes |
| `getAssetComparisonReport.vulnerabilityDiff.inBNotInA[].severity` | `string` | yes |
| `getAssetComparisonReport.vulnerabilityDiff.inBNotInAKevCount` | `integer` | yes |
| `getAssetComparisonReport.vulnerabilityDiff.inBNotInAReachableCount` | `integer` | yes |
| `getAssetComparisonReport.vulnerabilityDiff.overlap[]` | `object` | yes |
| `getAssetComparisonReport.vulnerabilityDiff.overlap[].cisaKev` | `boolean` | yes |
| `getAssetComparisonReport.vulnerabilityDiff.overlap[].componentName` | `string` | yes |
| `getAssetComparisonReport.vulnerabilityDiff.overlap[].componentVersion` | `string` | yes |
| `getAssetComparisonReport.vulnerabilityDiff.overlap[].cveId` | `string` | yes |
| `getAssetComparisonReport.vulnerabilityDiff.overlap[].cvssScore` | `float` | yes |
| `getAssetComparisonReport.vulnerabilityDiff.overlap[].exploitMaturity` | `string` | yes |
| `getAssetComparisonReport.vulnerabilityDiff.overlap[].reachable` | `boolean` | yes |
| `getAssetComparisonReport.vulnerabilityDiff.overlap[].severity` | `string` | yes |
| `getAssetComparisonReport.vulnerabilityDiff.overlapKevCount` | `integer` | yes |
| `getAssetComparisonReport.vulnerabilityDiff.overlapReachableCount` | `integer` | yes |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    GetAssetComparisonReportInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_get_asset_comparison_report(get_asset_comparison_report_args=GetAssetComparisonReportInput(report_id='id_123'))
        # Responses are typed Pydantic models: read fields as attributes.
        print(resp.get_asset_comparison_report.asset_a_info.name, resp.get_asset_comparison_report.asset_b_info.name)


if __name__ == "__main__":
    main()
```
