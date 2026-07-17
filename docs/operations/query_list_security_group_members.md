<!-- Generated file: do not edit by hand -->

# query_list_security_group_members

List the users who are members of a specific security group.

## Parameters

| name | type | required |
| --- | --- | --- |
| `list_security_group_members_security_group_id` | `str` | `true` |
| `list_security_group_members_cursor` | `Union[Cursor, None, UnsetType]` | `false` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `listSecurityGroupMembers` | `object` | no |
| `listSecurityGroupMembers.edges[]` | `object` | yes |
| `listSecurityGroupMembers.edges[].cursor` | `string` | yes |
| `listSecurityGroupMembers.edges[].node` | `object` | yes |
| `listSecurityGroupMembers.edges[].node.accessibleAssetCount` | `integer` | yes |
| `listSecurityGroupMembers.edges[].node.createdTime` | `string` | yes |
| `listSecurityGroupMembers.edges[].node.displayName` | `string` | yes |
| `listSecurityGroupMembers.edges[].node.email` | `string` | yes |
| `listSecurityGroupMembers.edges[].node.lastSeenTime` | `string` | yes |
| `listSecurityGroupMembers.edges[].node.source` | `SecurityGroupMemberSource` | no |
| `listSecurityGroupMembers.edges[].node.userId` | `string` | yes |
| `listSecurityGroupMembers.pageInfo` | `object` | no |
| `listSecurityGroupMembers.pageInfo.endCursor` | `string` | yes |
| `listSecurityGroupMembers.pageInfo.hasNextPage` | `boolean` | no |
| `listSecurityGroupMembers.pageInfo.hasPreviousPage` | `boolean` | no |
| `listSecurityGroupMembers.pageInfo.startCursor` | `string` | yes |
| `listSecurityGroupMembers.pageInfo.totalCount` | `integer` | yes |

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
        resp = client.query_list_security_group_members(list_security_group_members_security_group_id='group_123', list_security_group_members_cursor=Cursor())
        # Responses are typed Pydantic models: read fields as attributes.
        for edge in resp.list_security_group_members.edges or []:
            node = edge.node
            print(node.accessible_asset_count, node.created_time, node.display_name)


if __name__ == "__main__":
    main()
```
