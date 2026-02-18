<!-- Generated file: do not edit by hand -->

# query_rise_ai_analysis_data

Check for the contents of the RISE AI analysis report.

## Parameters

| name | type | required |
| --- | --- | --- |
| `rise_ai_analysis_data_args` | `RiseAIAnalysisDataInput` | `true` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `riseAIAnalysisData` | `object` | no |
| `riseAIAnalysisData.architectures[]` | `Architecture` | yes |
| `riseAIAnalysisData.components[]` | `object` | yes |
| `riseAIAnalysisData.components[].cpes[]` | `string` | no |
| `riseAIAnalysisData.components[].name` | `string` | no |
| `riseAIAnalysisData.components[].versions[]` | `string` | no |
| `riseAIAnalysisData.entropyData[]` | `object` | yes |
| `riseAIAnalysisData.entropyData[].description` | `string` | no |
| `riseAIAnalysisData.entropyData[].level` | `string` | no |
| `riseAIAnalysisData.entropyData[].percentage` | `float` | no |
| `riseAIAnalysisData.fileInfo` | `object` | yes |
| `riseAIAnalysisData.fileInfo.filename` | `string` | no |
| `riseAIAnalysisData.fileInfo.magic` | `string` | yes |
| `riseAIAnalysisData.fileInfo.sha256` | `string` | yes |
| `riseAIAnalysisData.fileInfo.size` | `integer` | yes |
| `riseAIAnalysisData.fileInfo.sizeFormatted` | `string` | yes |
| `riseAIAnalysisData.findingsCount` | `integer` | no |
| `riseAIAnalysisData.securityInsights` | `object` | yes |
| `riseAIAnalysisData.securityInsights.oldComponents[]` | `object` | no |
| `riseAIAnalysisData.securityInsights.oldComponents[].concern` | `string` | no |
| `riseAIAnalysisData.securityInsights.oldComponents[].name` | `string` | no |
| `riseAIAnalysisData.securityInsights.oldComponents[].version` | `string` | no |
| `riseAIAnalysisData.synopsis` | `string` | yes |
| `riseAIAnalysisData.totals` | `object` | yes |
| `riseAIAnalysisData.totals.architecturesCount` | `integer` | yes |
| `riseAIAnalysisData.totals.components` | `integer` | yes |
| `riseAIAnalysisData.totals.entropySections` | `integer` | yes |
| `riseAIAnalysisData.totals.highEntropyPct` | `float` | yes |
| `riseAIAnalysisData.totals.lowEntropyPct` | `float` | yes |
| `riseAIAnalysisData.totals.mediumEntropyPct` | `float` | yes |

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
        resp = client.query_rise_ai_analysis_data(rise_ai_analysis_data_args=RiseAIAnalysisDataInput(asset_id='asset_123'))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
