<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# query_get_ai_model_data

[Back to the index](../README.md)

Get config and metadata for an AI model integration.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |
| `get_ai_model_data_args` | `GetAiModelDataInput` | `true` |

## Response fields

Typed attributes on the response model.

| Field | Type | Nullable |
| --- | --- | --- |
| `getAiModelData` | `object` | yes |
| `getAiModelData.aiModelData` | `object` | yes |
| `getAiModelData.aiModelData.aiArchitecture` | `string` | yes |
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
        # Responses are typed Pydantic models: read fields as attributes.
        print(resp.get_ai_model_data.ai_model_data.name, resp.get_ai_model_data.ai_model_data.version)


if __name__ == "__main__":
    main()
```
