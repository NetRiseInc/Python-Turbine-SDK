<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# query_list_asset_crypto_libraries

[Back to the index](../README.md)

List crypto libraries detected in an asset.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |
| `list_asset_crypto_libraries_args` | `ListAssetCryptoLibrariesInput` | `true` |

## Response fields

Typed attributes on the response model.

| Field | Type | Nullable |
| --- | --- | --- |
| `listAssetCryptoLibraries` | `object` | yes |
| `listAssetCryptoLibraries.edges[]` | `object` | yes |
| `listAssetCryptoLibraries.edges[].cursor` | `string` | no |
| `listAssetCryptoLibraries.edges[].node` | `object` | yes |
| `listAssetCryptoLibraries.edges[].node.fips` | `string` | yes |
| `listAssetCryptoLibraries.edges[].node.name` | `string` | yes |
| `listAssetCryptoLibraries.edges[].node.pqcReady` | `boolean` | yes |
| `listAssetCryptoLibraries.edges[].node.purl` | `string` | yes |
| `listAssetCryptoLibraries.edges[].node.vendor` | `string` | yes |
| `listAssetCryptoLibraries.edges[].node.version` | `string` | yes |
| `listAssetCryptoLibraries.pageInfo` | `object` | no |
| `listAssetCryptoLibraries.pageInfo.endCursor` | `string` | yes |
| `listAssetCryptoLibraries.pageInfo.hasNextPage` | `boolean` | no |
| `listAssetCryptoLibraries.pageInfo.hasPreviousPage` | `boolean` | no |
| `listAssetCryptoLibraries.pageInfo.startCursor` | `string` | yes |
| `listAssetCryptoLibraries.pageInfo.totalCount` | `integer` | yes |

## Example

`sdk.iter_list_asset_crypto_libraries(...)` paginates for you and accepts filter kwargs.

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig


def main() -> None:
    sdk = TurbineClient(TurbineClientConfig.from_env())

    for item in sdk.iter_list_asset_crypto_libraries(asset_id="asset_123", page_size=10, max_pages=1):
        print(item)


if __name__ == "__main__":
    main()
```

## Raw client

Same data via `client.query_list_asset_crypto_libraries` when you need exact GraphQL control.

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    Cursor,
    ListAssetCryptoLibrariesInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_list_asset_crypto_libraries(list_asset_crypto_libraries_args=ListAssetCryptoLibrariesInput(asset_id='asset_123', cursor=Cursor()))
        # Responses are typed Pydantic models: read fields as attributes.
        for edge in resp.list_asset_crypto_libraries.edges or []:
            node = edge.node
            print(node.name, node.version, node.fips)


if __name__ == "__main__":
    main()
```
