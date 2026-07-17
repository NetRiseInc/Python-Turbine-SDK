<!-- Generated file: do not edit by hand -->

# query_get_my_permissions

Retrieve the flat union of permission IDs the calling user holds across all their access grants.

## Parameters

| name | type | required |
| --- | --- | --- |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `getMyPermissions` | `object` | no |
| `getMyPermissions.highestPrecedenceRole` | `string` | yes |
| `getMyPermissions.permissions[]` | `string` | no |
| `getMyPermissions.roles[]` | `object` | no |
| `getMyPermissions.roles[].atAsset` | `boolean` | no |
| `getMyPermissions.roles[].atAssetGroup` | `boolean` | no |
| `getMyPermissions.roles[].atOrg` | `boolean` | no |
| `getMyPermissions.roles[].roleName` | `string` | no |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_get_my_permissions()
        # Responses are typed Pydantic models: read fields as attributes.
        for item in resp.get_my_permissions.roles or []:
            print(item.at_asset, item.at_asset_group, item.at_org)


if __name__ == "__main__":
    main()
```
