<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# mutation_delete_security_group

[Back to the index](../README.md)

Delete a security group from the organization.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |
| `delete_security_group_args` | `DeleteSecurityGroupInput` | `true` |

## Response fields

Typed attributes on the response model.

| Field | Type | Nullable |
| --- | --- | --- |
| `deleteSecurityGroup` | `object` | no |
| `deleteSecurityGroup.securityGroupId` | `string` | no |
| `deleteSecurityGroup.success` | `boolean` | no |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    DeleteSecurityGroupInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.mutation_delete_security_group(delete_security_group_args=DeleteSecurityGroupInput(security_group_id='group_123'))
        # Responses are typed Pydantic models: read fields as attributes.
        print(resp.delete_security_group.security_group_id, resp.delete_security_group.success)


if __name__ == "__main__":
    main()
```
