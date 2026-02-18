<!-- Generated file: do not edit by hand -->

# query_search

Execute keyword searches across all artifacts and files in organization.

## Parameters

| name | type | required |
| --- | --- | --- |
| `search_args` | `Union[SearchInput, None, UnsetType]` | `false` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `search` | `object` | yes |
| `search.findings` | `object` | no |
| `search.findings.edges[]` | `object` | no |
| `search.findings.edges[].node` | `object` | no |
| `search.findings.edges[].node.assetGroupIds[]` | `string` | yes |
| `search.findings.edges[].node.assetId` | `string` | no |
| `search.findings.edges[].node.assetName` | `string` | no |
| `search.findings.edges[].node.assetRevision` | `integer` | no |
| `search.findings.edges[].node.data` | `Any` | no |
| `search.findings.edges[].node.filePath` | `string` | no |
| `search.findings.edges[].node.parser` | `string` | no |
| `search.findings.edges[].node.sha1` | `string` | yes |
| `search.findings.edges[].node.sha256` | `string` | yes |
| `search.findings.edges[].node.updatedAt` | `string` | yes |
| `search.findings.pageInfo` | `object` | no |
| `search.findings.pageInfo.endCursor` | `string` | yes |
| `search.findings.pageInfo.hasNextPage` | `boolean` | no |
| `search.findings.pageInfo.hasPreviousPage` | `boolean` | no |
| `search.findings.pageInfo.startCursor` | `string` | yes |
| `search.findings.pageInfo.totalCount` | `integer` | yes |
| `search.query` | `string` | no |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    SearchInput,
)
from netrise_turbine_sdk_graphql.enums import (
    ArtifactName,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_search(search_args=SearchInput(query='search_term', artifacts=[ArtifactName.PUBLICKEY]))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
