<!-- Generated file: do not edit by hand -->

# query_identified_components_preview

Return organization-wide component counts filtered by enabled identification methods, with before/after deltas when verification settings change.

## Parameters

| name | type | required |
| --- | --- | --- |
| `identified_components_preview_args` | `IdentifiedComponentsPreviewInput` | `true` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `identifiedComponentsPreview` | `object` | yes |
| `identifiedComponentsPreview.application` | `object` | no |
| `identifiedComponentsPreview.application.afterCount` | `integer` | yes |
| `identifiedComponentsPreview.application.beforeCount` | `integer` | yes |
| `identifiedComponentsPreview.container` | `object` | no |
| `identifiedComponentsPreview.container.afterCount` | `integer` | yes |
| `identifiedComponentsPreview.container.beforeCount` | `integer` | yes |
| `identifiedComponentsPreview.device` | `object` | no |
| `identifiedComponentsPreview.device.afterCount` | `integer` | yes |
| `identifiedComponentsPreview.device.beforeCount` | `integer` | yes |
| `identifiedComponentsPreview.framework` | `object` | no |
| `identifiedComponentsPreview.framework.afterCount` | `integer` | yes |
| `identifiedComponentsPreview.framework.beforeCount` | `integer` | yes |
| `identifiedComponentsPreview.kernel` | `object` | no |
| `identifiedComponentsPreview.kernel.afterCount` | `integer` | yes |
| `identifiedComponentsPreview.kernel.beforeCount` | `integer` | yes |
| `identifiedComponentsPreview.kernelModule` | `object` | no |
| `identifiedComponentsPreview.kernelModule.afterCount` | `integer` | yes |
| `identifiedComponentsPreview.kernelModule.beforeCount` | `integer` | yes |
| `identifiedComponentsPreview.library` | `object` | no |
| `identifiedComponentsPreview.library.afterCount` | `integer` | yes |
| `identifiedComponentsPreview.library.beforeCount` | `integer` | yes |
| `identifiedComponentsPreview.os` | `object` | no |
| `identifiedComponentsPreview.os.afterCount` | `integer` | yes |
| `identifiedComponentsPreview.os.beforeCount` | `integer` | yes |
| `identifiedComponentsPreview.package` | `object` | no |
| `identifiedComponentsPreview.package.afterCount` | `integer` | yes |
| `identifiedComponentsPreview.package.beforeCount` | `integer` | yes |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    IdentifiedComponentsPreviewInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_identified_components_preview(identified_components_preview_args=IdentifiedComponentsPreviewInput())
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
