<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# query_assets_relay_summary

[Back to the index](../README.md)

List assets as id, name, and analytic counts only.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |
| `assets_relay_args` | `AssetsRelayInput` | `true` |

## Filter fields

Use `where()` to build `AssetsFilter` — see [Filtering](../guides/filtering.md).

```python
from netrise_turbine_sdk import where
from netrise_turbine_sdk_graphql.input_types import AssetsFilter

flt = where(AssetsFilter, status="...", name__contains="...")
```

| `where()` kwarg | GraphQL field | exact match uses |
| --- | --- | --- |
| `id` | `AssetsFilterField.ID` | `EQUAL` |
| `name` | `AssetsFilterField.NAME` | `EQUAL` |
| `vendor` | `AssetsFilterField.VENDOR` | `EQUAL` |
| `product` | `AssetsFilterField.PRODUCT` | `EQUAL` |
| `version` | `AssetsFilterField.VERSION` | `EQUAL` |
| `type` | `AssetsFilterField.TYPE` | `EQUAL` |
| `sha256` | `AssetsFilterField.SHA256` | `EQUAL` |
| `status` | `AssetsFilterField.PROCESSINGSTATUS` | `ENUM` |
| `risk_category` | `AssetsFilterField.RISKCATEGORY` | `ENUM` |
| `risk_score` | `AssetsFilterField.RISKSCORE` | `EQUAL` |
| `uploaded_by` | `AssetsFilterField.UPLOADEDBY` | `EQUAL` |

Lookups: `field=` (exact), `field__contains=`, `field__in=`, `field__gt=`, `field__gte=`, `field__lt=`, `field__lte=`.

## Response fields

Typed attributes on the response model.

| Field | Type | Nullable |
| --- | --- | --- |
| `assetsRelay` | `object` | yes |
| `assetsRelay.edges[]` | `object` | yes |
| `assetsRelay.edges[].cursor` | `string` | yes |
| `assetsRelay.edges[].node` | `object` | yes |
| `assetsRelay.edges[].node.id` | `string` | yes |
| `assetsRelay.edges[].node.name` | `string` | yes |
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

`sdk.iter_assets_relay_summary(...)` paginates for you and accepts filter kwargs.

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig


def main() -> None:
    sdk = TurbineClient(TurbineClientConfig.from_env())

    for item in sdk.iter_assets_relay_summary(page_size=10, max_pages=1):
        print(item.id, item.name)


if __name__ == "__main__":
    main()
```

## Raw client

Same data via `client.query_assets_relay_summary` when you need exact GraphQL control.

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
        resp = client.query_assets_relay_summary(assets_relay_args=AssetsRelayInput(cursor=Cursor()))
        # Responses are typed Pydantic models: read fields as attributes.
        for edge in resp.assets_relay.edges or []:
            node = edge.node
            print(node.id, node.name)


if __name__ == "__main__":
    main()
```
