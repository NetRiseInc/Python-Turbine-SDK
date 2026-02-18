<!-- Generated file: do not edit by hand -->

# query_credentials

Identify user accounts and password hashes discovered within the filesystem.

## Parameters

| name | type | required |
| --- | --- | --- |
| `credentials_args` | `CredentialsInput` | `true` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `credentials` | `object` | yes |
| `credentials.edges[]` | `object` | yes |
| `credentials.edges[].cursor` | `string` | yes |
| `credentials.edges[].node` | `object` | yes |
| `credentials.edges[].node.correlations[]` | `object` | yes |
| `credentials.edges[].node.correlations[].artifact` | `string` | yes |
| `credentials.edges[].node.correlations[].assetId` | `string` | yes |
| `credentials.edges[].node.correlations[].assetName` | `string` | yes |
| `credentials.edges[].node.correlations[].location` | `string` | yes |
| `credentials.edges[].node.correlations[].risk` | `object` | yes |
| `credentials.edges[].node.correlations[].risk.category` | `RiskCategory` | yes |
| `credentials.edges[].node.correlations[].risk.rawScore` | `float` | yes |
| `credentials.edges[].node.correlations[].risk.score` | `float` | yes |
| `credentials.edges[].node.correlations[].updatedAt` | `string` | yes |
| `credentials.edges[].node.correlationsCount` | `integer` | yes |
| `credentials.edges[].node.cracked` | `boolean` | yes |
| `credentials.edges[].node.filePath` | `string` | yes |
| `credentials.edges[].node.hashType` | `string` | yes |
| `credentials.edges[].node.homeDir` | `string` | yes |
| `credentials.edges[].node.passwordHash` | `string` | yes |
| `credentials.edges[].node.shell` | `string` | yes |
| `credentials.edges[].node.userInfo` | `string` | yes |
| `credentials.edges[].node.userName` | `string` | yes |
| `credentials.pageInfo` | `object` | no |
| `credentials.pageInfo.endCursor` | `string` | yes |
| `credentials.pageInfo.hasNextPage` | `boolean` | no |
| `credentials.pageInfo.hasPreviousPage` | `boolean` | no |
| `credentials.pageInfo.startCursor` | `string` | yes |
| `credentials.pageInfo.totalCount` | `integer` | yes |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    CredentialsInput,
    Cursor,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_credentials(credentials_args=CredentialsInput(asset_id='asset_123', cursor=Cursor()))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
