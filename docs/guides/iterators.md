# Iterators

Lite iterators are the usual way to use the SDK: typed responses with the fields most workflows need, and cursor pagination handled for you.

```python
for vuln in sdk.iter_vulnerabilities_lite(asset_id="abc123"):
    print(vuln.cve, vuln.severity, vuln.cvss_score)
```

For asset lists, use `iter_assets()` (alias of `iter_assets_relay_lite()`). `iter_assets_full()` adds the full nested payload; `iter_assets_summary()` is the smallest count-only sweep.

## Common kwargs

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `page_size` | `int` | `100` | Items per server round-trip |
| `max_pages` | `int \| None` | `None` | Hard cap on pages fetched. `None` = fetch all |
| `max_items` | `int \| None` | `None` | Hard cap on items yielded |
| `start_after` | `str \| None` | `None` | Resume after a previously returned cursor |

Results are `Paginator` objects — loop over them, or inspect pagination metadata:

```python
page = sdk.iter_assets(page_size=100, max_items=250)
assets = page.to_list()

print(page.total_count)     # Server-reported total, once a page has been fetched
print(page.pages_fetched)   # Round-trips made
print(page.last_cursor)     # Save this for start_after=...

next_page = sdk.iter_assets(start_after=page.last_cursor, max_items=250)
```

`max_items` caps returned objects; `max_pages` caps server round-trips; `first()` fetches a single item.

## Lite iterators

| Method | Scope | Key parameters | Fields included |
| --- | --- | --- | --- |
| `iter_assets` (`iter_assets_relay_lite`) | Org-wide | `filter`, `sort`, `name_contains`, `vendor` | id, name, vendor, product, version, type, status, timestamps, risk score, analytic rollups |
| `iter_assets_summary` (`iter_assets_relay_summary`) | Org-wide | `filter`, `sort`, `name_contains`, `vendor` | id, name, analytic counts only |
| `iter_vulnerabilities_lite` | Per asset | `asset_id`, `filter`, `sort` | id, cve, name, severity, CVSS/EPSS scores, fix versions, KEV, reachability, correlation count |
| `iter_dependencies_lite` | Per asset | `composed_asset_id`, `filter`, `sort` | id, name, version, license, purls, analytic rollups |
| `iter_misconfigurations_lite` | Per asset | `asset_id`, `filter`, `sort` | check_id, name, severity, result, correlation count |
| `iter_detailed_vulnerabilities_lite` | Per asset | `asset_id`, `filter` | CVE, severity, description, preferred CVSS v3.1 vector |

For single records, use `get_asset(asset_id)` and `get_vulnerability(vulnerability_id)`. Raw `query_*` methods remain available via `sdk.graphql()` when you need exact GraphQL control.

Filtering (kwargs, `where()`, dicts, sorting) is covered in [Filtering](filtering.md).

## What Lite leaves out

Lite queries drop nested objects that are expensive to transfer:

- Vulnerability correlations (which other assets share this CVE, with per-asset risk scores)
- Remediation status (VEX justification, author, timestamps)
- Attack metadata (attack vector, attack complexity, maturity)
- Full CVSS blocks (v2/v4 impact breakdowns — Lite keeps the preferred v3.1 score)
- Exploit reference URLs and timelines
- File-level metadata (file paths, SHA-256 digests, filesystem IDs)

If you need any of these, use a full iterator or [custom GraphQL](custom-graphql.md).

## Org-wide triage

Scan all assets cheaply with Summary, then drill into flagged assets with Lite:

```python
from netrise_turbine_sdk import TurbineClient, TurbineClientConfig

sdk = TurbineClient(TurbineClientConfig.from_env())

# Pass 1: fast sweep using Summary (only id, name, and counts)
for asset in sdk.iter_assets_relay_summary(page_size=100):
    counts = asset.analytic
    if counts is None:
        continue

    # Pass 2: drill into high-risk assets with Lite queries
    if counts.vulnerability.critical + counts.vulnerability.high > 0:
        for vuln in sdk.iter_vulnerabilities_lite(asset_id=asset.id):
            print(f"{asset.name}  {vuln.cve}  {vuln.severity}  CVSS={vuln.cvss_score}")

    if counts.misconfigurations.failed > 0:
        for m in sdk.iter_misconfigurations_lite(asset_id=asset.id):
            print(f"{asset.name}  {m.check_id}  {m.severity}  {m.result}")
```

## Export vulnerabilities to CSV

```python
import csv
from netrise_turbine_sdk import TurbineClient, TurbineClientConfig

sdk = TurbineClient(TurbineClientConfig.from_env())

with open("vulns.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["asset", "cve", "severity", "cvss", "epss", "kev", "reachable"])

    for asset in sdk.iter_assets_summary(page_size=100):
        counts = asset.analytic
        if counts is None or counts.vulnerability.critical + counts.vulnerability.high == 0:
            continue
        for v in sdk.iter_vulnerabilities_lite(asset_id=asset.id):
            writer.writerow([
                asset.name,
                v.cve,
                v.severity,
                v.cvss_score,
                v.epss_score,
                v.in_known_exploited_vulnerabilities,
                v.is_reachable,
            ])
```

## Full iterators

When you need data Lite doesn't include — correlations, remediation details, exploit metadata, file paths — use the full iterators. They request every field the server exposes (depth 5), so responses are larger.

```python
# Full iterator: includes correlations, remediation, attack vector, file paths
for vuln in sdk.iter_vulnerabilities(asset_id="abc123"):
    print(vuln.cve, vuln.severity, vuln.attack_vector)
    for corr in vuln.correlations or []:
        print(f"  also in: {corr.asset_name} ({corr.location})")
    if vuln.current_remediation:
        print(f"  status: {vuln.current_remediation.status}")
```

### Full vs Lite

| Full iterator | Lite equivalent | Additional fields in Full |
| --- | --- | --- |
| `iter_assets_full` (`iter_assets_relay`) | `iter_assets` (`iter_assets_relay_lite`) | filesystems, SHA-256, CPE, file name, size, org ID, uploaded_by, group IDs/count, quantum_capable, remediation flag, full exploit/credential/cryptography rollups |
| `iter_vulnerabilities` | `iter_vulnerabilities_lite` | correlations (nested), current_remediation (nested), attack_complexity, attack_vector, maturity, file_path, vendor, version |
| `iter_dependencies` | `iter_dependencies_lite` | file metadata, digests, nested correlation details |
| `iter_misconfigurations` | `iter_misconfigurations_lite` | full correlation objects (not just count) |
| `iter_detailed_vulnerabilities` | `iter_detailed_vulnerabilities_lite` | CVSS v2/v4 impact blocks, exploit timelines, references, problem type details |

### All full iterators

| Method | Scope | Key parameters |
| --- | --- | --- |
| `iter_assets_full` (`iter_assets_relay`) | Org-wide | `filter`, `sort`, `name_contains`, `vendor` |
| `iter_assets_overview` | Org-wide | `asset_group_ids`, `filter`, `sort` |
| `iter_vulnerabilities_overview` | Org-wide | `asset_group_ids`, `filter`, `sort` |
| `iter_asset_groups` | Org-wide | `filter`, `sort` |
| `iter_users` | Org-wide | — |
| `iter_vulnerabilities` | Per asset | `asset_id`, `filter`, `sort` |
| `iter_detailed_vulnerabilities` | Per asset | `asset_id`, `filter` |
| `iter_dependencies` | Per asset | `composed_asset_id`, `filter`, `sort` |
| `iter_grouped_dependencies` | Per asset | `composed_asset_id`, `filter`, `sort`, `grouped_by` |
| `iter_misconfigurations` | Per asset | `asset_id`, `filter`, `sort` |
| `iter_certificates` | Per asset | `asset_id`, `filter`, `sort` |
| `iter_credentials` | Per asset | `asset_id`, `filter`, `sort` |
| `iter_binary_protections` | Per asset | `asset_id`, `filter`, `sort` |
| `iter_hashes` | Per asset | `asset_id`, `filter`, `sort` |
| `iter_license_issues` | Per asset | `asset_id`, `filter`, `sort` |
| `iter_list_asset_crypto_libraries` | Per asset | `asset_id`, `filter`, `sort` |
| `iter_private_keys` | Per asset | `asset_id`, `filter`, `sort` |
| `iter_public_keys` | Per asset | `asset_id`, `filter`, `sort` |
| `iter_secrets` | Per asset | `asset_id`, `filter`, `sort` |
| `iter_activity` | Per asset | `asset_id` |
| `iter_asset_group_members` | Per group | `group_id`, `sort` |

## Single-record helpers

```python
asset = sdk.get_asset("abc123")
print(asset.name, asset.status)

vuln = sdk.get_vulnerability("CVE-2024-12345")
print(vuln.id, vuln.severity)
```

The generated client also provides typed methods for mutations and lower-level single-page queries:

```python
from netrise_turbine_sdk import inputs

# Raw generated query
with sdk.graphql() as client:
    resp = client.query_asset(asset_args=inputs.AssetInput(asset_id="abc123"))
    print(resp.asset.name, resp.asset.status)

# Mutations
with sdk.graphql() as client:
    client.mutation_asset_update(
        asset_update_args=inputs.UpdateAssetInput(
            id="abc123",
            name="Updated Firmware Name",
        )
    )
```

`with sdk.graphql() as client:` is safe to use repeatedly — it does not close the underlying connection pool.
