<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# mutation_add_asset_groups_to_assets

[Back to the index](../README.md)

Attach asset groups to one or more assets.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |
| `add_asset_groups_to_assets_args` | `AddAssetGroupsToAssetsInput` | `true` |

## Response fields

Typed attributes on the response model.

| Field | Type | Nullable |
| --- | --- | --- |
| `addAssetGroupsToAssets` | `boolean` | no |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    AddAssetGroupsToAssetsInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.mutation_add_asset_groups_to_assets(add_asset_groups_to_assets_args=AddAssetGroupsToAssetsInput(asset_ids=['value']))
        # Responses are typed Pydantic models: read fields as attributes.
        print(resp.add_asset_groups_to_assets)


if __name__ == "__main__":
    main()
```
