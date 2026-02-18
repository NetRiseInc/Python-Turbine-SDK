<!-- Generated file: do not edit by hand -->

# query_binary_protections

List security hardening details for binaries found within the asset.

## Parameters

| name | type | required |
| --- | --- | --- |
| `binary_protections_args` | `BinaryProtectionsInput` | `true` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `binaryProtections` | `object` | yes |
| `binaryProtections.edges[]` | `object` | yes |
| `binaryProtections.edges[].cursor` | `string` | no |
| `binaryProtections.edges[].node` | `object` | yes |
| `binaryProtections.edges[].node.bindNow` | `BindNowType` | yes |
| `binaryProtections.edges[].node.correlations[]` | `object` | yes |
| `binaryProtections.edges[].node.correlations[].artifact` | `string` | yes |
| `binaryProtections.edges[].node.correlations[].assetId` | `string` | yes |
| `binaryProtections.edges[].node.correlations[].assetName` | `string` | yes |
| `binaryProtections.edges[].node.correlations[].location` | `string` | yes |
| `binaryProtections.edges[].node.correlations[].risk` | `object` | yes |
| `binaryProtections.edges[].node.correlations[].risk.category` | `RiskCategory` | yes |
| `binaryProtections.edges[].node.correlations[].risk.rawScore` | `float` | yes |
| `binaryProtections.edges[].node.correlations[].risk.score` | `float` | yes |
| `binaryProtections.edges[].node.correlations[].updatedAt` | `string` | yes |
| `binaryProtections.edges[].node.correlationsCount` | `integer` | yes |
| `binaryProtections.edges[].node.filePath` | `string` | yes |
| `binaryProtections.edges[].node.fortifySource` | `FortifySrcType` | yes |
| `binaryProtections.edges[].node.name` | `string` | yes |
| `binaryProtections.edges[].node.nx` | `NxType` | yes |
| `binaryProtections.edges[].node.pie` | `PieType` | yes |
| `binaryProtections.edges[].node.relro` | `RelroType` | yes |
| `binaryProtections.edges[].node.sha256` | `string` | yes |
| `binaryProtections.edges[].node.stackCanary` | `boolean` | yes |
| `binaryProtections.edges[].node.vfsId` | `string` | yes |
| `binaryProtections.pageInfo` | `object` | yes |
| `binaryProtections.pageInfo.endCursor` | `string` | yes |
| `binaryProtections.pageInfo.hasNextPage` | `boolean` | no |
| `binaryProtections.pageInfo.hasPreviousPage` | `boolean` | no |
| `binaryProtections.pageInfo.startCursor` | `string` | yes |
| `binaryProtections.pageInfo.totalCount` | `integer` | yes |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    BinaryProtectionsInput,
    Cursor,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_binary_protections(binary_protections_args=BinaryProtectionsInput(asset_id='asset_123', cursor=Cursor()))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
