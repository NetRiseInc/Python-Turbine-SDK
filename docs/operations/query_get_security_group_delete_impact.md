<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# query_get_security_group_delete_impact

[Back to the index](../README.md)

Preview who loses access if a security group is deleted.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |
| `get_security_group_delete_impact_security_group_id` | `str` | `true` |

## Response fields

Typed attributes on the response model.

| Field | Type | Nullable |
| --- | --- | --- |
| `getSecurityGroupDeleteImpact` | `object` | no |
| `getSecurityGroupDeleteImpact.totalMembers` | `integer` | no |
| `getSecurityGroupDeleteImpact.usersWhoLoseAll[]` | `object` | no |
| `getSecurityGroupDeleteImpact.usersWhoLoseAll[].displayName` | `string` | yes |
| `getSecurityGroupDeleteImpact.usersWhoLoseAll[].email` | `string` | no |
| `getSecurityGroupDeleteImpact.usersWhoLoseAll[].userId` | `string` | no |
| `getSecurityGroupDeleteImpact.usersWhoRetain[]` | `object` | no |
| `getSecurityGroupDeleteImpact.usersWhoRetain[].displayName` | `string` | yes |
| `getSecurityGroupDeleteImpact.usersWhoRetain[].email` | `string` | no |
| `getSecurityGroupDeleteImpact.usersWhoRetain[].userId` | `string` | no |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_get_security_group_delete_impact(get_security_group_delete_impact_security_group_id='group_123')
        # Responses are typed Pydantic models: read fields as attributes.
        for item in resp.get_security_group_delete_impact.users_who_lose_all or []:
            print(item.display_name, item.email, item.user_id)


if __name__ == "__main__":
    main()
```
