<!-- Generated file: do not edit by hand -->

# query_asset_group_analytics

View risk metrics and exploit counts for a specific group.

## Parameters

| name | type | required |
| --- | --- | --- |
| `asset_group_analytics_args` | `AssetGroupAnalyticsInput` | `true` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `assetGroupAnalytics` | `object` | yes |
| `assetGroupAnalytics.crackedCredentials` | `integer` | yes |
| `assetGroupAnalytics.exploits` | `integer` | yes |
| `assetGroupAnalytics.invalidCertificates` | `integer` | yes |
| `assetGroupAnalytics.misconfigurations` | `integer` | yes |
| `assetGroupAnalytics.totalComponents` | `integer` | yes |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    AssetGroupAnalyticsInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_asset_group_analytics(asset_group_analytics_args=AssetGroupAnalyticsInput(group_id='group_123'))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
