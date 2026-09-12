<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# mutation_remediate_license_issues

[Back to the index](../README.md)

Set status and notes on license compliance issues.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |
| `remediate_license_issues_args` | `RemediateLicenseIssuesInput` | `true` |

## Response fields

Typed attributes on the response model.

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
        # Responses are typed Pydantic models: read fields as attributes.
        print(resp.remediate_license_issues.err)


if __name__ == "__main__":
    main()
```
