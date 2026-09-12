<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# query_license

[Back to the index](../README.md)

Get details for one software license.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |
| `license_args` | `LicenseInput` | `true` |

## Response fields

Typed attributes on the response model.

| Field | Type | Nullable |
| --- | --- | --- |
| `license` | `object` | yes |
| `license.additionalCounts` | `object` | yes |
| `license.additionalCounts.associatedComponents` | `integer` | yes |
| `license.additionalCounts.issues` | `integer` | yes |
| `license.additionalInfoUrlsList[]` | `string` | yes |
| `license.licenseName` | `string` | yes |
| `license.licenseNotes` | `string` | yes |
| `license.licenseType` | `string` | yes |
| `license.licenseUrl` | `string` | yes |
| `license.spdxId` | `string` | yes |
| `license.url` | `string` | yes |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    LicenseInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_license(license_args=LicenseInput(spdx_id='MIT', asset_id='asset_123'))
        # Responses are typed Pydantic models: read fields as attributes.
        print(resp.license.license_name, resp.license.license_notes)


if __name__ == "__main__":
    main()
```
