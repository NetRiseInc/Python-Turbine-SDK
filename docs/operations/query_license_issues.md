<!-- Generated file: do not edit by hand -->

# query_license_issues

List license compliance issues identified across asset components.

## Parameters

| name | type | required |
| --- | --- | --- |
| `license_issues_args` | `LicenseIssuesInput` | `true` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `licenseIssues` | `object` | yes |
| `licenseIssues.edges[]` | `object` | no |
| `licenseIssues.edges[].cursor` | `string` | yes |
| `licenseIssues.edges[].node` | `object` | no |
| `licenseIssues.edges[].node.componentId` | `string` | yes |
| `licenseIssues.edges[].node.componentName` | `string` | yes |
| `licenseIssues.edges[].node.componentVersion` | `string` | yes |
| `licenseIssues.edges[].node.evidence` | `object` | yes |
| `licenseIssues.edges[].node.evidence.children` | `Any` | yes |
| `licenseIssues.edges[].node.evidence.componentId` | `string` | yes |
| `licenseIssues.edges[].node.evidence.licenseName` | `string` | yes |
| `licenseIssues.edges[].node.evidence.name` | `string` | yes |
| `licenseIssues.edges[].node.evidence.packageType` | `string` | yes |
| `licenseIssues.edges[].node.evidence.spdxId` | `string` | yes |
| `licenseIssues.edges[].node.evidence.vendor` | `string` | yes |
| `licenseIssues.edges[].node.evidence.version` | `string` | yes |
| `licenseIssues.edges[].node.issueDescription` | `string` | yes |
| `licenseIssues.edges[].node.issueId` | `string` | no |
| `licenseIssues.edges[].node.issueName` | `string` | no |
| `licenseIssues.edges[].node.lastModified` | `typing.Annotated[datetime.datetime, BeforeValidator(func=<function parse_datetime at 0x1090d31a0>, json_schema_input_type=PydanticUndefined)]` | yes |
| `licenseIssues.edges[].node.license` | `object` | yes |
| `licenseIssues.edges[].node.license.additionalCounts` | `object` | yes |
| `licenseIssues.edges[].node.license.additionalCounts.associatedComponents` | `integer` | yes |
| `licenseIssues.edges[].node.license.additionalCounts.issues` | `integer` | yes |
| `licenseIssues.edges[].node.license.additionalInfoUrlsList[]` | `string` | yes |
| `licenseIssues.edges[].node.license.licenseName` | `string` | yes |
| `licenseIssues.edges[].node.license.licenseNotes` | `string` | yes |
| `licenseIssues.edges[].node.license.licenseType` | `string` | yes |
| `licenseIssues.edges[].node.license.licenseUrl` | `string` | yes |
| `licenseIssues.edges[].node.license.spdxId` | `string` | yes |
| `licenseIssues.edges[].node.license.url` | `string` | yes |
| `licenseIssues.edges[].node.potentialSolution` | `string` | yes |
| `licenseIssues.edges[].node.remediation` | `object` | yes |
| `licenseIssues.edges[].node.remediation.createdTime` | `typing.Annotated[datetime.datetime, BeforeValidator(func=<function parse_datetime at 0x1090d31a0>, json_schema_input_type=PydanticUndefined)]` | yes |
| `licenseIssues.edges[].node.remediation.detail` | `string` | yes |
| `licenseIssues.edges[].node.remediation.user` | `string` | yes |
| `licenseIssues.edges[].node.severity` | `LicenseIssueSeverity` | yes |
| `licenseIssues.edges[].node.status` | `LicenseIssueStatus` | no |
| `licenseIssues.pageInfo` | `object` | no |
| `licenseIssues.pageInfo.endCursor` | `string` | yes |
| `licenseIssues.pageInfo.hasNextPage` | `boolean` | no |
| `licenseIssues.pageInfo.hasPreviousPage` | `boolean` | no |
| `licenseIssues.pageInfo.startCursor` | `string` | yes |
| `licenseIssues.pageInfo.totalCount` | `integer` | yes |

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
