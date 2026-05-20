<!-- Generated file: do not edit by hand -->

# mutation_delete_asset_comparison_report

Permanently delete an asset comparison report by its ID.

## Parameters

| name | type | required |
| --- | --- | --- |
| `delete_asset_comparison_report_args` | `DeleteAssetComparisonReportInput` | `true` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `deleteAssetComparisonReport` | `boolean` | no |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    DeleteAssetComparisonReportInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.mutation_delete_asset_comparison_report(delete_asset_comparison_report_args=DeleteAssetComparisonReportInput(report_id='id_123'))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
