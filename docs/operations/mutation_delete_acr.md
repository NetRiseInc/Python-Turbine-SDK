<!-- Generated file: do not edit by hand -->

# mutation_delete_acr

Delete a single access control record, revoking the associated grant.

## Parameters

| name | type | required |
| --- | --- | --- |
| `delete_acr_args` | `DeleteAcrInput` | `true` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `deleteACR` | `object` | no |
| `deleteACR.acrId` | `string` | no |
| `deleteACR.success` | `boolean` | no |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    DeleteAcrInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.mutation_delete_acr(delete_acr_args=DeleteAcrInput(acr_id='id_123'))
        # Responses are typed Pydantic models: read fields as attributes.
        print(resp.delete_acr.acr_id, resp.delete_acr.success)


if __name__ == "__main__":
    main()
```
