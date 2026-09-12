# Filtering

## Convenience kwargs

The fastest path when the iterator exposes them:

```python
from netrise_turbine_sdk import Severity

for asset in sdk.iter_assets(name_contains="router", vendor="Acme"):
    print(asset.id, asset.name)

for vuln in sdk.iter_vulnerabilities_lite(
    asset_id="abc123",
    severity=Severity.CRITICAL,
    cve_contains="2024",
):
    print(vuln.cve, vuln.severity)
```

## `where()`

A reusable typed filter. Lookups: `field=` (exact), `field__contains=`, `field__in=`, `field__gt=` / `__gte=` / `__lt=` / `__le=`. Each [operation page](../README.md) lists its supported fields under "Filter fields".

```python
from netrise_turbine_sdk import inputs, where

recent_cves = where(
    inputs.VulnerabilityFilter,
    cve__contains="2024",
)

for vuln in sdk.iter_vulnerabilities_lite(asset_id="abc123", filter=recent_cves):
    print(vuln.cve)
```

## Plain dicts

Shaped like the generated input model; Pydantic coerces before the request:

```python
for asset in sdk.iter_assets(filter={"hideFailed": True}):
    print(asset.name)
```

## Combine `filter=` with kwargs

They merge, so a base filter can be narrowed per call:

```python
for vuln in sdk.iter_vulnerabilities_lite(
    asset_id="abc123",
    filter=recent_cves,
    severity=Severity.CRITICAL,
):
    print(vuln.cve)
```

## Sorting

Pass the generated sort model:

```python
from netrise_turbine_sdk import SortOrder, enums, inputs

sort = inputs.AssetsSort(field=enums.AssetsSortField.CREATEDAT, order=SortOrder.DESC)
for asset in sdk.iter_assets(sort=sort, max_items=10):
    print(asset.name, asset.created_at)
```

## Notes

- `severity=` / `severity_in=` on vulnerability and misconfiguration iterators filter client-side (the server does not accept severity in `fields`), so pages are fetched then matched. Prefer server-side fields when volume matters.
- Common enums are importable from `netrise_turbine_sdk`: `Severity` (`LOW`–`CRITICAL`), `SortOrder`, `VexStatus`. Asset risk categories use a different scale (`NEGLIGIBLE`–`SEVERE`) in `enums.RiskCategoryFilter`.
