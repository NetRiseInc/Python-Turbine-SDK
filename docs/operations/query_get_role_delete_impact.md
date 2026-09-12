<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# query_get_role_delete_impact

[Back to the index](../README.md)

Preview who loses access if a custom role is deleted.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |
| `get_role_delete_impact_role_id` | `str` | `true` |

## Response fields

Typed attributes on the response model.

| Field | Type | Nullable |
| --- | --- | --- |
| `getRoleDeleteImpact` | `object` | no |
| `getRoleDeleteImpact.acrCount` | `integer` | no |
| `getRoleDeleteImpact.totalAffectedUsers` | `integer` | no |
| `getRoleDeleteImpact.usersWhoLoseAll[]` | `object` | no |
| `getRoleDeleteImpact.usersWhoLoseAll[].displayName` | `string` | yes |
| `getRoleDeleteImpact.usersWhoLoseAll[].email` | `string` | no |
| `getRoleDeleteImpact.usersWhoLoseAll[].userId` | `string` | no |
| `getRoleDeleteImpact.usersWhoRetain[]` | `object` | no |
| `getRoleDeleteImpact.usersWhoRetain[].displayName` | `string` | yes |
| `getRoleDeleteImpact.usersWhoRetain[].email` | `string` | no |
| `getRoleDeleteImpact.usersWhoRetain[].userId` | `string` | no |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_get_role_delete_impact(get_role_delete_impact_role_id='id_123')
        # Responses are typed Pydantic models: read fields as attributes.
        for item in resp.get_role_delete_impact.users_who_lose_all or []:
            print(item.display_name, item.email, item.user_id)


if __name__ == "__main__":
    main()
```
