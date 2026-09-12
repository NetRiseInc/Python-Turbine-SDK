<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# query_certificate_external_filters

[Back to the index](../README.md)

List filter options for certificate queries.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |
| `certificate_external_filters_args` | `CertificateExternalFiltersInput` | `true` |

## Response fields

Typed attributes on the response model.

| Field | Type | Nullable |
| --- | --- | --- |
| `certificateExternalFilters` | `object` | yes |
| `certificateExternalFilters.totalClassical` | `integer` | yes |
| `certificateExternalFilters.totalPqc` | `integer` | yes |

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
        # Responses are typed Pydantic models: read fields as attributes.
        print(resp.certificate_external_filters.total_classical, resp.certificate_external_filters.total_pqc)


if __name__ == "__main__":
    main()
```
