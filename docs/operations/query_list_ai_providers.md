<!-- Generated file: do not edit by hand -->

# query_list_ai_providers

List available AI provider integrations and their current status.

## Parameters

| name | type | required |
| --- | --- | --- |
| `list_ai_providers_args` | `Union[ListAiProvidersInput, None, UnsetType]` | `false` |

## Response Schema

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
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
