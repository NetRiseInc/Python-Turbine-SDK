<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# query_hashes

[Back to the index](../README.md)

List file hashes from an asset filesystem.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |
| `hashes_args` | `HashesInput` | `true` |

## Response fields

Typed attributes on the response model.

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

`sdk.iter_hashes(...)` paginates for you and accepts filter kwargs.

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig


def main() -> None:
    sdk = TurbineClient(TurbineClientConfig.from_env())

    for item in sdk.iter_hashes(asset_id="asset_123", page_size=10, max_pages=1):
        print(item)


if __name__ == "__main__":
    main()
```

## Raw client

Same data via `client.query_hashes` when you need exact GraphQL control.

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
