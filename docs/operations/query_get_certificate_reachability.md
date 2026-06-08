<!-- Generated file: do not edit by hand -->

# query_get_certificate_reachability

Determine whether discovered certificates are reachable via executable scripts or system paths.

## Parameters

| name | type | required |
| --- | --- | --- |
| `get_certificate_reachability_args` | `GetCertificateReachabilityInput` | `true` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `getCertificateReachability[]` | `object` | yes |
| `getCertificateReachability[].cveId` | `string` | yes |
| `getCertificateReachability[].entryPoint` | `string` | yes |
| `getCertificateReachability[].entryType` | `EvidenceEntryType` | yes |
| `getCertificateReachability[].scripts[]` | `object` | yes |
| `getCertificateReachability[].scripts[].detail` | `string` | yes |
| `getCertificateReachability[].scripts[].edgeType` | `EvidenceEdgeType` | yes |
| `getCertificateReachability[].scripts[].invocation` | `string` | yes |
| `getCertificateReachability[].scripts[].path` | `string` | yes |
| `getCertificateReachability[].user` | `string` | yes |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    GetCertificateReachabilityInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_get_certificate_reachability(get_certificate_reachability_args=GetCertificateReachabilityInput(composed_asset_id='composed_asset_123', file_path='./path/to/file', sha_256='value'))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
