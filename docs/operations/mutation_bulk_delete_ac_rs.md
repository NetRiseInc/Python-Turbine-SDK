<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# mutation_bulk_delete_ac_rs

[Back to the index](../README.md)

Delete many access control records; missing ones count as success.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |
| `bulk_delete_ac_rs_args` | `BulkDeleteAcrsInput` | `true` |

## Response fields

Typed attributes on the response model.

| Field | Type | Nullable |
| --- | --- | --- |
| `bulkDeleteACRs` | `object` | no |
| `bulkDeleteACRs.success` | `boolean` | no |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    BulkDeleteAcrsInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.mutation_bulk_delete_ac_rs(bulk_delete_ac_rs_args=BulkDeleteAcrsInput(acr_ids=['value']))
        # Responses are typed Pydantic models: read fields as attributes.
        print(resp.bulk_delete_ac_rs.success)


if __name__ == "__main__":
    main()
```
