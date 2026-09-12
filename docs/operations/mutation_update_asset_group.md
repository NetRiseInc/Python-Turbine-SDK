<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# mutation_update_asset_group

[Back to the index](../README.md)

Rename or update an asset group's description.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |
| `update_asset_group_args` | `UpdateAssetGroupInput` | `true` |

## Response fields

Typed attributes on the response model.

| Field | Type | Nullable |
| --- | --- | --- |
| `updateAssetGroup` | `object` | no |
| `updateAssetGroup.assetGroup` | `object` | yes |
| `updateAssetGroup.assetGroup.id` | `string` | no |
| `updateAssetGroup.assetGroup.description` | `string` | yes |
| `updateAssetGroup.assetGroup.name` | `string` | no |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    UpdateAssetGroupInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.mutation_update_asset_group(update_asset_group_args=UpdateAssetGroupInput(id='id_123', name='my-example'))
        # Responses are typed Pydantic models: read fields as attributes.
        print(resp.update_asset_group.asset_group.id, resp.update_asset_group.asset_group.name)


if __name__ == "__main__":
    main()
```
