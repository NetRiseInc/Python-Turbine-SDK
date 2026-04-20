<!-- Generated file: do not edit by hand -->

# query_assets_relay_lite

Retrieve assets with trimmed fields — keeps identity, status, risk score, and analytic rollups; drops filesystems, SHA-256, exploit trees, and credential counts.

## Parameters

| name | type | required |
| --- | --- | --- |
| `assets_relay_args` | `AssetsRelayInput` | `true` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `assetsRelay` | `object` | yes |
| `assetsRelay.edges[]` | `object` | yes |
| `assetsRelay.edges[].cursor` | `string` | yes |
| `assetsRelay.edges[].node` | `object` | yes |
| `assetsRelay.edges[].node.id` | `string` | yes |
| `assetsRelay.edges[].node.name` | `string` | yes |
| `assetsRelay.edges[].node.product` | `string` | yes |
| `assetsRelay.edges[].node.vendor` | `string` | yes |
| `assetsRelay.edges[].node.version` | `string` | yes |
| `assetsRelay.edges[].node.type` | `AssetType` | yes |
| `assetsRelay.edges[].node.status` | `ProcessingStatus` | yes |
| `assetsRelay.edges[].node.createdAt` | `string` | yes |
| `assetsRelay.edges[].node.updatedAt` | `string` | yes |
| `assetsRelay.edges[].node.risk` | `object` | yes |
| `assetsRelay.edges[].node.risk.category` | `RiskCategory` | yes |
| `assetsRelay.edges[].node.risk.score` | `float` | yes |
| `assetsRelay.edges[].node.analytic` | `object` | yes |
| `assetsRelay.edges[].node.analytic.vulnerability` | `object` | no |
| `assetsRelay.edges[].node.analytic.vulnerability.critical` | `integer` | no |
| `assetsRelay.edges[].node.analytic.vulnerability.high` | `integer` | no |
| `assetsRelay.edges[].node.analytic.vulnerability.medium` | `integer` | no |
| `assetsRelay.edges[].node.analytic.vulnerability.low` | `integer` | no |
| `assetsRelay.edges[].node.analytic.misconfigurations` | `object` | no |
| `assetsRelay.edges[].node.analytic.misconfigurations.failed` | `integer` | no |
| `assetsRelay.edges[].node.analytic.misconfigurations.notApplicable` | `integer` | no |
| `assetsRelay.edges[].node.analytic.misconfigurations.passed` | `integer` | no |
| `assetsRelay.edges[].node.analytic.components` | `object` | no |
| `assetsRelay.edges[].node.analytic.components.application` | `integer` | no |
| `assetsRelay.edges[].node.analytic.components.container` | `integer` | no |
| `assetsRelay.edges[].node.analytic.components.device` | `integer` | no |
| `assetsRelay.edges[].node.analytic.components.framework` | `integer` | no |
| `assetsRelay.edges[].node.analytic.components.kernel` | `integer` | no |
| `assetsRelay.edges[].node.analytic.components.kernelModule` | `integer` | no |
| `assetsRelay.edges[].node.analytic.components.library` | `integer` | no |
| `assetsRelay.edges[].node.analytic.components.os` | `integer` | no |
| `assetsRelay.edges[].node.analytic.components.package` | `integer` | no |
| `assetsRelay.pageInfo` | `object` | no |
| `assetsRelay.pageInfo.endCursor` | `string` | yes |
| `assetsRelay.pageInfo.hasNextPage` | `boolean` | no |
| `assetsRelay.pageInfo.hasPreviousPage` | `boolean` | no |
| `assetsRelay.pageInfo.startCursor` | `string` | yes |
| `assetsRelay.pageInfo.totalCount` | `integer` | yes |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    AssetsRelayInput,
    Cursor,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_assets_relay_lite(assets_relay_args=AssetsRelayInput(cursor=Cursor()))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
