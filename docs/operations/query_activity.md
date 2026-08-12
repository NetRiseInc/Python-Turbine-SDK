<!-- Generated file: do not edit by hand -->

# query_activity

Retrieve a comprehensive log of actions and events for assets.

> **Prefer `sdk.iter_activity(...)`** — same data with automatic pagination, filter kwargs, and no cursor plumbing.

## Parameters

| name | type | required |
| --- | --- | --- |
| `activity_args` | `ActivityInput` | `true` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `activity` | `object` | no |
| `activity.edges[]` | `object` | yes |
| `activity.edges[].cursor` | `string` | yes |
| `activity.edges[].node` | `object` | yes |
| `activity.edges[].node.id` | `string` | no |
| `activity.edges[].node.activityType` | `ActivityType` | no |
| `activity.edges[].node.assetId` | `string` | yes |
| `activity.edges[].node.assetName` | `string` | yes |
| `activity.edges[].node.correlationId` | `string` | no |
| `activity.edges[].node.createdAt` | `string` | no |
| `activity.edges[].node.description` | `string` | yes |
| `activity.edges[].node.entity` | `typing.Union[netrise_turbine_sdk_graphql.query_activity.QueryActivityActivityEdgesNodeEntityAssetCreatedPayload, netrise_turbine_sdk_graphql.query_activity.QueryActivityActivityEdgesNodeEntityAssetAnalysisCompletedPayload, netrise_turbine_sdk_graphql.query_activity.QueryActivityActivityEdgesNodeEntityAssetChangedPayload, netrise_turbine_sdk_graphql.query_activity.QueryActivityActivityEdgesNodeEntityAssetRiskChangedPayload, netrise_turbine_sdk_graphql.query_activity.QueryActivityActivityEdgesNodeEntityIdentificationAddedPayload, netrise_turbine_sdk_graphql.query_activity.QueryActivityActivityEdgesNodeEntityIdentificationRemovedPayload, netrise_turbine_sdk_graphql.query_activity.QueryActivityActivityEdgesNodeEntityVulnerabilityAddedPayload, netrise_turbine_sdk_graphql.query_activity.QueryActivityActivityEdgesNodeEntityVulnerabilityRemediatedPayload, netrise_turbine_sdk_graphql.query_activity.QueryActivityActivityEdgesNodeEntityVulnerabilityUpdatedPayload, netrise_turbine_sdk_graphql.query_activity.QueryActivityActivityEdgesNodeEntityVulnerabilityRemovedPayload, netrise_turbine_sdk_graphql.query_activity.QueryActivityActivityEdgesNodeEntityMisconfigChangedPayload, netrise_turbine_sdk_graphql.query_activity.QueryActivityActivityEdgesNodeEntityAssetGroupAddedPayload, netrise_turbine_sdk_graphql.query_activity.QueryActivityActivityEdgesNodeEntityAssetGroupRemovedPayload, netrise_turbine_sdk_graphql.query_activity.QueryActivityActivityEdgesNodeEntitySecretRemediatedPayload, netrise_turbine_sdk_graphql.query_activity.QueryActivityActivityEdgesNodeEntityLicenseIssueRemediatedPayload, netrise_turbine_sdk_graphql.query_activity.QueryActivityActivityEdgesNodeEntityGroupCreatedPayload, netrise_turbine_sdk_graphql.query_activity.QueryActivityActivityEdgesNodeEntityGroupUpdatedPayload, netrise_turbine_sdk_graphql.query_activity.QueryActivityActivityEdgesNodeEntityGroupDeletedPayload, netrise_turbine_sdk_graphql.query_activity.QueryActivityActivityEdgesNodeEntityGroupMembershipChangedPayload, netrise_turbine_sdk_graphql.query_activity.QueryActivityActivityEdgesNodeEntityOrgSettingsUpdatedPayload, netrise_turbine_sdk_graphql.query_activity.QueryActivityActivityEdgesNodeEntityUnspecifiedPayload]` | no |
| `activity.edges[].node.entityType` | `ActivityEntityType` | no |
| `activity.edges[].node.orgId` | `string` | yes |
| `activity.edges[].node.orgName` | `string` | yes |
| `activity.edges[].node.user` | `string` | no |
| `activity.pageInfo` | `object` | no |
| `activity.pageInfo.endCursor` | `string` | yes |
| `activity.pageInfo.hasNextPage` | `boolean` | no |
| `activity.pageInfo.hasPreviousPage` | `boolean` | no |
| `activity.pageInfo.startCursor` | `string` | yes |
| `activity.pageInfo.totalCount` | `integer` | yes |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    ActivityInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_activity(activity_args=ActivityInput(asset_id='asset_123'))
        # Responses are typed Pydantic models: read fields as attributes.
        for edge in resp.activity.edges or []:
            node = edge.node
            print(node.id, node.activity_type, node.asset_id)


if __name__ == "__main__":
    main()
```
