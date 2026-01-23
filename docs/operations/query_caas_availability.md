<!-- Generated file: do not edit by hand -->

# query_caas_availability

Check for the availability of the RISE AI analysis report.

## Parameters

| name | type | required |
| --- | --- | --- |
| `caas_availability_args` | `RiseAIAnalysisDataInput` | `true` |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    RiseAIAnalysisDataInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_caas_availability(caas_availability_args=RiseAIAnalysisDataInput(asset_id='asset_123'))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
