<!-- Generated file: do not edit by hand -->

# query_metrics

View organization-wide statistics on asset counts, processing, and risk.

## Parameters

| name | type | required |
| --- | --- | --- |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `metrics` | `object` | no |
| `metrics.assetsByRiskCategory[]` | `object` | no |
| `metrics.assetsByRiskCategory[].count` | `integer` | no |
| `metrics.assetsByRiskCategory[].status` | `string` | yes |
| `metrics.assetsByStatus[]` | `object` | no |
| `metrics.assetsByStatus[].count` | `integer` | no |
| `metrics.assetsByStatus[].status` | `string` | yes |
| `metrics.assetsCount[]` | `object` | no |
| `metrics.assetsCount[].count` | `integer` | no |
| `metrics.assetsCount[].status` | `string` | yes |
| `metrics.filesCount[]` | `object` | no |
| `metrics.filesCount[].count` | `integer` | no |
| `metrics.filesCount[].status` | `string` | yes |
| `metrics.vulnerabilitiesCount[]` | `object` | no |
| `metrics.vulnerabilitiesCount[].count` | `integer` | no |
| `metrics.vulnerabilitiesCount[].status` | `string` | yes |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_metrics()
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
