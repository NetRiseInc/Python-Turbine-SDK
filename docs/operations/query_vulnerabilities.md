<!-- Generated file: do not edit by hand -->

# query_vulnerabilities

## Parameters

| name | type | required |
| --- | --- | --- |
| `vulnerabilities_args` | `PaginatedVulnerabilitiesInput` | `true` |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    PaginatedVulnerabilitiesInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_vulnerabilities(vulnerabilities_args=PaginatedVulnerabilitiesInput(asset_id='asset_123'))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
