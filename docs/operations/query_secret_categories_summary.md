<!-- Generated file: do not edit by hand -->

# query_secret_categories_summary

Get aggregated counts of secrets grouped by category type.

## Parameters

| name | type | required |
| --- | --- | --- |
| `secret_categories_summary_args` | `SecretCategoriesInput` | `true` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `secretCategoriesSummary[]` | `object` | yes |
| `secretCategoriesSummary[].category` | `SecretCategory` | yes |
| `secretCategoriesSummary[].categoryLabel` | `string` | yes |
| `secretCategoriesSummary[].remediationStatusCounts[]` | `object` | yes |
| `secretCategoriesSummary[].remediationStatusCounts[].count` | `integer` | yes |
| `secretCategoriesSummary[].remediationStatusCounts[].status` | `SecretRemediationStatus` | yes |
| `secretCategoriesSummary[].severityCounts[]` | `object` | yes |
| `secretCategoriesSummary[].severityCounts[].count` | `integer` | yes |
| `secretCategoriesSummary[].severityCounts[].severity` | `SecretSeverity` | yes |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    SecretCategoriesInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_secret_categories_summary(secret_categories_summary_args=SecretCategoriesInput(asset_id='asset_123'))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
