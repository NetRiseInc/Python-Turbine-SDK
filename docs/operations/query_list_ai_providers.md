<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# query_list_ai_providers

[Back to the index](../README.md)

List AI provider integrations and their status.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |
| `list_ai_providers_args` | `Union[ListAiProvidersInput, None, UnsetType]` | `false` |

## Response fields

Typed attributes on the response model.

| Field | Type | Nullable |
| --- | --- | --- |
| `listAiProviders` | `object` | yes |
| `listAiProviders.aiProviders[]` | `string` | no |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    ListAiProvidersInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_list_ai_providers(list_ai_providers_args=ListAiProvidersInput())
        # Responses are typed Pydantic models: read fields as attributes.
        for value in resp.list_ai_providers.ai_providers or []:
            print(value)


if __name__ == "__main__":
    main()
```
