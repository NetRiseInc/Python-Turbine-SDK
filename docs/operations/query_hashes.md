<!-- Generated file: do not edit by hand -->

# query_hashes

List cryptographic hashes for files identified within the asset filesystem.

> **Prefer `sdk.iter_hashes(...)`** — same data with automatic pagination, filter kwargs, and no cursor plumbing.

## Parameters

| name | type | required |
| --- | --- | --- |
| `hashes_args` | `HashesInput` | `true` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `hashes` | `object` | yes |
| `hashes.edges[]` | `object` | yes |
| `hashes.edges[].cursor` | `string` | yes |
| `hashes.edges[].node` | `object` | yes |
| `hashes.edges[].node.correlations[]` | `object` | yes |
| `hashes.edges[].node.correlations[].artifact` | `string` | yes |
| `hashes.edges[].node.correlations[].assetId` | `string` | yes |
| `hashes.edges[].node.correlations[].assetName` | `string` | yes |
| `hashes.edges[].node.correlations[].location` | `string` | yes |
| `hashes.edges[].node.correlations[].risk` | `object` | yes |
| `hashes.edges[].node.correlations[].risk.category` | `RiskCategory` | yes |
| `hashes.edges[].node.correlations[].risk.rawScore` | `float` | yes |
| `hashes.edges[].node.correlations[].risk.score` | `float` | yes |
| `hashes.edges[].node.correlations[].updatedAt` | `string` | yes |
| `hashes.edges[].node.correlationsCount` | `integer` | yes |
| `hashes.edges[].node.cracked` | `boolean` | yes |
| `hashes.edges[].node.filePath` | `string` | yes |
| `hashes.edges[].node.hash` | `string` | yes |
| `hashes.edges[].node.hashType` | `string` | yes |
| `hashes.edges[].node.hashcatNumber` | `integer` | yes |
| `hashes.edges[].node.numRounds` | `integer` | yes |
| `hashes.edges[].node.type` | `string` | yes |
| `hashes.pageInfo` | `object` | no |
| `hashes.pageInfo.endCursor` | `string` | yes |
| `hashes.pageInfo.hasNextPage` | `boolean` | no |
| `hashes.pageInfo.hasPreviousPage` | `boolean` | no |
| `hashes.pageInfo.startCursor` | `string` | yes |
| `hashes.pageInfo.totalCount` | `integer` | yes |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    Cursor,
    HashesInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_hashes(hashes_args=HashesInput(asset_id='asset_123', cursor=Cursor()))
        # Responses are typed Pydantic models: read fields as attributes.
        for edge in resp.hashes.edges or []:
            node = edge.node
            print(node.correlations_count, node.cracked, node.file_path)


if __name__ == "__main__":
    main()
```
