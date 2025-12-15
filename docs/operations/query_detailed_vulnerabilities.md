<!-- Generated file: do not edit by hand -->

# query_detailed_vulnerabilities

## Parameters

| name | type | required |
| --- | --- | --- |
| `detailed_vulnerabilities_args` | `PaginatedDetailedVulnerabilitiesInput` | `true` |

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
