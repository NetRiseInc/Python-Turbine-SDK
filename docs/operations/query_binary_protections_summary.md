<!-- Generated file: do not edit by hand -->

# query_binary_protections_summary

## Parameters

| name | type | required |
| --- | --- | --- |
| `binary_protections_summary_args` | `BinaryProtectionsSummaryInput` | `true` |

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
        resp = client.query_binary_protections_summary(binary_protections_summary_args=BinaryProtectionsSummaryInput(composed_asset_id='asset_123'))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
