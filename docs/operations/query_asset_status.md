<!-- Generated file: do not edit by hand -->

# query_asset_status

Check if an asset is currently processing or has finished.

## Parameters

| name | type | required |
| --- | --- | --- |
| `asset_status_args` | `AssetStatusInput` | `true` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `assetStatus` | `object` | no |
| `assetStatus.assetId` | `string` | no |
| `assetStatus.hasRunningJob` | `boolean` | no |
| `assetStatus.lastUpdatedTime` | `string` | yes |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    AssetStatusInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_asset_status(asset_status_args=AssetStatusInput(asset_id='asset_123'))
        # Responses are typed Pydantic models: read fields as attributes.
        print(resp.asset_status.asset_id, resp.asset_status.has_running_job)


if __name__ == "__main__":
    main()
```
