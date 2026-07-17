<!-- Generated file: do not edit by hand -->

# query_list_security_groups

List all RBAC security groups defined for the current organization.

## Parameters

| name | type | required |
| --- | --- | --- |
| `list_security_groups_cursor` | `Union[Cursor, None, UnsetType]` | `false` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `listSecurityGroups` | `object` | no |
| `listSecurityGroups.edges[]` | `object` | yes |
| `listSecurityGroups.edges[].cursor` | `string` | yes |
| `listSecurityGroups.edges[].node` | `object` | yes |
| `listSecurityGroups.edges[].node.id` | `string` | no |
| `listSecurityGroups.edges[].node.createdBy` | `string` | yes |
| `listSecurityGroups.edges[].node.createdTime` | `string` | yes |
| `listSecurityGroups.edges[].node.description` | `string` | yes |
| `listSecurityGroups.edges[].node.lastModifiedTime` | `string` | yes |
| `listSecurityGroups.edges[].node.lastSeenTime` | `string` | yes |
| `listSecurityGroups.edges[].node.memberCount` | `integer` | yes |
| `listSecurityGroups.edges[].node.members[]` | `object` | no |
| `listSecurityGroups.edges[].node.members[].displayName` | `string` | yes |
| `listSecurityGroups.edges[].node.members[].email` | `string` | no |
| `listSecurityGroups.edges[].node.members[].userId` | `string` | no |
| `listSecurityGroups.edges[].node.name` | `string` | no |
| `listSecurityGroups.pageInfo` | `object` | no |
| `listSecurityGroups.pageInfo.endCursor` | `string` | yes |
| `listSecurityGroups.pageInfo.hasNextPage` | `boolean` | no |
| `listSecurityGroups.pageInfo.hasPreviousPage` | `boolean` | no |
| `listSecurityGroups.pageInfo.startCursor` | `string` | yes |
| `listSecurityGroups.pageInfo.totalCount` | `integer` | yes |

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
        resp = client.query_list_security_groups(list_security_groups_cursor=Cursor())
        # Responses are typed Pydantic models: read fields as attributes.
        for edge in resp.list_security_groups.edges or []:
            node = edge.node
            print(node.id, node.name, node.created_by)


if __name__ == "__main__":
    main()
```
