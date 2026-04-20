<!-- Generated file: do not edit by hand -->

# query_get_ai_model_data

Retrieve configuration and metadata for a specific AI model integration.

## Parameters

| name | type | required |
| --- | --- | --- |
| `get_ai_model_data_args` | `GetAiModelDataInput` | `true` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `getAiModelData` | `object` | yes |
| `getAiModelData.aiModelData` | `object` | yes |
| `getAiModelData.aiModelData.aiModelArchitectureType` | `string` | yes |
| `getAiModelData.aiModelData.author` | `string` | yes |
| `getAiModelData.aiModelData.description` | `string` | yes |
| `getAiModelData.aiModelData.license` | `string` | yes |
| `getAiModelData.aiModelData.name` | `string` | yes |
| `getAiModelData.aiModelData.organization` | `string` | yes |
| `getAiModelData.aiModelData.version` | `string` | yes |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    GetAiModelDataInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_get_ai_model_data(get_ai_model_data_args=GetAiModelDataInput(composed_asset_id='composed_asset_123', component_id='id_123'))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
