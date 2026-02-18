<!-- Generated file: do not edit by hand -->

# query_public_key_external_filters

Retrieve available filter options for public key queries.

## Parameters

| name | type | required |
| --- | --- | --- |
| `public_key_external_filters_args` | `PublicKeyExternalFiltersInput` | `true` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `publicKeyExternalFilters` | `object` | yes |
| `publicKeyExternalFilters.totalClassical` | `integer` | yes |
| `publicKeyExternalFilters.totalPqc` | `integer` | yes |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    PublicKeyExternalFiltersInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_public_key_external_filters(public_key_external_filters_args=PublicKeyExternalFiltersInput(asset_id='asset_123'))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
