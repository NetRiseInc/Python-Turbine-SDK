<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# query_get_sso_group_sync_summary

[Back to the index](../README.md)

Show recent SSO group-sync membership changes per group.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |
| `get_sso_group_sync_summary_security_group_ids` | `Union[list[str], None, UnsetType]` | `false` |

## Response fields

Typed attributes on the response model.

| Field | Type | Nullable |
| --- | --- | --- |
| `getSsoGroupSyncSummary` | `object` | no |
| `getSsoGroupSyncSummary.summaries[]` | `object` | no |
| `getSsoGroupSyncSummary.summaries[].lastAdded` | `integer` | no |
| `getSsoGroupSyncSummary.summaries[].lastRemoved` | `integer` | no |
| `getSsoGroupSyncSummary.summaries[].lastSyncedAt` | `string` | yes |
| `getSsoGroupSyncSummary.summaries[].securityGroupId` | `string` | no |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_get_sso_group_sync_summary()
        # Responses are typed Pydantic models: read fields as attributes.
        for item in resp.get_sso_group_sync_summary.summaries or []:
            print(item.last_added, item.last_removed, item.last_synced_at)


if __name__ == "__main__":
    main()
```
