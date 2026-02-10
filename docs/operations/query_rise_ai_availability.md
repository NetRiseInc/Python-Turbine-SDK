<!-- Generated file: do not edit by hand -->

# query_rise_ai_availability

Check eligibility and status of RISE AI analysis for an asset.

## Parameters

| name | type | required |
| --- | --- | --- |
| `rise_ai_availability_args` | `RiseAIAnalysisDataInput` | `true` |

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
        resp = client.query_rise_ai_availability(rise_ai_availability_args=RiseAIAnalysisDataInput(asset_id='asset_123'))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
