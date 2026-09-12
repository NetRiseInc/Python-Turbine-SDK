<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# query_secrets

[Back to the index](../README.md)

List secrets discovered in an asset.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |
| `secrets_args` | `SecretsInput` | `true` |

## Response fields

Typed attributes on the response model.

| Field | Type | Nullable |
| --- | --- | --- |
| `secrets` | `object` | yes |
| `secrets.edges[]` | `object` | yes |
| `secrets.edges[].cursor` | `string` | yes |
| `secrets.edges[].node` | `object` | yes |
| `secrets.edges[].node.id` | `string` | no |
| `secrets.edges[].node.category` | `SecretCategory` | no |
| `secrets.edges[].node.categoryLabel` | `string` | yes |
| `secrets.edges[].node.correlations[]` | `object` | yes |
| `secrets.edges[].node.correlations[].artifact` | `string` | yes |
| `secrets.edges[].node.correlations[].assetId` | `string` | yes |
| `secrets.edges[].node.correlations[].assetName` | `string` | yes |
| `secrets.edges[].node.correlations[].location` | `string` | yes |
| `secrets.edges[].node.correlations[].risk` | `object` | yes |
| `secrets.edges[].node.correlations[].risk.category` | `RiskCategory` | yes |
| `secrets.edges[].node.correlations[].risk.rawScore` | `float` | yes |
| `secrets.edges[].node.correlations[].risk.score` | `float` | yes |
| `secrets.edges[].node.correlations[].updatedAt` | `string` | yes |
| `secrets.edges[].node.correlationsCount` | `integer` | no |
| `secrets.edges[].node.currentRemediation` | `object` | yes |
| `secrets.edges[].node.currentRemediation.author` | `string` | yes |
| `secrets.edges[].node.currentRemediation.createdAt` | `string` | yes |
| `secrets.edges[].node.currentRemediation.description` | `string` | yes |
| `secrets.edges[].node.currentRemediation.secretId` | `string` | yes |
| `secrets.edges[].node.currentRemediation.status` | `SecretRemediationStatus` | yes |
| `secrets.edges[].node.description` | `string` | yes |
| `secrets.edges[].node.filePath` | `string` | yes |
| `secrets.edges[].node.isReachable` | `boolean` | yes |
| `secrets.edges[].node.rawSecret` | `string` | yes |
| `secrets.edges[].node.remediationStatus` | `SecretRemediationStatus` | yes |
| `secrets.edges[].node.sanitizedSecret` | `string` | yes |
| `secrets.edges[].node.severity` | `SecretSeverity` | no |
| `secrets.edges[].node.subtype` | `string` | yes |
| `secrets.edges[].node.type` | `SecretType` | yes |
| `secrets.pageInfo` | `object` | no |
| `secrets.pageInfo.endCursor` | `string` | yes |
| `secrets.pageInfo.hasNextPage` | `boolean` | no |
| `secrets.pageInfo.hasPreviousPage` | `boolean` | no |
| `secrets.pageInfo.startCursor` | `string` | yes |
| `secrets.pageInfo.totalCount` | `integer` | yes |

## Example

`sdk.iter_secrets(...)` paginates for you and accepts filter kwargs.

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig


def main() -> None:
    sdk = TurbineClient(TurbineClientConfig.from_env())

    for item in sdk.iter_secrets(asset_id="asset_123", page_size=10, max_pages=1):
        print(item)


if __name__ == "__main__":
    main()
```

## Raw client

Same data via `client.query_secrets` when you need exact GraphQL control.

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    Cursor,
    SecretsInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_secrets(secrets_args=SecretsInput(asset_id='asset_123', cursor=Cursor()))
        # Responses are typed Pydantic models: read fields as attributes.
        for edge in resp.secrets.edges or []:
            node = edge.node
            print(node.id, node.severity, node.category)


if __name__ == "__main__":
    main()
```
