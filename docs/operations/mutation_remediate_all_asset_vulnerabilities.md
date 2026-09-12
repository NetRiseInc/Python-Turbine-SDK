<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# mutation_remediate_all_asset_vulnerabilities

[Back to the index](../README.md)

Apply a VEX status to every vuln matching a filter.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |
| `remediate_all_asset_vulnerabilities_args` | `CreateAllAssetVulnerabilitiesRemediationInput` | `true` |

## Filter fields

Use `where()` to build `VulnerabilityFilter` — see [Filtering](../guides/filtering.md).

```python
from netrise_turbine_sdk import where
from netrise_turbine_sdk_graphql.input_types import VulnerabilityFilter

flt = where(VulnerabilityFilter, severity="...", name__contains="...")
```

| `where()` kwarg | GraphQL field | exact match uses |
| --- | --- | --- |
| `cve` | `VulnerabilityField.CVE` | `EQUAL` |
| `severity` | `VulnerabilityField.SEVERITY` | `ENUM` |
| `name` | `VulnerabilityField.NAME` | `EQUAL` |
| `version` | `VulnerabilityField.VERSION` | `EQUAL` |
| `vendor` | `VulnerabilityField.VENDOR` | `EQUAL` |
| `maturity` | `VulnerabilityField.MATURITY` | `ENUM` |
| `filepath` | `VulnerabilityField.FILEPATH` | `EQUAL` |
| `attack_vector` | `VulnerabilityField.ATTACKVECTOR` | `ENUM` |
| `attack_complexity` | `VulnerabilityField.ATTACKCOMPLEXITY` | `ENUM` |
| `remediation_status` | `VulnerabilityField.VULNERABILITYREMEDIATIONSTATUS` | `ENUM` |
| `epss_score` | `VulnerabilityField.EPSSSCORE` | `EQUAL` |
| `epss_percentile` | `VulnerabilityField.EPSSPERCENTILE` | `EQUAL` |

Lookups: `field=` (exact), `field__contains=`, `field__in=`, `field__gt=`, `field__gte=`, `field__lt=`, `field__lte=`.

## Response fields

Typed attributes on the response model.

| Field | Type | Nullable |
| --- | --- | --- |
| `remediateAllAssetVulnerabilities` | `object` | no |
| `remediateAllAssetVulnerabilities.err` | `string` | yes |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    CreateAllAssetVulnerabilitiesRemediationInput,
    VulnerabilityFilter,
)
from netrise_turbine_sdk_graphql.enums import (
    VexStatus,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.mutation_remediate_all_asset_vulnerabilities(remediate_all_asset_vulnerabilities_args=CreateAllAssetVulnerabilitiesRemediationInput(asset_id='asset_123', vulnerability_filter=VulnerabilityFilter(), status=VexStatus.UNSPECIFIED))
        # Responses are typed Pydantic models: read fields as attributes.
        print(resp.remediate_all_asset_vulnerabilities.err)


if __name__ == "__main__":
    main()
```
