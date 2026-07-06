<!-- Generated file: do not edit by hand -->

# query_misconfigurations

List failed security checks and configuration risks found in assets.

> **Prefer `sdk.iter_misconfigurations(...)`** — same data with automatic pagination, filter kwargs, and no cursor plumbing.

## Parameters

| name | type | required |
| --- | --- | --- |
| `misconfigurations_args` | `MisconfigurationsInput` | `true` |

## Filter fields

Build the `filter` argument with `where()` instead of hand-assembling `MisconfigurationsFilter.fields`:

```python
from netrise_turbine_sdk import where
from netrise_turbine_sdk_graphql.input_types import MisconfigurationsFilter

flt = where(MisconfigurationsFilter, status="...", name__contains="...")
```

| `where()` kwarg | GraphQL field | exact match uses |
| --- | --- | --- |
| `name` | `MisconfigurationsField.NAME` | `EQUAL` |
| `category` | `MisconfigurationsField.CATEGORY` | `EQUAL` |
| `status` | `MisconfigurationsField.STATUS` | `ENUM` |
| `severity` | `MisconfigurationsField.SEVERITY` | `ENUM` |

Lookups: `field=` (exact), `field__contains=`, `field__in=`, `field__gt=`, `field__gte=`, `field__lt=`, `field__lte=`.

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `misconfigurations` | `object` | yes |
| `misconfigurations.edges[]` | `object` | yes |
| `misconfigurations.edges[].cursor` | `string` | no |
| `misconfigurations.edges[].node` | `object` | yes |
| `misconfigurations.edges[].node.category` | `MisconfigurationCategoryType` | yes |
| `misconfigurations.edges[].node.checkDescription` | `string` | yes |
| `misconfigurations.edges[].node.checkId` | `string` | yes |
| `misconfigurations.edges[].node.checkRecommendation` | `string` | yes |
| `misconfigurations.edges[].node.context` | `Any` | yes |
| `misconfigurations.edges[].node.correlations[]` | `object` | yes |
| `misconfigurations.edges[].node.correlations[].artifact` | `string` | yes |
| `misconfigurations.edges[].node.correlations[].assetId` | `string` | yes |
| `misconfigurations.edges[].node.correlations[].assetName` | `string` | yes |
| `misconfigurations.edges[].node.correlations[].location` | `string` | yes |
| `misconfigurations.edges[].node.correlations[].risk` | `object` | yes |
| `misconfigurations.edges[].node.correlations[].risk.category` | `RiskCategory` | yes |
| `misconfigurations.edges[].node.correlations[].risk.rawScore` | `float` | yes |
| `misconfigurations.edges[].node.correlations[].risk.score` | `float` | yes |
| `misconfigurations.edges[].node.correlations[].updatedAt` | `string` | yes |
| `misconfigurations.edges[].node.correlationsCount` | `integer` | yes |
| `misconfigurations.edges[].node.displayName` | `string` | yes |
| `misconfigurations.edges[].node.result` | `MisconfigurationStatusType` | yes |
| `misconfigurations.edges[].node.severity` | `MisconfigurationSeverityType` | yes |
| `misconfigurations.pageInfo` | `object` | no |
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
        resp = client.query_misconfigurations(misconfigurations_args=MisconfigurationsInput(asset_id='asset_123', cursor=Cursor()))
        # Responses are typed Pydantic models: read fields as attributes.
        for edge in resp.misconfigurations.edges or []:
            node = edge.node
            print(node.severity, node.category, node.check_description)


if __name__ == "__main__":
    main()
```
