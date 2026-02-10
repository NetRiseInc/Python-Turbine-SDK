<!-- Generated file: do not edit by hand -->

# query_license_issue

Get details about a specific license compliance issue.

## Parameters

| name | type | required |
| --- | --- | --- |
| `license_issue_args` | `LicenseIssueInput` | `true` |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    LicenseIssueInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_license_issue(license_issue_args=LicenseIssueInput(asset_id='asset_123', issue_id='id_123'))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
