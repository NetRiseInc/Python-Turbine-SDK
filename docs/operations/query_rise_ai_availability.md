<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# query_rise_ai_availability

[Back to the index](../README.md)

Check RiseAI eligibility and status for an asset.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |
| `rise_ai_availability_args` | `RiseAIAnalysisDataInput` | `true` |

## Response fields

Typed attributes on the response model.

| Field | Type | Nullable |
| --- | --- | --- |
| `riseAIAvailability` | `object` | no |
| `riseAIAvailability.available` | `boolean` | yes |
| `riseAIAvailability.eligible` | `boolean` | yes |
| `riseAIAvailability.status` | `RiseAIStatus` | yes |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    RiseAIAnalysisDataInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_rise_ai_availability(rise_ai_availability_args=RiseAIAnalysisDataInput(asset_id='asset_123'))
        # Responses are typed Pydantic models: read fields as attributes.
        print(resp.rise_ai_availability.status)


if __name__ == "__main__":
    main()
```
