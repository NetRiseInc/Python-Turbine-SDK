<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# query_secret_status_count

[Back to the index](../README.md)

Get secret counts grouped by remediation status.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |
| `secret_status_count_args` | `SecretStatusCountInput` | `true` |

## Response fields

Typed attributes on the response model.

| Field | Type | Nullable |
| --- | --- | --- |
| `secretStatusCount[]` | `object` | yes |
| `secretStatusCount[].count` | `integer` | yes |
| `secretStatusCount[].name` | `SecretRemediationStatus` | yes |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    SecretStatusCountInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_secret_status_count(secret_status_count_args=SecretStatusCountInput(asset_id='asset_123'))
        # Responses are typed Pydantic models: read fields as attributes.
        for item in resp.secret_status_count or []:
            print(item.name, item.count)


if __name__ == "__main__":
    main()
```
