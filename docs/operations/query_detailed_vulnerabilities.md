<!-- Generated file: do not edit by hand -->

# query_detailed_vulnerabilities

Retrieve in-depth vulnerability data including descriptions and CVSS vector strings.

## Parameters

| name | type | required |
| --- | --- | --- |
| `detailed_vulnerabilities_args` | `PaginatedDetailedVulnerabilitiesInput` | `true` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `detailedVulnerabilities` | `object` | yes |
| `detailedVulnerabilities.edges[]` | `object` | yes |
| `detailedVulnerabilities.edges[].cursor` | `string` | yes |
| `detailedVulnerabilities.edges[].node` | `object` | yes |
| `detailedVulnerabilities.edges[].node.id` | `string` | yes |
| `detailedVulnerabilities.edges[].node.createdDatetime` | `string` | yes |
| `detailedVulnerabilities.edges[].node.description` | `string` | yes |
| `detailedVulnerabilities.edges[].node.exploit` | `object` | yes |
| `detailedVulnerabilities.edges[].node.exploit.botnetDatetime` | `string` | yes |
| `detailedVulnerabilities.edges[].node.exploit.epss` | `object` | yes |
| `detailedVulnerabilities.edges[].node.exploit.epss.percentile` | `float` | no |
| `detailedVulnerabilities.edges[].node.exploit.epss.score` | `float` | no |
| `detailedVulnerabilities.edges[].node.exploit.exploitDatetime` | `string` | yes |
| `detailedVulnerabilities.edges[].node.exploit.found` | `boolean` | no |
| `detailedVulnerabilities.edges[].node.exploit.inBotnets` | `boolean` | no |
| `detailedVulnerabilities.edges[].node.exploit.inKnownExploitedVulnerabilities` | `boolean` | no |
| `detailedVulnerabilities.edges[].node.exploit.inRansomware` | `boolean` | no |
| `detailedVulnerabilities.edges[].node.exploit.inTheWild` | `boolean` | no |
| `detailedVulnerabilities.edges[].node.exploit.inThreatActors` | `boolean` | no |
| `detailedVulnerabilities.edges[].node.exploit.isTrendingGithub` | `boolean` | no |
| `detailedVulnerabilities.edges[].node.exploit.kevAddedDatetime` | `string` | yes |
| `detailedVulnerabilities.edges[].node.exploit.kevDueDatetime` | `string` | yes |
| `detailedVulnerabilities.edges[].node.exploit.knownAttacks[]` | `string` | yes |
| `detailedVulnerabilities.edges[].node.exploit.maturity` | `string` | no |
| `detailedVulnerabilities.edges[].node.exploit.pocDatetime` | `string` | yes |
| `detailedVulnerabilities.edges[].node.exploit.prevalence` | `object` | yes |
| `detailedVulnerabilities.edges[].node.exploit.prevalence.botnets` | `integer` | no |
| `detailedVulnerabilities.edges[].node.exploit.prevalence.exploit` | `integer` | no |
| `detailedVulnerabilities.edges[].node.exploit.prevalence.knownAttacks` | `integer` | no |
| `detailedVulnerabilities.edges[].node.exploit.prevalence.ransomware` | `integer` | yes |
| `detailedVulnerabilities.edges[].node.exploit.prevalence.threatActors` | `integer` | no |
| `detailedVulnerabilities.edges[].node.exploit.publishDatetime` | `string` | yes |
| `detailedVulnerabilities.edges[].node.exploit.ransomwareDatetime` | `string` | yes |
| `detailedVulnerabilities.edges[].node.exploit.recentBotnetDatetime` | `string` | yes |
| `detailedVulnerabilities.edges[].node.exploit.recentExploitDatetime` | `string` | yes |
| `detailedVulnerabilities.edges[].node.exploit.recentRansomwareDatetime` | `string` | yes |
| `detailedVulnerabilities.edges[].node.exploit.recentThreatActorDatetime` | `string` | yes |
| `detailedVulnerabilities.edges[].node.exploit.threatActorDatetime` | `string` | yes |
| `detailedVulnerabilities.edges[].node.exploit.weaponizeDatetime` | `string` | yes |
| `detailedVulnerabilities.edges[].node.impact` | `object` | yes |
| `detailedVulnerabilities.edges[].node.impact.base` | `object` | no |
| `detailedVulnerabilities.edges[].node.impact.base.attackComplexity` | `string` | no |
| `detailedVulnerabilities.edges[].node.impact.base.attackVector` | `string` | no |
| `detailedVulnerabilities.edges[].node.impact.base.availabilityImpact` | `string` | no |
| `detailedVulnerabilities.edges[].node.impact.base.baseScore` | `float` | no |
| `detailedVulnerabilities.edges[].node.impact.base.baseSeverity` | `string` | no |
| `detailedVulnerabilities.edges[].node.impact.base.confidentialityImpact` | `string` | no |
| `detailedVulnerabilities.edges[].node.impact.base.exploitabilityScore` | `float` | no |
| `detailedVulnerabilities.edges[].node.impact.base.impactScore` | `float` | no |
| `detailedVulnerabilities.edges[].node.impact.base.integrityImpact` | `string` | no |
| `detailedVulnerabilities.edges[].node.impact.base.privilegesRequired` | `string` | no |
| `detailedVulnerabilities.edges[].node.impact.base.scope` | `string` | no |
| `detailedVulnerabilities.edges[].node.impact.base.userInteraction` | `string` | no |
| `detailedVulnerabilities.edges[].node.impact.base.vectorString` | `string` | no |
| `detailedVulnerabilities.edges[].node.impact.temporal` | `object` | no |
| `detailedVulnerabilities.edges[].node.impact.temporal.exploitCodeMaturity` | `string` | no |
| `detailedVulnerabilities.edges[].node.impact.temporal.remediationLevel` | `string` | no |
| `detailedVulnerabilities.edges[].node.impact.temporal.reportConfidence` | `string` | no |
| `detailedVulnerabilities.edges[].node.impact.temporal.temporalScore` | `float` | no |
| `detailedVulnerabilities.edges[].node.impact.temporal.vectorString` | `string` | no |
| `detailedVulnerabilities.edges[].node.impactV2` | `object` | yes |
| `detailedVulnerabilities.edges[].node.impactV2.base` | `object` | no |
| `detailedVulnerabilities.edges[].node.impactV2.base.accessComplexity` | `string` | no |
| `detailedVulnerabilities.edges[].node.impactV2.base.accessVector` | `string` | no |
| `detailedVulnerabilities.edges[].node.impactV2.base.authentication` | `string` | no |
| `detailedVulnerabilities.edges[].node.impactV2.base.availabilityImpact` | `string` | no |
| `detailedVulnerabilities.edges[].node.impactV2.base.baseScore` | `float` | no |
| `detailedVulnerabilities.edges[].node.impactV2.base.confidentialityImpact` | `string` | no |
| `detailedVulnerabilities.edges[].node.impactV2.base.exploitabilityScore` | `float` | no |
| `detailedVulnerabilities.edges[].node.impactV2.base.impactScore` | `float` | no |
| `detailedVulnerabilities.edges[].node.impactV2.base.integrityImpact` | `string` | no |
| `detailedVulnerabilities.edges[].node.impactV2.base.severity` | `string` | no |
| `detailedVulnerabilities.edges[].node.impactV2.base.vectorString` | `string` | no |
| `detailedVulnerabilities.edges[].node.impactV2.base.version` | `string` | no |
| `detailedVulnerabilities.edges[].node.impactV2.temporal` | `object` | no |
| `detailedVulnerabilities.edges[].node.impactV2.temporal.exploitability` | `string` | no |
| `detailedVulnerabilities.edges[].node.impactV2.temporal.remediationLevel` | `string` | no |
| `detailedVulnerabilities.edges[].node.impactV2.temporal.reportConfidence` | `string` | no |
| `detailedVulnerabilities.edges[].node.impactV2.temporal.temporalScore` | `float` | no |
| `detailedVulnerabilities.edges[].node.impactV2.temporal.vectorString` | `string` | no |
| `detailedVulnerabilities.edges[].node.impactV2.temporal.version` | `string` | no |
| `detailedVulnerabilities.edges[].node.impactV31` | `object` | yes |
| `detailedVulnerabilities.edges[].node.impactV31.metric` | `object` | yes |
| `detailedVulnerabilities.edges[].node.impactV31.metric.exploitabilityScore` | `float` | yes |
| `detailedVulnerabilities.edges[].node.impactV31.metric.impactScore` | `float` | yes |
| `detailedVulnerabilities.edges[].node.impactV31.metric.source` | `string` | yes |
| `detailedVulnerabilities.edges[].node.impactV31.metric.type` | `string` | yes |
| `detailedVulnerabilities.edges[].node.impactV31.temporal` | `object` | yes |
| `detailedVulnerabilities.edges[].node.impactV31.temporal.exploitCodeMaturity` | `string` | no |
| `detailedVulnerabilities.edges[].node.impactV31.temporal.remediationLevel` | `string` | no |
| `detailedVulnerabilities.edges[].node.impactV31.temporal.reportConfidence` | `string` | no |
| `detailedVulnerabilities.edges[].node.impactV31.temporal.temporalScore` | `float` | no |
| `detailedVulnerabilities.edges[].node.impactV31.temporal.vectorString` | `string` | no |
| `detailedVulnerabilities.edges[].node.impactV4` | `object` | yes |
| `detailedVulnerabilities.edges[].node.impactV4.cvssData` | `object` | yes |
| `detailedVulnerabilities.edges[].node.impactV4.cvssData.attackComplexity` | `string` | yes |
| `detailedVulnerabilities.edges[].node.impactV4.cvssData.attackRequirements` | `string` | yes |
| `detailedVulnerabilities.edges[].node.impactV4.cvssData.attackVector` | `string` | yes |
| `detailedVulnerabilities.edges[].node.impactV4.cvssData.automatable` | `string` | yes |
| `detailedVulnerabilities.edges[].node.impactV4.cvssData.availabilityRequirement` | `string` | yes |
| `detailedVulnerabilities.edges[].node.impactV4.cvssData.baseScore` | `float` | yes |
| `detailedVulnerabilities.edges[].node.impactV4.cvssData.baseSeverity` | `string` | yes |
| `detailedVulnerabilities.edges[].node.impactV4.cvssData.confidentialityRequirement` | `string` | yes |
| `detailedVulnerabilities.edges[].node.impactV4.cvssData.exploitMaturity` | `string` | yes |
| `detailedVulnerabilities.edges[].node.impactV4.cvssData.integrityRequirement` | `string` | yes |
| `detailedVulnerabilities.edges[].node.impactV4.cvssData.modifiedAttackComplexity` | `string` | yes |
| `detailedVulnerabilities.edges[].node.impactV4.cvssData.modifiedAttackRequirements` | `string` | yes |
| `detailedVulnerabilities.edges[].node.impactV4.cvssData.modifiedAttackVector` | `string` | yes |
| `detailedVulnerabilities.edges[].node.impactV4.cvssData.modifiedPrivilegesRequired` | `string` | yes |
| `detailedVulnerabilities.edges[].node.impactV4.cvssData.modifiedSubAvailabilityImpact` | `string` | yes |
| `detailedVulnerabilities.edges[].node.impactV4.cvssData.modifiedSubConfidentialityImpact` | `string` | yes |
| `detailedVulnerabilities.edges[].node.impactV4.cvssData.modifiedSubIntegrityImpact` | `string` | yes |
| `detailedVulnerabilities.edges[].node.impactV4.cvssData.modifiedUserInteraction` | `string` | yes |
| `detailedVulnerabilities.edges[].node.impactV4.cvssData.modifiedVulnAvailabilityImpact` | `string` | yes |
| `detailedVulnerabilities.edges[].node.impactV4.cvssData.modifiedVulnConfidentialityImpact` | `string` | yes |
| `detailedVulnerabilities.edges[].node.impactV4.cvssData.modifiedVulnIntegrityImpact` | `string` | yes |
| `detailedVulnerabilities.edges[].node.impactV4.cvssData.privilegesRequired` | `string` | yes |
| `detailedVulnerabilities.edges[].node.impactV4.cvssData.providerUrgency` | `string` | yes |
| `detailedVulnerabilities.edges[].node.impactV4.cvssData.recovery` | `string` | yes |
| `detailedVulnerabilities.edges[].node.impactV4.cvssData.safety` | `string` | yes |
| `detailedVulnerabilities.edges[].node.impactV4.cvssData.subAvailabilityImpact` | `string` | yes |
| `detailedVulnerabilities.edges[].node.impactV4.cvssData.subConfidentialityImpact` | `string` | yes |
| `detailedVulnerabilities.edges[].node.impactV4.cvssData.subIntegrityImpact` | `string` | yes |
| `detailedVulnerabilities.edges[].node.impactV4.cvssData.userInteraction` | `string` | yes |
| `detailedVulnerabilities.edges[].node.impactV4.cvssData.valueDensity` | `string` | yes |
| `detailedVulnerabilities.edges[].node.impactV4.cvssData.vectorString` | `string` | yes |
| `detailedVulnerabilities.edges[].node.impactV4.cvssData.version` | `string` | yes |
| `detailedVulnerabilities.edges[].node.impactV4.cvssData.vulnAvailabilityImpact` | `string` | yes |
| `detailedVulnerabilities.edges[].node.impactV4.cvssData.vulnConfidentialityImpact` | `string` | yes |
| `detailedVulnerabilities.edges[].node.impactV4.cvssData.vulnIntegrityImpact` | `string` | yes |
| `detailedVulnerabilities.edges[].node.impactV4.cvssData.vulnerabilityResponseEffort` | `string` | yes |
| `detailedVulnerabilities.edges[].node.impactV4.source` | `string` | yes |
| `detailedVulnerabilities.edges[].node.impactV4.threatCvssSecondary` | `object` | yes |
| `detailedVulnerabilities.edges[].node.impactV4.threatCvssSecondary.baseThreatScore` | `float` | yes |
| `detailedVulnerabilities.edges[].node.impactV4.threatCvssSecondary.baseThreatSeverity` | `string` | yes |
| `detailedVulnerabilities.edges[].node.impactV4.threatCvssSecondary.exploitMaturity` | `string` | yes |
| `detailedVulnerabilities.edges[].node.impactV4.type` | `string` | yes |
| `detailedVulnerabilities.edges[].node.problemTypes[]` | `object` | yes |
| `detailedVulnerabilities.edges[].node.problemTypes[].name` | `string` | yes |
| `detailedVulnerabilities.edges[].node.problemTypes[].url` | `string` | no |
| `detailedVulnerabilities.edges[].node.problemTypes[].value` | `string` | no |
| `detailedVulnerabilities.edges[].node.processedDatetime` | `string` | yes |
| `detailedVulnerabilities.edges[].node.references[]` | `object` | yes |
| `detailedVulnerabilities.edges[].node.references[].name` | `string` | yes |
| `detailedVulnerabilities.edges[].node.references[].refsource` | `string` | no |
| `detailedVulnerabilities.edges[].node.references[].url` | `string` | no |
| `detailedVulnerabilities.edges[].node.severity` | `string` | yes |
| `detailedVulnerabilities.edges[].node.updatedDatetime` | `string` | yes |
| `detailedVulnerabilities.pageInfo` | `object` | no |
| `detailedVulnerabilities.pageInfo.endCursor` | `string` | yes |
| `detailedVulnerabilities.pageInfo.hasNextPage` | `boolean` | no |
| `detailedVulnerabilities.pageInfo.hasPreviousPage` | `boolean` | no |
| `detailedVulnerabilities.pageInfo.startCursor` | `string` | yes |
| `detailedVulnerabilities.pageInfo.totalCount` | `integer` | yes |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    PaginatedDetailedVulnerabilitiesInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_detailed_vulnerabilities(detailed_vulnerabilities_args=PaginatedDetailedVulnerabilitiesInput(asset_id='asset_123'))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
