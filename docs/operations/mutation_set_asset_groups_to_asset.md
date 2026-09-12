<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# mutation_set_asset_groups_to_asset

[Back to the index](../README.md)

Replace an asset's group memberships.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |
| `set_asset_groups_to_asset_args` | `SetAssetGroupsToAssetInput` | `true` |

## Response fields

Typed attributes on the response model.

| Field | Type | Nullable |
| --- | --- | --- |
| `setAssetGroupsToAsset` | `boolean` | no |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    SetAssetGroupsToAssetInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.mutation_set_asset_groups_to_asset(set_asset_groups_to_asset_args=SetAssetGroupsToAssetInput(asset_id='asset_123'))
        # Responses are typed Pydantic models: read fields as attributes.
        print(resp.set_asset_groups_to_asset)


if __name__ == "__main__":
    main()
```
