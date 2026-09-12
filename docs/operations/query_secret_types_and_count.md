<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# query_secret_types_and_count

[Back to the index](../README.md)

List secret types with occurrence counts.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |
| `secret_types_and_count_args` | `SecretTypesAndCountInput` | `true` |

## Response fields

Typed attributes on the response model.

| Field | Type | Nullable |
| --- | --- | --- |
| `secretTypesAndCount` | `object` | yes |
| `secretTypesAndCount.totalTypes` | `integer` | yes |
| `secretTypesAndCount.typeCounts[]` | `object` | yes |
| `secretTypesAndCount.typeCounts[].count` | `integer` | yes |
| `secretTypesAndCount.typeCounts[].type` | `SecretType` | yes |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    SecretTypesAndCountInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_secret_types_and_count(secret_types_and_count_args=SecretTypesAndCountInput(asset_id='asset_123'))
        # Responses are typed Pydantic models: read fields as attributes.
        for item in resp.secret_types_and_count.type_counts or []:
            print(item.count, item.type)


if __name__ == "__main__":
    main()
```
