<!-- Generated file: do not edit by hand -->

# query_secrets_summary

Get a high-level overview of secret findings and exposure metrics.

## Parameters

| name | type | required |
| --- | --- | --- |
| `secrets_summary_args` | `SecretsSummaryInput` | `true` |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    SecretsSummaryInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_secrets_summary(secrets_summary_args=SecretsSummaryInput(asset_id='asset_123'))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
