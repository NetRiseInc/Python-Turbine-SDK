<!-- Generated file: do not edit by hand -->

# mutation_submit_rise_ai_analysis

Request a RISE AI analysis for an eligible asset to generate insights.

## Parameters

| name | type | required |
| --- | --- | --- |
| `submit_rise_ai_analysis_args` | `RiseAIAnalysisDataInput` | `true` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `submitRiseAIAnalysis` | `object` | no |
| `submitRiseAIAnalysis.status` | `RiseAIStatus` | yes |

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
        resp = client.mutation_submit_rise_ai_analysis(submit_rise_ai_analysis_args=RiseAIAnalysisDataInput(asset_id='asset_123'))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
