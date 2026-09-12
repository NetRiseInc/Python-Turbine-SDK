<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# mutation_set_assets_to_asset_group

[Back to the index](../README.md)

Replace an asset group's member list.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |
| `set_assets_to_asset_group_args` | `SetAssetsToAssetGroupInput` | `true` |

## Response fields

Typed attributes on the response model.

| Field | Type | Nullable |
| --- | --- | --- |
| `setAssetsToAssetGroup` | `boolean` | no |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    SetAssetsToAssetGroupInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.mutation_set_assets_to_asset_group(set_assets_to_asset_group_args=SetAssetsToAssetGroupInput(group_id='group_123'))
        # Responses are typed Pydantic models: read fields as attributes.
        print(resp.set_assets_to_asset_group)


if __name__ == "__main__":
    main()
```
