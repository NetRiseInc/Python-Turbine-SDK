<!-- Generated file: do not edit by hand -->

# query_license

Retrieve detailed information for a specific software license.

## Parameters

| name | type | required |
| --- | --- | --- |
| `license_args` | `LicenseInput` | `true` |

## Response Schema

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
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
