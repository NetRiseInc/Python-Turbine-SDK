<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# mutation_delete_sso_group_mapping

[Back to the index](../README.md)

Remove one IdP group mapping rule.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |
| `delete_sso_group_mapping_args` | `DeleteSsoGroupMappingInput` | `true` |

## Response fields

Typed attributes on the response model.

| Field | Type | Nullable |
| --- | --- | --- |
| `deleteSsoGroupMapping` | `object` | no |
| `deleteSsoGroupMapping.mappingId` | `string` | no |
| `deleteSsoGroupMapping.success` | `boolean` | no |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    DeleteSsoGroupMappingInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.mutation_delete_sso_group_mapping(delete_sso_group_mapping_args=DeleteSsoGroupMappingInput(mapping_id='id_123'))
        # Responses are typed Pydantic models: read fields as attributes.
        print(resp.delete_sso_group_mapping.mapping_id, resp.delete_sso_group_mapping.success)


if __name__ == "__main__":
    main()
```
