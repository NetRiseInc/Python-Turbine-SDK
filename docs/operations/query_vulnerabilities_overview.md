<!-- Generated file: do not edit by hand -->

# query_vulnerabilities_overview

Get a summary of vulnerability counts and severity across assets.

## Parameters

| name | type | required |
| --- | --- | --- |
| `vulnerabilities_overview_args` | `VulnerabilityOverviewInput` | `true` |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    Cursor,
    VulnerabilityOverviewInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_vulnerabilities_overview(vulnerabilities_overview_args=VulnerabilityOverviewInput(cursor=Cursor()))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
