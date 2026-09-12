<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# mutation_remove_assets_from_asset_group

[Back to the index](../README.md)

Remove selected assets from an asset group.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |
| `remove_assets_from_asset_group_args` | `RemoveAssetsFromAssetGroupInput` | `true` |

## Response fields

Typed attributes on the response model.

| Field | Type | Nullable |
| --- | --- | --- |
| `removeAssetsFromAssetGroup` | `boolean` | no |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    RemoveAssetsFromAssetGroupInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.mutation_remove_assets_from_asset_group(remove_assets_from_asset_group_args=RemoveAssetsFromAssetGroupInput(id='id_123', asset_ids=['value']))
        # Responses are typed Pydantic models: read fields as attributes.
        print(resp.remove_assets_from_asset_group)


if __name__ == "__main__":
    main()
```
