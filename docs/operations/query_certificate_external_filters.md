<!-- Generated file: do not edit by hand -->

# query_certificate_external_filters

Retrieve available filter options for certificate queries.

## Parameters

| name | type | required |
| --- | --- | --- |
| `certificate_external_filters_args` | `CertificateExternalFiltersInput` | `true` |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    CertificateExternalFiltersInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_certificate_external_filters(certificate_external_filters_args=CertificateExternalFiltersInput(asset_id='asset_123'))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
