<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# query_asset_status

[Back to the index](../README.md)

Check whether an asset is still processing.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |
| `asset_status_args` | `AssetStatusInput` | `true` |

## Response fields

Typed attributes on the response model.

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
