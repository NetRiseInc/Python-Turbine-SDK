<!-- Generated file: do not edit by hand -->

# mutation_remediate_asset_vulnerabilities

Bulk apply VEX remediation status to multiple vulnerabilities on assets.

## Parameters

| name | type | required |
| --- | --- | --- |
| `remediate_asset_vulnerabilities_args` | `CreateAssetVulnerabilityRemediationsInput` | `true` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `remediateAssetVulnerabilities[]` | `object` | no |
| `remediateAssetVulnerabilities[].id` | `string` | no |
| `remediateAssetVulnerabilities[].attackComplexity` | `string` | yes |
| `remediateAssetVulnerabilities[].attackVector` | `string` | yes |
| `remediateAssetVulnerabilities[].correlations[]` | `object` | yes |
| `remediateAssetVulnerabilities[].correlations[].artifact` | `string` | yes |
| `remediateAssetVulnerabilities[].correlations[].assetId` | `string` | yes |
| `remediateAssetVulnerabilities[].correlations[].assetName` | `string` | yes |
| `remediateAssetVulnerabilities[].correlations[].location` | `string` | yes |
| `remediateAssetVulnerabilities[].correlations[].risk` | `object` | yes |
| `remediateAssetVulnerabilities[].correlations[].risk.category` | `RiskCategory` | yes |
| `remediateAssetVulnerabilities[].correlations[].risk.rawScore` | `float` | yes |
| `remediateAssetVulnerabilities[].correlations[].risk.score` | `float` | yes |
| `remediateAssetVulnerabilities[].correlations[].updatedAt` | `string` | yes |
| `remediateAssetVulnerabilities[].correlationsCount` | `integer` | yes |
| `remediateAssetVulnerabilities[].currentRemediation` | `object` | yes |
| `remediateAssetVulnerabilities[].currentRemediation.assetId` | `string` | yes |
| `remediateAssetVulnerabilities[].currentRemediation.author` | `string` | no |
| `remediateAssetVulnerabilities[].currentRemediation.createdAt` | `string` | no |
| `remediateAssetVulnerabilities[].currentRemediation.description` | `string` | yes |
| `remediateAssetVulnerabilities[].currentRemediation.identificationIds[]` | `string` | yes |
| `remediateAssetVulnerabilities[].currentRemediation.justification` | `VexJustification` | yes |
| `remediateAssetVulnerabilities[].currentRemediation.response` | `RemediationResponses` | yes |
| `remediateAssetVulnerabilities[].currentRemediation.status` | `VexStatus` | no |
| `remediateAssetVulnerabilities[].currentRemediation.vulnerabilityId` | `string` | no |
| `remediateAssetVulnerabilities[].cve` | `string` | yes |
| `remediateAssetVulnerabilities[].cvssScore` | `float` | yes |
| `remediateAssetVulnerabilities[].epssPercentile` | `float` | yes |
| `remediateAssetVulnerabilities[].epssScore` | `float` | yes |
| `remediateAssetVulnerabilities[].filePath` | `string` | yes |
| `remediateAssetVulnerabilities[].fixVersions[]` | `string` | yes |
| `remediateAssetVulnerabilities[].identificationIds[]` | `string` | yes |
| `remediateAssetVulnerabilities[].inKnownExploitedVulnerabilities` | `boolean` | yes |
| `remediateAssetVulnerabilities[].isReachable` | `boolean` | yes |
| `remediateAssetVulnerabilities[].maturity` | `string` | yes |
| `remediateAssetVulnerabilities[].name` | `string` | yes |
| `remediateAssetVulnerabilities[].severity` | `string` | yes |
| `remediateAssetVulnerabilities[].vendor` | `string` | yes |
| `remediateAssetVulnerabilities[].version` | `string` | yes |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    CreateAssetVulnerabilityRemediationsInput,
    RemediationId,
)
from netrise_turbine_sdk_graphql.enums import (
    VexStatus,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.mutation_remediate_asset_vulnerabilities(remediate_asset_vulnerabilities_args=CreateAssetVulnerabilityRemediationsInput(asset_id='asset_123', remediation_ids=[RemediationId(vulnerability_id=None  # TODO: fill)], status=VexStatus.UNSPECIFIED))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
