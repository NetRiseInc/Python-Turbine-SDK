<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# mutation_submit_rise_ai_analysis

[Back to the index](../README.md)

Request a RiseAI analysis for an eligible asset.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |
| `submit_rise_ai_analysis_args` | `RiseAIAnalysisDataInput` | `true` |

## Response fields

Typed attributes on the response model.

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
        # Responses are typed Pydantic models: read fields as attributes.
        print(resp.submit_rise_ai_analysis.status)


if __name__ == "__main__":
    main()
```
