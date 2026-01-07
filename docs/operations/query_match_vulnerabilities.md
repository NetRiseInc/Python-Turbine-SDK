<!-- Generated file: do not edit by hand -->

# query_match_vulnerabilities

Find specific vulnerabilities matching a provided component identifier or package.

## Parameters

| name | type | required |
| --- | --- | --- |
| `match_vulnerabilities_args` | `MatchVulnerabilitiesInput` | `true` |

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
        resp = client.query_match_vulnerabilities(match_vulnerabilities_args=MatchVulnerabilitiesInput(identifier='example'))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
