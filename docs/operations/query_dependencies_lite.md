<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# query_dependencies_lite

[Back to the index](../README.md)

List components with identity, version, license, and rollups.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |
| `dependencies_args` | `DependencyInput` | `true` |

## Filter fields

Use `where()` to build `DependencyFilter` — see [Filtering](../guides/filtering.md).

```python
from netrise_turbine_sdk import where
from netrise_turbine_sdk_graphql.input_types import DependencyFilter

flt = where(DependencyFilter, type="...", name__contains="...")
```

| `where()` kwarg | GraphQL field | exact match uses |
| --- | --- | --- |
| `name` | `DependencyField.NAME` | `EQUAL` |
| `vendor` | `DependencyField.VENDOR` | `EQUAL` |
| `type` | `DependencyField.TYPE` | `ENUM` |
| `subtype` | `DependencyField.SUBTYPE` | `ENUM` |
| `license` | `DependencyField.LICENSE` | `EQUAL` |
| `version` | `DependencyField.VERSION` | `EQUAL` |
| `verification` | `DependencyField.VERIFICATION` | `ENUM` |
| `scope` | `DependencyField.SCOPE` | `ENUM` |
| `confidence` | `DependencyField.CONFIDENCE` | `EQUAL` |

Lookups: `field=` (exact), `field__contains=`, `field__in=`, `field__gt=`, `field__gte=`, `field__lt=`, `field__lte=`.

## Response fields

Typed attributes on the response model.

| Field | Type | Nullable |
| --- | --- | --- |
| `dependencies` | `object` | yes |
| `dependencies.edges[]` | `object` | yes |
| `dependencies.edges[].cursor` | `string` | yes |
| `dependencies.edges[].node` | `object` | yes |
| `dependencies.edges[].node.id` | `string` | no |
| `dependencies.edges[].node.submitDatetime` | `typing.Annotated[datetime.datetime, BeforeValidator(func=<function parse_datetime at 0x1090c2660>, json_schema_input_type=PydanticUndefined)]` | yes |
| `dependencies.edges[].node.identifiedVia[]` | `IdentifiedViaCategory` | yes |
| `dependencies.edges[].node.correlationsCount` | `integer` | yes |
| `dependencies.edges[].node.dependency` | `object` | no |
| `dependencies.edges[].node.dependency.id` | `string` | no |
| `dependencies.edges[].node.dependency.name` | `string` | no |
| `dependencies.edges[].node.dependency.vendor` | `string` | yes |
| `dependencies.edges[].node.dependency.product` | `string` | yes |
| `dependencies.edges[].node.dependency.license[]` | `string` | yes |
| `dependencies.edges[].node.dependency.purls[]` | `string` | yes |
| `dependencies.edges[].node.dependency.type` | `ComponentType` | no |
| `dependencies.edges[].node.dependency.subtype` | `ComponentSubType` | yes |
| `dependencies.edges[].node.dependency.path` | `string` | yes |
| `dependencies.edges[].node.dependency.version` | `object` | yes |
| `dependencies.edges[].node.dependency.version.id` | `string` | yes |
| `dependencies.edges[].node.dependency.version.isConcrete` | `boolean` | no |
| `dependencies.edges[].node.analytic` | `object` | no |
| `dependencies.edges[].node.analytic.vulnerability` | `object` | no |
| `dependencies.edges[].node.analytic.vulnerability.critical` | `integer` | no |
| `dependencies.edges[].node.analytic.vulnerability.high` | `integer` | no |
| `dependencies.edges[].node.analytic.vulnerability.medium` | `integer` | no |
| `dependencies.edges[].node.analytic.vulnerability.low` | `integer` | no |
| `dependencies.edges[].node.analytic.misconfigurations` | `object` | no |
| `dependencies.edges[].node.analytic.misconfigurations.failed` | `integer` | no |
| `dependencies.edges[].node.analytic.misconfigurations.notApplicable` | `integer` | no |
| `dependencies.edges[].node.analytic.misconfigurations.passed` | `integer` | no |
| `dependencies.edges[].node.analytic.components` | `object` | no |
| `dependencies.edges[].node.analytic.components.application` | `integer` | no |
| `dependencies.edges[].node.analytic.components.container` | `integer` | no |
| `dependencies.edges[].node.analytic.components.device` | `integer` | no |
| `dependencies.edges[].node.analytic.components.framework` | `integer` | no |
| `dependencies.edges[].node.analytic.components.kernel` | `integer` | no |
| `dependencies.edges[].node.analytic.components.kernelModule` | `integer` | no |
| `dependencies.edges[].node.analytic.components.library` | `integer` | no |
| `dependencies.edges[].node.analytic.components.os` | `integer` | no |
| `dependencies.edges[].node.analytic.components.package` | `integer` | no |
| `dependencies.pageInfo` | `object` | no |
| `dependencies.pageInfo.endCursor` | `string` | yes |
| `dependencies.pageInfo.hasNextPage` | `boolean` | no |
| `dependencies.pageInfo.hasPreviousPage` | `boolean` | no |
| `dependencies.pageInfo.startCursor` | `string` | yes |
| `dependencies.pageInfo.totalCount` | `integer` | yes |

## Example

`sdk.iter_dependencies_lite(...)` paginates for you and accepts filter kwargs.

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig


def main() -> None:
    sdk = TurbineClient(TurbineClientConfig.from_env())

    for item in sdk.iter_dependencies_lite(asset_id="asset_123", page_size=10, max_pages=1):
        print(item)


if __name__ == "__main__":
    main()
```

## Raw client

Same data via `client.query_dependencies_lite` when you need exact GraphQL control.

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    DependencyInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_dependencies_lite(dependencies_args=DependencyInput(composed_asset_id='composed_asset_123'))
        # Responses are typed Pydantic models: read fields as attributes.
        for edge in resp.dependencies.edges or []:
            node = edge.node
            print(node.id, node.submit_datetime, node.correlations_count)


if __name__ == "__main__":
    main()
```
