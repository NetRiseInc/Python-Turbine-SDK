<!-- Generated file: do not edit by hand -->

# query_grouped_dependencies

View dependencies aggregated by vendor, license, or specific component type.

## Parameters

| name | type | required |
| --- | --- | --- |
| `grouped_dependencies_args` | `GroupedDependenciesInput` | `true` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `groupedDependencies` | `object` | yes |
| `groupedDependencies.edges[]` | `object` | yes |
| `groupedDependencies.edges[].cursor` | `string` | yes |
| `groupedDependencies.edges[].node` | `object` | yes |
| `groupedDependencies.edges[].node.analytic` | `object` | yes |
| `groupedDependencies.edges[].node.analytic.binaries` | `integer` | no |
| `groupedDependencies.edges[].node.analytic.components` | `object` | no |
| `groupedDependencies.edges[].node.analytic.components.application` | `integer` | no |
| `groupedDependencies.edges[].node.analytic.components.container` | `integer` | no |
| `groupedDependencies.edges[].node.analytic.components.device` | `integer` | no |
| `groupedDependencies.edges[].node.analytic.components.framework` | `integer` | no |
| `groupedDependencies.edges[].node.analytic.components.kernel` | `integer` | no |
| `groupedDependencies.edges[].node.analytic.components.kernelModule` | `integer` | no |
| `groupedDependencies.edges[].node.analytic.components.library` | `integer` | no |
| `groupedDependencies.edges[].node.analytic.components.os` | `integer` | no |
| `groupedDependencies.edges[].node.analytic.components.package` | `integer` | no |
| `groupedDependencies.edges[].node.analytic.credentials` | `object` | no |
| `groupedDependencies.edges[].node.analytic.credentials.crackedCred` | `integer` | yes |
| `groupedDependencies.edges[].node.analytic.credentials.crackedHash` | `integer` | yes |
| `groupedDependencies.edges[].node.analytic.credentials.credential` | `integer` | no |
| `groupedDependencies.edges[].node.analytic.credentials.hash` | `integer` | no |
| `groupedDependencies.edges[].node.analytic.credentials.secrets` | `integer` | yes |
| `groupedDependencies.edges[].node.analytic.cryptography` | `object` | no |
| `groupedDependencies.edges[].node.analytic.cryptography.certificate` | `integer` | no |
| `groupedDependencies.edges[].node.analytic.cryptography.privateKey` | `integer` | no |
| `groupedDependencies.edges[].node.analytic.cryptography.publicKey` | `integer` | no |
| `groupedDependencies.edges[].node.analytic.exploit` | `object` | no |
| `groupedDependencies.edges[].node.analytic.exploit.botnet` | `integer` | no |
| `groupedDependencies.edges[].node.analytic.exploit.exploitCode` | `integer` | yes |
| `groupedDependencies.edges[].node.analytic.exploit.inKnownExploitedVulnerabilities` | `integer` | yes |
| `groupedDependencies.edges[].node.analytic.exploit.inTheWild` | `integer` | no |
| `groupedDependencies.edges[].node.analytic.exploit.knownAttacks` | `integer` | no |
| `groupedDependencies.edges[].node.analytic.exploit.ransomware` | `integer` | no |
| `groupedDependencies.edges[].node.analytic.exploit.threatActor` | `integer` | no |
| `groupedDependencies.edges[].node.analytic.files` | `integer` | no |
| `groupedDependencies.edges[].node.analytic.licenseIssues` | `integer` | no |
| `groupedDependencies.edges[].node.analytic.misconfigurations` | `object` | no |
| `groupedDependencies.edges[].node.analytic.misconfigurations.failed` | `integer` | no |
| `groupedDependencies.edges[].node.analytic.misconfigurations.notApplicable` | `integer` | no |
| `groupedDependencies.edges[].node.analytic.misconfigurations.passed` | `integer` | no |
| `groupedDependencies.edges[].node.analytic.vulnerability` | `object` | no |
| `groupedDependencies.edges[].node.analytic.vulnerability.critical` | `integer` | no |
| `groupedDependencies.edges[].node.analytic.vulnerability.high` | `integer` | no |
| `groupedDependencies.edges[].node.analytic.vulnerability.low` | `integer` | no |
| `groupedDependencies.edges[].node.analytic.vulnerability.medium` | `integer` | no |
| `groupedDependencies.edges[].node.components` | `integer` | yes |
| `groupedDependencies.edges[].node.license` | `string` | yes |
| `groupedDependencies.edges[].node.licenses` | `integer` | yes |
| `groupedDependencies.edges[].node.subtype` | `string` | yes |
| `groupedDependencies.edges[].node.type` | `string` | yes |
| `groupedDependencies.edges[].node.vendor` | `string` | yes |
| `groupedDependencies.edges[].node.vendors` | `integer` | yes |
| `groupedDependencies.pageInfo` | `object` | no |
| `groupedDependencies.pageInfo.endCursor` | `string` | yes |
| `groupedDependencies.pageInfo.hasNextPage` | `boolean` | no |
| `groupedDependencies.pageInfo.hasPreviousPage` | `boolean` | no |
| `groupedDependencies.pageInfo.startCursor` | `string` | yes |
| `groupedDependencies.pageInfo.totalCount` | `integer` | yes |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    GroupedDependenciesInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_grouped_dependencies(grouped_dependencies_args=GroupedDependenciesInput(composed_asset_id='composed_asset_123'))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
