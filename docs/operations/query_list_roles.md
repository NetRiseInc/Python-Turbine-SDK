<!-- Generated file: do not edit by hand -->

# query_list_roles

List all RBAC roles defined for the current organization.

## Parameters

| name | type | required |
| --- | --- | --- |
| `list_roles_cursor` | `Union[Cursor, None, UnsetType]` | `false` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `listRoles` | `object` | no |
| `listRoles.edges[]` | `object` | yes |
| `listRoles.edges[].cursor` | `string` | yes |
| `listRoles.edges[].node` | `object` | yes |
| `listRoles.edges[].node.id` | `string` | no |
| `listRoles.edges[].node.description` | `string` | yes |
| `listRoles.edges[].node.isBuiltin` | `boolean` | no |
| `listRoles.edges[].node.lastModifiedBy` | `string` | yes |
| `listRoles.edges[].node.lastModifiedByEmail` | `string` | yes |
| `listRoles.edges[].node.lastModifiedTime` | `string` | yes |
| `listRoles.edges[].node.name` | `string` | no |
| `listRoles.edges[].node.orgId` | `string` | no |
| `listRoles.edges[].node.permissions[]` | `string` | no |
| `listRoles.edges[].node.precedence` | `integer` | yes |
| `listRoles.pageInfo` | `object` | no |
| `listRoles.pageInfo.endCursor` | `string` | yes |
| `listRoles.pageInfo.hasNextPage` | `boolean` | no |
| `listRoles.pageInfo.hasPreviousPage` | `boolean` | no |
| `listRoles.pageInfo.startCursor` | `string` | yes |
| `listRoles.pageInfo.totalCount` | `integer` | yes |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    Cursor,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_list_roles(list_roles_cursor=Cursor())
        # Responses are typed Pydantic models: read fields as attributes.
        for edge in resp.list_roles.edges or []:
            node = edge.node
            print(node.id, node.name, node.description)


if __name__ == "__main__":
    main()
```
