<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# query_secrets_summary

[Back to the index](../README.md)

Get a summary of secret findings on an asset.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |
| `secrets_summary_args` | `SecretsSummaryInput` | `true` |

## Response fields

Typed attributes on the response model.

| Field | Type | Nullable |
| --- | --- | --- |
| `secretsSummary` | `object` | no |
| `secretsSummary.high` | `integer` | no |
| `secretsSummary.invalid` | `integer` | no |
| `secretsSummary.low` | `integer` | no |
| `secretsSummary.medium` | `integer` | no |
| `secretsSummary.total` | `integer` | no |

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
        # Responses are typed Pydantic models: read fields as attributes.
        print(resp.secrets_summary.high, resp.secrets_summary.invalid)


if __name__ == "__main__":
    main()
```
