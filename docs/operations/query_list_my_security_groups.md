<!-- Generated file: do not edit by hand -->

# query_list_my_security_groups

List the security groups the calling user belongs to.

## Parameters

| name | type | required |
| --- | --- | --- |
| `list_my_security_groups_cursor` | `Union[Cursor, None, UnsetType]` | `false` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `listMySecurityGroups` | `object` | no |
| `listMySecurityGroups.edges[]` | `object` | yes |
| `listMySecurityGroups.edges[].cursor` | `string` | yes |
| `listMySecurityGroups.edges[].node` | `object` | yes |
| `listMySecurityGroups.edges[].node.id` | `string` | no |
| `listMySecurityGroups.edges[].node.createdBy` | `string` | yes |
| `listMySecurityGroups.edges[].node.createdTime` | `string` | yes |
| `listMySecurityGroups.edges[].node.description` | `string` | yes |
| `listMySecurityGroups.edges[].node.lastModifiedTime` | `string` | yes |
| `listMySecurityGroups.edges[].node.lastSeenTime` | `string` | yes |
| `listMySecurityGroups.edges[].node.memberCount` | `integer` | yes |
| `listMySecurityGroups.edges[].node.members[]` | `object` | no |
| `listMySecurityGroups.edges[].node.members[].displayName` | `string` | yes |
| `listMySecurityGroups.edges[].node.members[].email` | `string` | no |
| `listMySecurityGroups.edges[].node.members[].userId` | `string` | no |
| `listMySecurityGroups.edges[].node.name` | `string` | no |
| `listMySecurityGroups.pageInfo` | `object` | no |
| `listMySecurityGroups.pageInfo.endCursor` | `string` | yes |
| `listMySecurityGroups.pageInfo.hasNextPage` | `boolean` | no |
| `listMySecurityGroups.pageInfo.hasPreviousPage` | `boolean` | no |
| `listMySecurityGroups.pageInfo.startCursor` | `string` | yes |
| `listMySecurityGroups.pageInfo.totalCount` | `integer` | yes |

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
        resp = client.query_list_my_security_groups(list_my_security_groups_cursor=Cursor())
        # Responses are typed Pydantic models: read fields as attributes.
        for edge in resp.list_my_security_groups.edges or []:
            node = edge.node
            print(node.id, node.name, node.created_by)


if __name__ == "__main__":
    main()
```
