<!-- Generated file: do not edit by hand -->

# query_binary_protections_summary

Get aggregated counts of binary hardening features like NX or PIE.

## Parameters

| name | type | required |
| --- | --- | --- |
| `binary_protections_summary_args` | `BinaryProtectionsSummaryInput` | `true` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `binaryProtectionsSummary` | `object` | yes |
| `binaryProtectionsSummary.canaryDisabled` | `integer` | no |
| `binaryProtectionsSummary.canaryEnabled` | `integer` | no |
| `binaryProtectionsSummary.nxDisabled` | `integer` | no |
| `binaryProtectionsSummary.nxEnabled` | `integer` | no |
| `binaryProtectionsSummary.pieDisabled` | `integer` | no |
| `binaryProtectionsSummary.pieEnabled` | `integer` | no |
| `binaryProtectionsSummary.relroDisabled` | `integer` | no |
| `binaryProtectionsSummary.relroEnabled` | `integer` | no |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    BinaryProtectionsSummaryInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_binary_protections_summary(binary_protections_summary_args=BinaryProtectionsSummaryInput(composed_asset_id='composed_asset_123'))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
