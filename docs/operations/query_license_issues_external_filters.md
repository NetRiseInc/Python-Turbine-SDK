<!-- Generated file: do not edit by hand -->

# query_license_issues_external_filters

Retrieve available filter options for license issue queries.

## Parameters

| name | type | required |
| --- | --- | --- |
| `license_issues_external_filters_args` | `LicenseIssuesExternalFiltersInput` | `true` |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    LicenseIssuesExternalFiltersInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_license_issues_external_filters(license_issues_external_filters_args=LicenseIssuesExternalFiltersInput(asset_id='asset_123'))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
