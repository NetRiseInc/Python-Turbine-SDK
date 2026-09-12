<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# query_binary_protections

[Back to the index](../README.md)

List binary hardening details for an asset.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |
| `binary_protections_args` | `BinaryProtectionsInput` | `true` |

## Response fields

Typed attributes on the response model.

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
| `binaryProtections.pageInfo` | `object` | no |
| `binaryProtections.pageInfo.endCursor` | `string` | yes |
| `binaryProtections.pageInfo.hasNextPage` | `boolean` | no |
| `binaryProtections.pageInfo.hasPreviousPage` | `boolean` | no |
| `binaryProtections.pageInfo.startCursor` | `string` | yes |
| `binaryProtections.pageInfo.totalCount` | `integer` | yes |

## Example

`sdk.iter_binary_protections(...)` paginates for you and accepts filter kwargs.

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig


def main() -> None:
    sdk = TurbineClient(TurbineClientConfig.from_env())

    for item in sdk.iter_binary_protections(asset_id="asset_123", page_size=10, max_pages=1):
        print(item)


if __name__ == "__main__":
    main()
```

## Raw client

Same data via `client.query_binary_protections` when you need exact GraphQL control.

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
        # Responses are typed Pydantic models: read fields as attributes.
        for edge in resp.binary_protections.edges or []:
            node = edge.node
            print(node.name, node.bind_now, node.correlations_count)


if __name__ == "__main__":
    main()
```
