<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# mutation_remove_all_asset_groups_from_assets

[Back to the index](../README.md)

Detach every asset group from the given assets.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |
| `remove_all_asset_groups_from_assets_args` | `RemoveAllAssetGroupsFromAssetsInput` | `true` |

## Response fields

Typed attributes on the response model.

| Field | Type | Nullable |
| --- | --- | --- |
| `removeAllAssetGroupsFromAssets` | `boolean` | no |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    RemoveAllAssetGroupsFromAssetsInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.mutation_remove_all_asset_groups_from_assets(remove_all_asset_groups_from_assets_args=RemoveAllAssetGroupsFromAssetsInput(asset_ids=['value']))
        # Responses are typed Pydantic models: read fields as attributes.
        print(resp.remove_all_asset_groups_from_assets)


if __name__ == "__main__":
    main()
```
