<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# query_get_security_group

[Back to the index](../README.md)

Get one security group by ID.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |
| `get_security_group_security_group_id` | `str` | `true` |

## Response fields

Typed attributes on the response model.

| Field | Type | Nullable |
| --- | --- | --- |
| `getSecurityGroup` | `object` | yes |
| `getSecurityGroup.id` | `string` | no |
| `getSecurityGroup.createdBy` | `string` | yes |
| `getSecurityGroup.createdTime` | `string` | yes |
| `getSecurityGroup.description` | `string` | yes |
| `getSecurityGroup.lastModifiedTime` | `string` | yes |
| `getSecurityGroup.lastSeenTime` | `string` | yes |
| `getSecurityGroup.memberCount` | `integer` | yes |
| `getSecurityGroup.members[]` | `object` | no |
| `getSecurityGroup.members[].displayName` | `string` | yes |
| `getSecurityGroup.members[].email` | `string` | no |
| `getSecurityGroup.members[].userId` | `string` | no |
| `getSecurityGroup.name` | `string` | no |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_get_security_group(get_security_group_security_group_id='group_123')
        # Responses are typed Pydantic models: read fields as attributes.
        print(resp.get_security_group.id, resp.get_security_group.name)


if __name__ == "__main__":
    main()
```
