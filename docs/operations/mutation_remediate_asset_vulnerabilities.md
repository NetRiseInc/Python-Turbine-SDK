<!-- Generated file: do not edit by hand -->

# mutation_remediate_asset_vulnerabilities

Bulk apply VEX remediation status to multiple vulnerabilities on assets.

## Parameters

| name | type | required |
| --- | --- | --- |
| `remediate_asset_vulnerabilities_args` | `CreateAssetVulnerabilityRemediationsInput` | `true` |

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
