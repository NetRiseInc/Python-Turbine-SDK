<!-- Generated file: do not edit by hand -->

# mutation_remediate_license_issues

Update status and add notes to resolve identified license issues.

## Parameters

| name | type | required |
| --- | --- | --- |
| `remediate_license_issues_args` | `RemediateLicenseIssuesInput` | `true` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `remediateLicenseIssues` | `object` | yes |
| `remediateLicenseIssues.err` | `string` | yes |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    RemediateLicenseIssuesInput,
)
from netrise_turbine_sdk_graphql.enums import (
    LicenseIssueStatus,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.mutation_remediate_license_issues(remediate_license_issues_args=RemediateLicenseIssuesInput(asset_id='asset_123', issue_ids=['value'], status=LicenseIssueStatus.RESOLVED))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
