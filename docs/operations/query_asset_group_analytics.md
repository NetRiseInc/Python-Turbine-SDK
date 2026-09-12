<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# query_asset_group_analytics

[Back to the index](../README.md)

Get risk metrics for one asset group.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |
| `asset_group_analytics_args` | `AssetGroupAnalyticsInput` | `true` |

## Response fields

Typed attributes on the response model.

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
        # Responses are typed Pydantic models: read fields as attributes.
        print(resp.asset_group_analytics.cracked_credentials, resp.asset_group_analytics.exploits)


if __name__ == "__main__":
    main()
```
