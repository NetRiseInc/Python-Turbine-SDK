<!-- Generated file: do not edit by hand -->

# mutation_remediate_all_asset_vulnerabilities

## Parameters

| name | type | required |
| --- | --- | --- |
| `remediate_all_asset_vulnerabilities_args` | `CreateAllAssetVulnerabilitiesRemediationInput` | `true` |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    CreateAllAssetVulnerabilitiesRemediationInput,
    VulnerabilityFilter,
)
from netrise_turbine_sdk_graphql.enums import (
    VexStatus,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.mutation_remediate_all_asset_vulnerabilities(remediate_all_asset_vulnerabilities_args=CreateAllAssetVulnerabilitiesRemediationInput(asset_id='asset_123', vulnerability_filter=VulnerabilityFilter(), status=VexStatus.UNSPECIFIED))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
