<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# mutation_add_assets_to_asset_group

[Back to the index](../README.md)

Add assets to an existing asset group.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |
| `add_assets_to_asset_group_args` | `AddAssetsToAssetGroupInput` | `true` |

## Response fields

Typed attributes on the response model.

| Field | Type | Nullable |
| --- | --- | --- |
| `addAssetsToAssetGroup` | `boolean` | no |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    AddAssetsToAssetGroupInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.mutation_add_assets_to_asset_group(add_assets_to_asset_group_args=AddAssetsToAssetGroupInput(id='id_123', asset_ids=['value']))
        # Responses are typed Pydantic models: read fields as attributes.
        print(resp.add_assets_to_asset_group)


if __name__ == "__main__":
    main()
```
