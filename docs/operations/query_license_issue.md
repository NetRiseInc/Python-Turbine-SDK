<!-- Generated file: do not edit by hand -->

# query_license_issue

Get details about a specific license compliance issue.

## Parameters

| name | type | required |
| --- | --- | --- |
| `license_issue_args` | `LicenseIssueInput` | `true` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `licenseIssue` | `object` | yes |
| `licenseIssue.componentId` | `string` | yes |
| `licenseIssue.componentName` | `string` | yes |
| `licenseIssue.componentVersion` | `string` | yes |
| `licenseIssue.evidence` | `object` | yes |
| `licenseIssue.evidence.children` | `Any` | yes |
| `licenseIssue.evidence.componentId` | `string` | yes |
| `licenseIssue.evidence.licenseName` | `string` | yes |
| `licenseIssue.evidence.name` | `string` | yes |
| `licenseIssue.evidence.packageType` | `string` | yes |
| `licenseIssue.evidence.spdxId` | `string` | yes |
| `licenseIssue.evidence.vendor` | `string` | yes |
| `licenseIssue.evidence.version` | `string` | yes |
| `licenseIssue.issueDescription` | `string` | yes |
| `licenseIssue.issueId` | `string` | no |
| `licenseIssue.issueName` | `string` | no |
| `licenseIssue.lastModified` | `typing.Annotated[datetime.datetime, BeforeValidator(func=<function parse_datetime at 0x1090d31a0>, json_schema_input_type=PydanticUndefined)]` | yes |
| `licenseIssue.license` | `object` | yes |
| `licenseIssue.license.additionalCounts` | `object` | yes |
| `licenseIssue.license.additionalCounts.associatedComponents` | `integer` | yes |
| `licenseIssue.license.additionalCounts.issues` | `integer` | yes |
| `licenseIssue.license.additionalInfoUrlsList[]` | `string` | yes |
| `licenseIssue.license.licenseName` | `string` | yes |
| `licenseIssue.license.licenseNotes` | `string` | yes |
| `licenseIssue.license.licenseType` | `string` | yes |
| `licenseIssue.license.licenseUrl` | `string` | yes |
| `licenseIssue.license.spdxId` | `string` | yes |
| `licenseIssue.license.url` | `string` | yes |
| `licenseIssue.potentialSolution` | `string` | yes |
| `licenseIssue.remediation` | `object` | yes |
| `licenseIssue.remediation.createdTime` | `typing.Annotated[datetime.datetime, BeforeValidator(func=<function parse_datetime at 0x1090d31a0>, json_schema_input_type=PydanticUndefined)]` | yes |
| `licenseIssue.remediation.detail` | `string` | yes |
| `licenseIssue.remediation.user` | `string` | yes |
| `licenseIssue.severity` | `LicenseIssueSeverity` | yes |
| `licenseIssue.status` | `LicenseIssueStatus` | no |

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
        resp = client.query_license_issue(license_issue_args=LicenseIssueInput(asset_id='asset_123', issue_id='issue_123'))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
