<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# mutation_delete_asset_comparison_report

[Back to the index](../README.md)

Delete an asset comparison report by ID.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |
| `delete_asset_comparison_report_args` | `DeleteAssetComparisonReportInput` | `true` |

## Response fields

Typed attributes on the response model.

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
        # Responses are typed Pydantic models: read fields as attributes.
        print(resp.delete_asset_comparison_report)


if __name__ == "__main__":
    main()
```
