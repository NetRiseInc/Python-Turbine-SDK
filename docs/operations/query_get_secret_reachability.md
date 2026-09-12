<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# query_get_secret_reachability

[Back to the index](../README.md)

Check whether secrets are reachable via paths or scripts.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |
| `get_secret_reachability_args` | `GetSecretReachabilityInput` | `true` |

## Response fields

Typed attributes on the response model.

| Field | Type | Nullable |
| --- | --- | --- |
| `getSecretReachability[]` | `object` | yes |
| `getSecretReachability[].cveId` | `string` | yes |
| `getSecretReachability[].entryPoint` | `string` | yes |
| `getSecretReachability[].entryType` | `EvidenceEntryType` | yes |
| `getSecretReachability[].scripts[]` | `object` | yes |
| `getSecretReachability[].scripts[].detail` | `string` | yes |
| `getSecretReachability[].scripts[].edgeType` | `EvidenceEdgeType` | yes |
| `getSecretReachability[].scripts[].invocation` | `string` | yes |
| `getSecretReachability[].scripts[].path` | `string` | yes |
| `getSecretReachability[].user` | `string` | yes |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    GetSecretReachabilityInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_get_secret_reachability(get_secret_reachability_args=GetSecretReachabilityInput(composed_asset_id='composed_asset_123', secret_id='id_123'))
        # Responses are typed Pydantic models: read fields as attributes.
        for item in resp.get_secret_reachability or []:
            print(item.cve_id, item.entry_point, item.entry_type)


if __name__ == "__main__":
    main()
```
