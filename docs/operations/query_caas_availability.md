<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# query_caas_availability

[Back to the index](../README.md)

Check whether a RiseAI analysis report is available.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |
| `caas_availability_args` | `RiseAIAnalysisDataInput` | `true` |

## Response fields

Typed attributes on the response model.

| Field | Type | Nullable |
| --- | --- | --- |
| `caasAvailability` | `boolean` | no |

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
        resp = client.query_caas_availability(caas_availability_args=RiseAIAnalysisDataInput(asset_id='asset_123'))
        # Responses are typed Pydantic models: read fields as attributes.
        print(resp.caas_availability)


if __name__ == "__main__":
    main()
```
