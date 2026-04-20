<!-- Generated file: do not edit by hand -->

# query_misconfigurations_lite

List misconfigurations with trimmed fields — keeps check ID, name, severity, result, and correlation count; drops nested correlation objects.

## Parameters

| name | type | required |
| --- | --- | --- |
| `misconfigurations_args` | `MisconfigurationsInput` | `true` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `misconfigurations` | `object` | yes |
| `misconfigurations.edges[]` | `object` | yes |
| `misconfigurations.edges[].cursor` | `string` | no |
| `misconfigurations.edges[].node` | `object` | yes |
| `misconfigurations.edges[].node.checkId` | `string` | yes |
| `misconfigurations.edges[].node.displayName` | `string` | yes |
| `misconfigurations.edges[].node.category` | `MisconfigurationCategoryType` | yes |
| `misconfigurations.edges[].node.severity` | `MisconfigurationSeverityType` | yes |
| `misconfigurations.edges[].node.result` | `MisconfigurationStatusType` | yes |
| `misconfigurations.edges[].node.correlationsCount` | `integer` | yes |
| `misconfigurations.pageInfo` | `object` | yes |
| `misconfigurations.pageInfo.endCursor` | `string` | yes |
| `misconfigurations.pageInfo.hasNextPage` | `boolean` | no |
| `misconfigurations.pageInfo.hasPreviousPage` | `boolean` | no |
| `misconfigurations.pageInfo.startCursor` | `string` | yes |
| `misconfigurations.pageInfo.totalCount` | `integer` | yes |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    Cursor,
    MisconfigurationsInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_misconfigurations_lite(misconfigurations_args=MisconfigurationsInput(asset_id='asset_123', cursor=Cursor()))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
