<!-- Generated file: do not edit by hand -->

# query_license_issues

List license compliance issues identified across asset components.

## Parameters

| name | type | required |
| --- | --- | --- |
| `license_issues_args` | `LicenseIssuesInput` | `true` |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    LicenseIssuesInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_license_issues(license_issues_args=LicenseIssuesInput(asset_id='asset_123'))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
