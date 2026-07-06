<!-- Generated file: do not edit by hand -->

# query_private_key_external_filters

Retrieve available filter options for private key queries.

## Parameters

| name | type | required |
| --- | --- | --- |
| `private_key_external_filters_args` | `PrivateKeyExternalFiltersInput` | `true` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `privateKeyExternalFilters` | `object` | yes |
| `privateKeyExternalFilters.totalClassical` | `integer` | yes |
| `privateKeyExternalFilters.totalPqc` | `integer` | yes |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    PrivateKeyExternalFiltersInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_private_key_external_filters(private_key_external_filters_args=PrivateKeyExternalFiltersInput(asset_id='asset_123'))
        # Responses are typed Pydantic models: read fields as attributes.
        print(resp.private_key_external_filters.total_classical, resp.private_key_external_filters.total_pqc)


if __name__ == "__main__":
    main()
```
