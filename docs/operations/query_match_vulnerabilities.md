<!-- Generated file: do not edit by hand -->

# query_match_vulnerabilities

Find specific vulnerabilities matching a provided component identifier or package.

## Parameters

| name | type | required |
| --- | --- | --- |
| `match_vulnerabilities_args` | `MatchVulnerabilitiesInput` | `true` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `matchVulnerabilities[]` | `object` | yes |
| `matchVulnerabilities[].id` | `string` | no |
| `matchVulnerabilities[].createdDatetime` | `string` | no |
| `matchVulnerabilities[].currentRemediation` | `object` | yes |
| `matchVulnerabilities[].currentRemediation.assetId` | `string` | yes |
| `matchVulnerabilities[].currentRemediation.author` | `string` | no |
| `matchVulnerabilities[].currentRemediation.createdAt` | `string` | no |
| `matchVulnerabilities[].currentRemediation.description` | `string` | yes |
| `matchVulnerabilities[].currentRemediation.identificationIds[]` | `string` | yes |
| `matchVulnerabilities[].currentRemediation.justification` | `VexJustification` | yes |
| `matchVulnerabilities[].currentRemediation.response` | `RemediationResponses` | yes |
| `matchVulnerabilities[].currentRemediation.status` | `VexStatus` | no |
| `matchVulnerabilities[].currentRemediation.vulnerabilityId` | `string` | no |
| `matchVulnerabilities[].description` | `string` | yes |
| `matchVulnerabilities[].exploit` | `object` | yes |
| `matchVulnerabilities[].exploit.botnetDatetime` | `string` | yes |
| `matchVulnerabilities[].exploit.epss` | `object` | yes |
| `matchVulnerabilities[].exploit.epss.percentile` | `float` | no |
| `matchVulnerabilities[].exploit.epss.score` | `float` | no |
| `matchVulnerabilities[].exploit.exploitDatetime` | `string` | yes |
| `matchVulnerabilities[].exploit.found` | `boolean` | no |
| `matchVulnerabilities[].exploit.inBotnets` | `boolean` | no |
| `matchVulnerabilities[].exploit.inKnownExploitedVulnerabilities` | `boolean` | no |
| `matchVulnerabilities[].exploit.inRansomware` | `boolean` | no |
| `matchVulnerabilities[].exploit.inTheWild` | `boolean` | no |
| `matchVulnerabilities[].exploit.inThreatActors` | `boolean` | no |
| `matchVulnerabilities[].exploit.isTrendingGithub` | `boolean` | no |
| `matchVulnerabilities[].exploit.kevAddedDatetime` | `string` | yes |
| `matchVulnerabilities[].exploit.kevDueDatetime` | `string` | yes |
| `matchVulnerabilities[].exploit.knownAttacks[]` | `string` | yes |
| `matchVulnerabilities[].exploit.maturity` | `string` | no |
| `matchVulnerabilities[].exploit.pocDatetime` | `string` | yes |
| `matchVulnerabilities[].exploit.prevalence` | `object` | yes |
| `matchVulnerabilities[].exploit.prevalence.botnets` | `integer` | no |
| `matchVulnerabilities[].exploit.prevalence.exploit` | `integer` | no |
| `matchVulnerabilities[].exploit.prevalence.knownAttacks` | `integer` | no |
| `matchVulnerabilities[].exploit.prevalence.ransomware` | `integer` | yes |
| `matchVulnerabilities[].exploit.prevalence.threatActors` | `integer` | no |
| `matchVulnerabilities[].exploit.publishDatetime` | `string` | yes |
| `matchVulnerabilities[].exploit.ransomwareDatetime` | `string` | yes |
| `matchVulnerabilities[].exploit.recentBotnetDatetime` | `string` | yes |
| `matchVulnerabilities[].exploit.recentExploitDatetime` | `string` | yes |
| `matchVulnerabilities[].exploit.recentRansomwareDatetime` | `string` | yes |
| `matchVulnerabilities[].exploit.recentThreatActorDatetime` | `string` | yes |
| `matchVulnerabilities[].exploit.references` | `object` | yes |
| `matchVulnerabilities[].exploit.references.botnets[]` | `object` | yes |
| `matchVulnerabilities[].exploit.references.botnets[].botnetName` | `string` | no |
| `matchVulnerabilities[].exploit.references.botnets[].dateAdded` | `string` | no |
| `matchVulnerabilities[].exploit.references.botnets[].url` | `string` | yes |
| `matchVulnerabilities[].exploit.references.exploits[]` | `object` | yes |
| `matchVulnerabilities[].exploit.references.exploits[].dateAdded` | `string` | no |
| `matchVulnerabilities[].exploit.references.exploits[].exploitAvailability` | `string` | no |
| `matchVulnerabilities[].exploit.references.exploits[].exploitMaturity` | `string` | no |
| `matchVulnerabilities[].exploit.references.exploits[].name` | `string` | no |
| `matchVulnerabilities[].exploit.references.exploits[].refsource` | `string` | no |
| `matchVulnerabilities[].exploit.references.exploits[].url` | `string` | no |
| `matchVulnerabilities[].exploit.references.knownAttacks[]` | `object` | yes |
| `matchVulnerabilities[].exploit.references.knownAttacks[].associatedVulnerabilitiesList[]` | `string` | yes |
| `matchVulnerabilities[].exploit.references.knownAttacks[].displayName` | `string` | yes |
| `matchVulnerabilities[].exploit.references.knownAttacks[].name` | `string` | yes |
| `matchVulnerabilities[].exploit.references.knownExploitedVulnerabilities` | `object` | yes |
| `matchVulnerabilities[].exploit.references.knownExploitedVulnerabilities.action` | `string` | no |
| `matchVulnerabilities[].exploit.references.knownExploitedVulnerabilities.dateAdded` | `string` | no |
| `matchVulnerabilities[].exploit.references.knownExploitedVulnerabilities.description` | `string` | no |
| `matchVulnerabilities[].exploit.references.knownExploitedVulnerabilities.dueDate` | `string` | no |
| `matchVulnerabilities[].exploit.references.knownExploitedVulnerabilities.name` | `string` | no |
| `matchVulnerabilities[].exploit.references.knownExploitedVulnerabilities.notes` | `string` | no |
| `matchVulnerabilities[].exploit.references.knownExploitedVulnerabilities.product` | `string` | no |
| `matchVulnerabilities[].exploit.references.knownExploitedVulnerabilities.vendor` | `string` | no |
| `matchVulnerabilities[].exploit.references.ransomware[]` | `object` | yes |
| `matchVulnerabilities[].exploit.references.ransomware[].families[]` | `string` | no |
| `matchVulnerabilities[].exploit.references.ransomware[].references[]` | `object` | no |
| `matchVulnerabilities[].exploit.references.ransomware[].references[].date` | `string` | no |
| `matchVulnerabilities[].exploit.references.ransomware[].references[].url` | `string` | no |
| `matchVulnerabilities[].exploit.references.threatActors[]` | `object` | yes |
| `matchVulnerabilities[].exploit.references.threatActors[].aliases[]` | `string` | yes |
| `matchVulnerabilities[].exploit.references.threatActors[].name` | `string` | no |
| `matchVulnerabilities[].exploit.references.threatActors[].url` | `string` | no |
| `matchVulnerabilities[].exploit.threatActorDatetime` | `string` | yes |
| `matchVulnerabilities[].exploit.weaponizeDatetime` | `string` | yes |
| `matchVulnerabilities[].impact` | `object` | yes |
| `matchVulnerabilities[].impact.base` | `object` | no |
| `matchVulnerabilities[].impact.base.attackComplexity` | `string` | no |
| `matchVulnerabilities[].impact.base.attackVector` | `string` | no |
| `matchVulnerabilities[].impact.base.availabilityImpact` | `string` | no |
| `matchVulnerabilities[].impact.base.baseScore` | `float` | no |
| `matchVulnerabilities[].impact.base.baseSeverity` | `string` | no |
| `matchVulnerabilities[].impact.base.confidentialityImpact` | `string` | no |
| `matchVulnerabilities[].impact.base.exploitabilityScore` | `float` | no |
| `matchVulnerabilities[].impact.base.impactScore` | `float` | no |
| `matchVulnerabilities[].impact.base.integrityImpact` | `string` | no |
| `matchVulnerabilities[].impact.base.privilegesRequired` | `string` | no |
| `matchVulnerabilities[].impact.base.scope` | `string` | no |
| `matchVulnerabilities[].impact.base.userInteraction` | `string` | no |
| `matchVulnerabilities[].impact.base.vectorString` | `string` | no |
| `matchVulnerabilities[].impact.temporal` | `object` | no |
| `matchVulnerabilities[].impact.temporal.exploitCodeMaturity` | `string` | no |
| `matchVulnerabilities[].impact.temporal.remediationLevel` | `string` | no |
| `matchVulnerabilities[].impact.temporal.reportConfidence` | `string` | no |
| `matchVulnerabilities[].impact.temporal.temporalScore` | `float` | no |
| `matchVulnerabilities[].impact.temporal.vectorString` | `string` | no |
| `matchVulnerabilities[].impactV2` | `object` | yes |
| `matchVulnerabilities[].impactV2.base` | `object` | no |
| `matchVulnerabilities[].impactV2.base.accessComplexity` | `string` | no |
| `matchVulnerabilities[].impactV2.base.accessVector` | `string` | no |
| `matchVulnerabilities[].impactV2.base.authentication` | `string` | no |
| `matchVulnerabilities[].impactV2.base.availabilityImpact` | `string` | no |
| `matchVulnerabilities[].impactV2.base.baseScore` | `float` | no |
| `matchVulnerabilities[].impactV2.base.confidentialityImpact` | `string` | no |
| `matchVulnerabilities[].impactV2.base.exploitabilityScore` | `float` | no |
| `matchVulnerabilities[].impactV2.base.impactScore` | `float` | no |
| `matchVulnerabilities[].impactV2.base.integrityImpact` | `string` | no |
| `matchVulnerabilities[].impactV2.base.severity` | `string` | no |
| `matchVulnerabilities[].impactV2.base.vectorString` | `string` | no |
| `matchVulnerabilities[].impactV2.base.version` | `string` | no |
| `matchVulnerabilities[].impactV2.temporal` | `object` | no |
| `matchVulnerabilities[].impactV2.temporal.exploitability` | `string` | no |
| `matchVulnerabilities[].impactV2.temporal.remediationLevel` | `string` | no |
| `matchVulnerabilities[].impactV2.temporal.reportConfidence` | `string` | no |
| `matchVulnerabilities[].impactV2.temporal.temporalScore` | `float` | no |
| `matchVulnerabilities[].impactV2.temporal.vectorString` | `string` | no |
| `matchVulnerabilities[].impactV2.temporal.version` | `string` | no |
| `matchVulnerabilities[].impactV31` | `object` | yes |
| `matchVulnerabilities[].impactV31.metric` | `object` | yes |
| `matchVulnerabilities[].impactV31.metric.cvssData` | `object` | yes |
| `matchVulnerabilities[].impactV31.metric.cvssData.attackComplexity` | `string` | yes |
| `matchVulnerabilities[].impactV31.metric.cvssData.attackVector` | `string` | yes |
| `matchVulnerabilities[].impactV31.metric.cvssData.availabilityImpact` | `string` | yes |
| `matchVulnerabilities[].impactV31.metric.cvssData.baseScore` | `float` | yes |
| `matchVulnerabilities[].impactV31.metric.cvssData.baseSeverity` | `string` | yes |
| `matchVulnerabilities[].impactV31.metric.cvssData.confidentialityImpact` | `string` | yes |
| `matchVulnerabilities[].impactV31.metric.cvssData.environmentalScore` | `float` | yes |
| `matchVulnerabilities[].impactV31.metric.cvssData.integrityImpact` | `string` | yes |
| `matchVulnerabilities[].impactV31.metric.cvssData.privilegesRequired` | `string` | yes |
| `matchVulnerabilities[].impactV31.metric.cvssData.scope` | `string` | yes |
| `matchVulnerabilities[].impactV31.metric.cvssData.temporalScore` | `float` | yes |
| `matchVulnerabilities[].impactV31.metric.cvssData.userInteraction` | `string` | yes |
| `matchVulnerabilities[].impactV31.metric.cvssData.vectorString` | `string` | yes |
| `matchVulnerabilities[].impactV31.metric.cvssData.version` | `string` | yes |
| `matchVulnerabilities[].impactV31.metric.exploitabilityScore` | `float` | yes |
| `matchVulnerabilities[].impactV31.metric.impactScore` | `float` | yes |
| `matchVulnerabilities[].impactV31.metric.source` | `string` | yes |
| `matchVulnerabilities[].impactV31.metric.type` | `string` | yes |
| `matchVulnerabilities[].impactV31.temporal` | `object` | yes |
| `matchVulnerabilities[].impactV31.temporal.exploitCodeMaturity` | `string` | no |
| `matchVulnerabilities[].impactV31.temporal.remediationLevel` | `string` | no |
| `matchVulnerabilities[].impactV31.temporal.reportConfidence` | `string` | no |
| `matchVulnerabilities[].impactV31.temporal.temporalScore` | `float` | no |
| `matchVulnerabilities[].impactV31.temporal.vectorString` | `string` | no |
| `matchVulnerabilities[].impactV4` | `object` | yes |
| `matchVulnerabilities[].impactV4.cvssData` | `object` | yes |
| `matchVulnerabilities[].impactV4.cvssData.attackComplexity` | `string` | yes |
| `matchVulnerabilities[].impactV4.cvssData.attackRequirements` | `string` | yes |
| `matchVulnerabilities[].impactV4.cvssData.attackVector` | `string` | yes |
| `matchVulnerabilities[].impactV4.cvssData.automatable` | `string` | yes |
| `matchVulnerabilities[].impactV4.cvssData.availabilityRequirement` | `string` | yes |
| `matchVulnerabilities[].impactV4.cvssData.baseScore` | `float` | yes |
| `matchVulnerabilities[].impactV4.cvssData.baseSeverity` | `string` | yes |
| `matchVulnerabilities[].impactV4.cvssData.confidentialityRequirement` | `string` | yes |
| `matchVulnerabilities[].impactV4.cvssData.exploitMaturity` | `string` | yes |
| `matchVulnerabilities[].impactV4.cvssData.integrityRequirement` | `string` | yes |
| `matchVulnerabilities[].impactV4.cvssData.modifiedAttackComplexity` | `string` | yes |
| `matchVulnerabilities[].impactV4.cvssData.modifiedAttackRequirements` | `string` | yes |
| `matchVulnerabilities[].impactV4.cvssData.modifiedAttackVector` | `string` | yes |
| `matchVulnerabilities[].impactV4.cvssData.modifiedPrivilegesRequired` | `string` | yes |
| `matchVulnerabilities[].impactV4.cvssData.modifiedSubAvailabilityImpact` | `string` | yes |
| `matchVulnerabilities[].impactV4.cvssData.modifiedSubConfidentialityImpact` | `string` | yes |
| `matchVulnerabilities[].impactV4.cvssData.modifiedSubIntegrityImpact` | `string` | yes |
| `matchVulnerabilities[].impactV4.cvssData.modifiedUserInteraction` | `string` | yes |
| `matchVulnerabilities[].impactV4.cvssData.modifiedVulnAvailabilityImpact` | `string` | yes |
| `matchVulnerabilities[].impactV4.cvssData.modifiedVulnConfidentialityImpact` | `string` | yes |
| `matchVulnerabilities[].impactV4.cvssData.modifiedVulnIntegrityImpact` | `string` | yes |
| `matchVulnerabilities[].impactV4.cvssData.privilegesRequired` | `string` | yes |
| `matchVulnerabilities[].impactV4.cvssData.providerUrgency` | `string` | yes |
| `matchVulnerabilities[].impactV4.cvssData.recovery` | `string` | yes |
| `matchVulnerabilities[].impactV4.cvssData.safety` | `string` | yes |
| `matchVulnerabilities[].impactV4.cvssData.subAvailabilityImpact` | `string` | yes |
| `matchVulnerabilities[].impactV4.cvssData.subConfidentialityImpact` | `string` | yes |
| `matchVulnerabilities[].impactV4.cvssData.subIntegrityImpact` | `string` | yes |
| `matchVulnerabilities[].impactV4.cvssData.userInteraction` | `string` | yes |
| `matchVulnerabilities[].impactV4.cvssData.valueDensity` | `string` | yes |
| `matchVulnerabilities[].impactV4.cvssData.vectorString` | `string` | yes |
| `matchVulnerabilities[].impactV4.cvssData.version` | `string` | yes |
| `matchVulnerabilities[].impactV4.cvssData.vulnAvailabilityImpact` | `string` | yes |
| `matchVulnerabilities[].impactV4.cvssData.vulnConfidentialityImpact` | `string` | yes |
| `matchVulnerabilities[].impactV4.cvssData.vulnIntegrityImpact` | `string` | yes |
| `matchVulnerabilities[].impactV4.cvssData.vulnerabilityResponseEffort` | `string` | yes |
| `matchVulnerabilities[].impactV4.source` | `string` | yes |
| `matchVulnerabilities[].impactV4.threatCvssSecondary` | `object` | yes |
| `matchVulnerabilities[].impactV4.threatCvssSecondary.associatedBaseMetricV40` | `object` | yes |
| `matchVulnerabilities[].impactV4.threatCvssSecondary.associatedBaseMetricV40.baseScore` | `float` | yes |
| `matchVulnerabilities[].impactV4.threatCvssSecondary.associatedBaseMetricV40.source` | `string` | yes |
| `matchVulnerabilities[].impactV4.threatCvssSecondary.associatedBaseMetricV40.type` | `string` | yes |
| `matchVulnerabilities[].impactV4.threatCvssSecondary.baseThreatScore` | `float` | yes |
| `matchVulnerabilities[].impactV4.threatCvssSecondary.baseThreatSeverity` | `string` | yes |
| `matchVulnerabilities[].impactV4.threatCvssSecondary.exploitMaturity` | `string` | yes |
| `matchVulnerabilities[].impactV4.type` | `string` | yes |
| `matchVulnerabilities[].nvdStatus` | `VulnerabilityNVDStatus` | yes |
| `matchVulnerabilities[].priorityScore` | `float` | no |
| `matchVulnerabilities[].problemTypes[]` | `object` | yes |
| `matchVulnerabilities[].problemTypes[].name` | `string` | yes |
| `matchVulnerabilities[].problemTypes[].url` | `string` | no |
| `matchVulnerabilities[].problemTypes[].value` | `string` | no |
| `matchVulnerabilities[].processedDatetime` | `string` | no |
| `matchVulnerabilities[].references[]` | `object` | yes |
| `matchVulnerabilities[].references[].name` | `string` | yes |
| `matchVulnerabilities[].references[].refsource` | `string` | no |
| `matchVulnerabilities[].references[].url` | `string` | no |
| `matchVulnerabilities[].severity` | `string` | no |
| `matchVulnerabilities[].tags[]` | `string` | yes |
| `matchVulnerabilities[].updatedDatetime` | `string` | no |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    MatchVulnerabilitiesInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_match_vulnerabilities(match_vulnerabilities_args=MatchVulnerabilitiesInput(identifier='cpe:2.3:a:vendor:product:1.0'))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
