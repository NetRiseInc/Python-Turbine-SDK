<!-- Generated file: do not edit by hand -->

# mutation_create_asset_comparison_report

Create a new comparison report to diff vulnerabilities and components between two assets.

## Parameters

| name | type | required |
| --- | --- | --- |
| `create_asset_comparison_report_args` | `CreateAssetComparisonReportInput` | `true` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `createAssetComparisonReport` | `object` | no |
| `createAssetComparisonReport.jobId` | `string` | no |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    CreateAssetComparisonReportInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.mutation_create_asset_comparison_report(create_asset_comparison_report_args=CreateAssetComparisonReportInput(asset_a='value', asset_b='value'))
        # Responses are typed Pydantic models: read fields as attributes.
        print(resp.create_asset_comparison_report.job_id)


if __name__ == "__main__":
    main()
```
