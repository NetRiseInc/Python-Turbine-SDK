<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# mutation_delete_asset_group

[Back to the index](../README.md)

Delete an asset group; assets stay in the org.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |
| `delete_asset_group_args` | `DeleteAssetGroupInput` | `true` |

## Response fields

Typed attributes on the response model.

| Field | Type | Nullable |
| --- | --- | --- |
| `deleteAssetGroup` | `boolean` | no |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    DeleteAssetGroupInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.mutation_delete_asset_group(delete_asset_group_args=DeleteAssetGroupInput(id='id_123'))
        # Responses are typed Pydantic models: read fields as attributes.
        print(resp.delete_asset_group)


if __name__ == "__main__":
    main()
```
