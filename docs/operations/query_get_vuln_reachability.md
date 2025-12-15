<!-- Generated file: do not edit by hand -->

# query_get_vuln_reachability

## Parameters

| name | type | required |
| --- | --- | --- |
| `get_vuln_reachability_args` | `GetVulnReachabilityInput` | `true` |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    GetVulnReachabilityInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_get_vuln_reachability(get_vuln_reachability_args=GetVulnReachabilityInput(asset_id='asset_123', advisory_id='id_123', identification_ids=['example']))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
