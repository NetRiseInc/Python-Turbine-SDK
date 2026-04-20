# Turbine Python SDK

Minimal, sync-first Python client for the Turbine GraphQL API.

---

## Quick Start

### 1. Install

```bash
pip install netrise-turbine-sdk
```

Also available via `poetry add netrise-turbine-sdk` or `uv add netrise-turbine-sdk`.

### 2. Configure credentials

Create a `.env` file in your project directory:

```bash
endpoint=https://apollo.turbine.netrise.io/graphql/v3
audience=https://prod.turbine.netrise.io/
domain=https://authn.turbine.netrise.io
client_id=<your_client_id>
client_secret=<your_client_secret>
organization_id=<your_org_id>
```

The SDK loads this automatically. Reach out to [support@netrise.io](mailto:support@netrise.io) if you need credentials.

### 3. Run your first query

```python
from netrise_turbine_sdk import TurbineClient, TurbineClientConfig

sdk = TurbineClient(TurbineClientConfig.from_env())

for asset in sdk.iter_assets_relay_lite(page_size=10, max_pages=1):
    print(f"{asset.name}  risk={asset.risk.score}  vulns={asset.analytic.vulnerability.critical}")
```

That's it -- authentication, pagination, and connection pooling are handled for you.

---

## Core Concepts

### Three levels of API access

The SDK is built on the Turbine GraphQL API. Rather than forcing you into a single rigid response shape, it provides three levels of access so you can choose the right trade-off between convenience and control:

| Level | What you get | When to use |
| --- | --- | --- |
| **1. Lite iterators** (recommended) | Typed, auto-paginated iterators with lean payloads | Most workflows -- lists, reports, triage, CSV exports |
| **2. Full iterators** | Same iterators but requesting every field to depth 5 | When you need deeply-nested data (correlations, remediation details, exploit metadata) |
| **3. Custom GraphQL** | Write your own queries against the full schema | When you need a specific combination of fields that no pre-built query provides |

Start at Level 1. Move to Level 2 or 3 only when you need data that the Lite response doesn't include.

### Authentication

The SDK authenticates via OAuth client credentials. Set `domain`, `client_id`, `client_secret`, `audience`, and `organization_id` in your `.env` file (or as environment variables). The SDK fetches and caches tokens automatically -- you never need to manage tokens yourself.

### Client lifecycle

`TurbineClient` manages an HTTP connection pool internally. Always close it when you're done, or use it as a context manager:

```python
# Context manager (recommended)
with TurbineClient(TurbineClientConfig.from_env()) as sdk:
    for asset in sdk.iter_assets_relay_lite():
        print(asset.name)

# Manual close
sdk = TurbineClient(TurbineClientConfig.from_env())
try:
    for asset in sdk.iter_assets_relay_lite():
        print(asset.name)
finally:
    sdk.close()
```

---

## Level 1: Lite Iterators (Start Here)

The Lite iterators are the recommended way to use the SDK. They return fast, compact responses with the fields you need for most workflows -- identifiers, scores, severity, counts -- while skipping large nested objects that inflate payloads.

Every `iter_*_lite` method handles Relay-style cursor pagination for you. You get back a plain Python iterator of typed objects -- no manual cursor tracking, no `while` loops, no `page_info` checks.

```python
for vuln in sdk.iter_vulnerabilities_lite(asset_id="abc123"):
    print(vuln.cve, vuln.severity, vuln.cvss_score)
```

All iterators accept these common keyword arguments:

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `page_size` | `int` | `100` | Number of items per server round-trip |
| `max_pages` | `int \| None` | `None` | Hard cap on pages fetched. `None` = fetch all |

### Available Lite iterators

| Method | Scope | Key parameters | Fields included |
| --- | --- | --- | --- |
| `iter_assets_relay_lite` | Org-wide | `filter`, `sort` | id, name, vendor, product, version, type, status, timestamps, risk score, analytic rollups |
| `iter_assets_relay_summary` | Org-wide | `filter`, `sort` | id, name, analytic counts only (smallest payload) |
| `iter_vulnerabilities_lite` | Per asset | `asset_id`, `filter`, `sort` | id, cve, name, severity, CVSS/EPSS scores, fix versions, KEV, reachability, correlation count |
| `iter_dependencies_lite` | Per asset | `composed_asset_id`, `filter`, `sort` | id, name, version, license, purls, analytic rollups |
| `iter_misconfigurations_lite` | Per asset | `asset_id`, `filter`, `sort` | check_id, name, severity, result, correlation count |
| `iter_detailed_vulnerabilities_lite` | Per asset | `asset_id`, `filter` | CVE, severity, description, preferred CVSS v3.1 vector |

There is also a single-item `query_vulnerability_lite` available via `sdk.graphql().query_vulnerability_lite(...)`.

### What Lite leaves out

Lite queries drop deeply-nested objects that are expensive to transfer and process:
- **Vulnerability correlations** (which other assets share this CVE, with per-asset risk scores)
- **Remediation status** (VEX justification, author, timestamps)
- **Attack metadata** (attack vector, attack complexity, maturity)
- **Full CVSS blocks** (v2/v4 impact breakdowns -- Lite keeps the preferred v3.1 score)
- **Exploit reference URLs and timelines**
- **File-level metadata** (file paths, SHA-256 digests, filesystem IDs)

If you need any of these, move to Level 2 (Full iterators) or Level 3 (custom GraphQL).

### Example: efficient org-wide triage

Scan all assets cheaply with Summary, then drill into flagged assets with Lite:

```python
from netrise_turbine_sdk import TurbineClient, TurbineClientConfig

sdk = TurbineClient(TurbineClientConfig.from_env())

# Pass 1: fast sweep using Summary (only id, name, and counts)
for asset in sdk.iter_assets_relay_summary(page_size=100):
    counts = asset.analytic

    # Pass 2: drill into high-risk assets with Lite queries
    if counts.vulnerability.critical + counts.vulnerability.high > 0:
        for vuln in sdk.iter_vulnerabilities_lite(asset_id=asset.id):
            print(f"{asset.name}  {vuln.cve}  {vuln.severity}  CVSS={vuln.cvss_score}")

    if counts.misconfigurations.failed > 0:
        for m in sdk.iter_misconfigurations_lite(asset_id=asset.id):
            print(f"{asset.name}  {m.check_id}  {m.severity}  {m.result}")
```

### Example: export vulnerabilities to CSV

```python
import csv
from netrise_turbine_sdk import TurbineClient, TurbineClientConfig

sdk = TurbineClient(TurbineClientConfig.from_env())

with open("vulns.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["asset", "cve", "severity", "cvss", "epss", "kev", "reachable"])

    for asset in sdk.iter_assets_relay_summary(page_size=100):
        if asset.analytic.vulnerability.critical + asset.analytic.vulnerability.high == 0:
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

---

## Level 2: Full Iterators

When you need data that Lite doesn't include -- correlations, remediation details, exploit metadata, file paths -- use the full iterators. These request every field the server exposes (expanded to depth 5), so responses are significantly larger.

```python
# Full iterator: includes correlations, remediation, attack vector, file paths
for vuln in sdk.iter_vulnerabilities(asset_id="abc123"):
    print(vuln.cve, vuln.severity, vuln.attack_vector)
    for corr in vuln.correlations or []:
        print(f"  also in: {corr.asset_name} ({corr.location})")
    if vuln.current_remediation:
        print(f"  status: {vuln.current_remediation.status}")
```

### Full vs Lite: what you gain

| Full iterator | Lite equivalent | Additional fields in Full |
| --- | --- | --- |
| `iter_assets_relay` | `iter_assets_relay_lite` | filesystems, SHA-256, CPE, file name, size, org ID, uploaded_by, group IDs/count, quantum_capable, remediation flag, full exploit/credential/cryptography rollups |
| `iter_vulnerabilities` | `iter_vulnerabilities_lite` | correlations (nested), current_remediation (nested), attack_complexity, attack_vector, maturity, file_path, vendor, version |
| `iter_dependencies` | `iter_dependencies_lite` | file metadata, digests, nested correlation details |
| `iter_misconfigurations` | `iter_misconfigurations_lite` | full correlation objects (not just count) |
| `iter_detailed_vulnerabilities` | `iter_detailed_vulnerabilities_lite` | CVSS v2/v4 impact blocks, exploit timelines, references, problem type details |

### All available full iterators

| Method | Scope | Key parameters |
| --- | --- | --- |
| `iter_assets_relay` | Org-wide | `filter`, `sort` |
| `iter_assets_overview` | Org-wide | `asset_group_ids`, `filter`, `sort` |
| `iter_vulnerabilities_overview` | Org-wide | `asset_group_ids`, `filter`, `sort` |
| `iter_asset_groups` | Org-wide | `filter`, `sort` |
| `iter_users` | Org-wide | -- |
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

The generated client also provides typed methods for mutations and single-page queries:

```python
from netrise_turbine_sdk_graphql import input_types as inputs

# Single asset lookup (full detail)
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

The `with sdk.graphql() as client:` pattern is safe to use repeatedly -- it does not close the underlying connection pool.

---

## Level 3: Custom GraphQL Queries

The Turbine API is a standard GraphQL endpoint. If you need a specific combination of fields that neither the Lite nor Full pre-built queries provide, you can write your own GraphQL and execute it directly. This gives you the full flexibility of GraphQL -- request exactly the fields you need, nothing more.

Use `sdk.graphql()` to get a client with managed auth and connection pooling, then call `execute()` with any valid query string:

```python
from netrise_turbine_sdk import TurbineClient, TurbineClientConfig

sdk = TurbineClient(TurbineClientConfig.from_env())
client = sdk.graphql()

# Request only the specific fields you need
response = client.execute(
    """
    query ($args: PaginatedVulnerabilitiesInput!) {
        vulnerabilities(args: $args) {
            edges {
                node {
                    id
                    cve
                    severity
                    cvssScore
                    correlations {
                        assetName
                        location
                    }
                }
            }
            pageInfo {
                endCursor
                hasNextPage
            }
        }
    }
    """,
    variables={
        "args": {
            "assetId": "abc123",
            "cursor": {"first": 50},
        }
    },
)
data = client.get_data(response)

for edge in data["vulnerabilities"]["edges"]:
    vuln = edge["node"]
    print(f"{vuln['cve']}  {vuln['severity']}  CVSS={vuln['cvssScore']}")
    for corr in vuln.get("correlations") or []:
        print(f"  also in: {corr['assetName']} at {corr['location']}")
```

### What to know about custom queries

- **Responses are plain dicts**, not typed Pydantic models. You lose autocomplete and validation but gain full field-selection control.
- **Auth is still managed for you.** The `sdk.graphql()` client handles token refresh automatically.
- **Pagination is manual.** You'll need to check `pageInfo.hasNextPage` and pass `endCursor` yourself. See the [pageInfo fields](#pagination-with-custom-queries) below.
- **The schema is your reference.** The full GraphQL schema is bundled at `sdk-artifacts/schema.graphql`. Use it to discover available types and fields.
- **Input types still work.** You can use the generated `input_types` module to build your variables, then call `.model_dump(by_alias=True)` to get the dict:

```python
from netrise_turbine_sdk_graphql.input_types import PaginatedVulnerabilitiesInput, Cursor

args = PaginatedVulnerabilitiesInput(
    assetId="abc123",
    cursor=Cursor(first=50),
)
variables = {"args": args.model_dump(by_alias=True, exclude_unset=True)}
```

### Pagination with custom queries

When paginating custom queries, include `pageInfo` in your selection and loop on `hasNextPage`:

```python
client = sdk.graphql()
cursor = None
all_vulns = []

while True:
    cursor_input = {"first": 100}
    if cursor:
        cursor_input["after"] = cursor

    data = client.get_data(client.execute(
        """
        query ($args: PaginatedVulnerabilitiesInput!) {
            vulnerabilities(args: $args) {
                edges { node { id, cve, severity, cvssScore } }
                pageInfo { endCursor, hasNextPage }
            }
        }
        """,
        variables={"args": {"assetId": "abc123", "cursor": cursor_input}},
    ))

    vulns = data["vulnerabilities"]
    for edge in vulns["edges"]:
        all_vulns.append(edge["node"])

    if not vulns["pageInfo"]["hasNextPage"]:
        break
    cursor = vulns["pageInfo"]["endCursor"]
```

### When to use each level

| | Level 1: Lite | Level 2: Full | Level 3: Custom |
| --- | --- | --- | --- |
| **Response type** | Typed Pydantic models | Typed Pydantic models | Plain dicts |
| **Pagination** | Automatic | Automatic | Manual |
| **Field selection** | Curated subset | Everything (depth 5) | You choose |
| **Best for** | Most workflows | Deep-dive analysis | Surgical queries, unique field combos |

---

## File Uploads

The SDK provides helper methods that handle the two-step upload flow (get a signed URL, then PUT the file) in a single call. Files are streamed directly from disk, so uploads work for files of any size without loading them entirely into memory.

### upload_asset

Upload a single file and submit it as an asset:

```python
from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import SubmitAssetInput

sdk = TurbineClient(TurbineClientConfig.from_env())

# Simple -- uses the filename as the asset name
resp = sdk.upload_asset("./firmware.bin")
print(f"Upload ID: {resp.asset.submit.upload_id}")

# With a display name
resp = sdk.upload_asset("./firmware.bin", name="My Firmware v1.0")

# With full metadata
resp = sdk.upload_asset(
    "./image.tar",
    submit_args=SubmitAssetInput(
        name="Router Firmware",
        product="home-router",
        manufacturer="Acme Corp",
        version="2.1.0",
    ),
)
```

**Parameters:**

| Parameter | Type | Description |
| --- | --- | --- |
| `file_path` | `str \| Path` | Path to the file to upload |
| `submit_args` | `SubmitAssetInput` | Optional metadata (name, manufacturer, model, version, type, etc.) |
| `name` | `str` | Optional display name. Defaults to the filename. Ignored if `submit_args.name` is set |

**Returns:** `MutationAssetSubmit` response containing asset info and upload details.

### upload_assets

Upload all files in a directory as assets (batch):

```python
# Simple: upload all files with default names
results = sdk.upload_assets("./firmware_images/")

# With per-file metadata
def make_args(path):
    return SubmitAssetInput(name=f"device-{path.name}", product="iot-devices")

results = sdk.upload_assets("./firmware/", submit_args_fn=make_args)

for file_path, resp in results:
    print(f"{file_path.name}: {resp.asset.submit.upload_id}")
```

**Parameters:**

| Parameter | Type | Description |
| --- | --- | --- |
| `directory` | `str \| Path` | Path to directory containing files to upload |
| `submit_args_fn` | `callable` | Optional function `(Path) -> SubmitAssetInput`. If omitted, the filename is used as the asset name |

**Returns:** List of `(Path, MutationAssetSubmit)` tuples for successfully uploaded files. Failed uploads are logged to stderr but do not stop the batch.

### Upload timeout

File uploads default to a 5-minute timeout. For very large files over slow connections, override it at construction:

```python
sdk = TurbineClient(TurbineClientConfig.from_env(), upload_timeout=600.0)
```

---

## Client Configuration Reference

All parameters are keyword-only except `config`:

```python
sdk = TurbineClient(
    config,                          # TurbineClientConfig (required)
    timeout=30.0,                    # Per-request timeout for GraphQL queries (seconds)
    upload_timeout=300.0,            # Per-request timeout for file uploads (seconds)
    max_retries=5,                   # Retry attempts for 429 / 5xx responses
    backoff_factor=0.5,              # Exponential backoff base (with jitter)
    retry_statuses=(429, 502, 503, 504),
    max_in_flight=None,              # Cap on concurrent in-flight requests
    rate_limit_per_second=None,      # Max requests/second
    rate_limit_per_minute=None,      # Max requests/minute
    httpx_client=None,               # Bring your own httpx.Client (bypasses transport stack)
)
```

### Alternate configuration methods

**Set environment variables directly (no `.env` file):**

```python
import os
os.environ["endpoint"] = "https://apollo.turbine.netrise.io/graphql/v3"
os.environ["domain"] = "https://authn.turbine.netrise.io"
os.environ["client_id"] = "your-client-id"
os.environ["client_secret"] = "your-client-secret"
os.environ["audience"] = "https://prod.turbine.netrise.io/"
os.environ["organization_id"] = "your-org-id"

cfg = TurbineClientConfig.from_env(load_env_file=False)
```

**Load a `.env` file from a custom path:**

```python
from dotenv import load_dotenv
load_dotenv("/path/to/custom.env")

cfg = TurbineClientConfig.from_env(load_env_file=False)
```

---

## API Documentation & Code Samples

<!-- Index is auto-generated below this point -->

- [mutation_add_asset_groups_to_assets](operations/mutation_add_asset_groups_to_assets.md): Associate a list of existing asset groups with selected assets.
- [mutation_add_assets_to_asset_group](operations/mutation_add_assets_to_asset_group.md): Add specified assets to an existing asset group for organization.
- [mutation_asset_add_dependency](operations/mutation_asset_add_dependency.md): Manually inject a missing dependency component into an asset's inventory.
- [mutation_asset_modify_dependency](operations/mutation_asset_modify_dependency.md): Update metadata or details for a manually added asset dependency.
- [mutation_asset_remove_dependencies](operations/mutation_asset_remove_dependencies.md): Remove specific dependencies from the component list of an asset.
- [mutation_asset_submit](operations/mutation_asset_submit.md): Upload firmware or SBOMs with metadata, group assignments, and CPEs.
- [mutation_asset_update](operations/mutation_asset_update.md): Modify metadata such as name, vendor, or version for assets.
- [mutation_create_asset_group](operations/mutation_create_asset_group.md): Create a new named group to organize and track assets.
- [mutation_delete_asset_group](operations/mutation_delete_asset_group.md): Permanently remove an asset group while keeping contained assets intact.
- [mutation_remediate_all_asset_vulnerabilities](operations/mutation_remediate_all_asset_vulnerabilities.md): Apply a remediation status to all vulnerabilities matching specific filters.
- [mutation_remediate_asset_vulnerabilities](operations/mutation_remediate_asset_vulnerabilities.md): Bulk apply VEX remediation status to multiple vulnerabilities on assets.
- [mutation_remediate_asset_vulnerability](operations/mutation_remediate_asset_vulnerability.md): Update remediation status and justification for a single asset vulnerability.
- [mutation_remediate_certificates](operations/mutation_remediate_certificates.md): Update remediation status and notes for certificate issues found in assets.
- [mutation_remediate_license_issues](operations/mutation_remediate_license_issues.md): Update status and add notes to resolve identified license issues.
- [mutation_remediate_private_keys](operations/mutation_remediate_private_keys.md): Apply remediation status to private key exposures discovered in assets.
- [mutation_remediate_public_keys](operations/mutation_remediate_public_keys.md): Update remediation status for public key issues identified in assets.
- [mutation_remediate_secrets](operations/mutation_remediate_secrets.md): Apply remediation status and justification to exposed secrets in assets.
- [mutation_remove_all_asset_groups_from_assets](operations/mutation_remove_all_asset_groups_from_assets.md): Disassociate all asset groups from a specified list of assets.
- [mutation_remove_assets_from_asset_group](operations/mutation_remove_assets_from_asset_group.md): Remove selected assets from a specific asset group container configuration.
- [mutation_set_asset_groups_to_asset](operations/mutation_set_asset_groups_to_asset.md): Replace all current group associations for an asset with new ones.
- [mutation_set_assets_to_asset_group](operations/mutation_set_assets_to_asset_group.md): Overwrite the member list of an asset group with new assets.
- [mutation_submit_rise_ai_analysis](operations/mutation_submit_rise_ai_analysis.md): Request a RISE AI analysis for an eligible asset to generate insights.
- [mutation_update_asset_group](operations/mutation_update_asset_group.md): Rename or update the description of an existing asset group.
- [mutation_update_org_level_settings](operations/mutation_update_org_level_settings.md): Configure global organization settings such as idle session timeout duration.
- [mutation_user_action](operations/mutation_user_action.md): Perform administrative actions like enabling or disabling specific user accounts.
- [mutation_user_delete](operations/mutation_user_delete.md): Permanently delete a user account and remove their access rights.
- [mutation_user_invite](operations/mutation_user_invite.md): Invite a new user to the organization with a specific role.
- [mutation_user_remove](operations/mutation_user_remove.md): Remove a user from the organization without deleting their account.
- [mutation_user_reset_password](operations/mutation_user_reset_password.md): Trigger a password reset email for a specific user account.
- [mutation_user_set_user_role](operations/mutation_user_set_user_role.md): Assign a new permission role like Owner or Operator to users.
- [mutation_user_update_user](operations/mutation_user_update_user.md): Modify user profile information including name and contact email details.
- [query_activity](operations/query_activity.md): Retrieve a comprehensive log of actions and events for assets.
- [query_analytics](operations/query_analytics.md): Access high-level risk data and charts for organization dashboards.
- [query_asset](operations/query_asset.md): Retrieve detailed metadata and risk information for a single asset.
- [query_asset_group_analytics](operations/query_asset_group_analytics.md): View risk metrics and exploit counts for a specific group.
- [query_asset_group_members](operations/query_asset_group_members.md): List all assets associated with a specific asset group container.
- [query_asset_groups](operations/query_asset_groups.md): Retrieve a detailed paginated list of all asset groups available.
- [query_asset_status](operations/query_asset_status.md): Check if an asset is currently processing or has finished.
- [query_asset_upload](operations/query_asset_upload.md): Obtain a secure pre-signed URL to upload files for analysis.
- [query_asset_vulnerability_remediation](operations/query_asset_vulnerability_remediation.md): Retrieve current VEX status and justification for a specific vulnerability.
- [query_assets_overview](operations/query_assets_overview.md): View high-level risk and threat exposure metrics for multiple assets.
- [query_assets_relay](operations/query_assets_relay.md): Retrieve a paginated, sortable list of assets with filtering options.
- [query_assets_relay_lite](operations/query_assets_relay_lite.md): Retrieve assets with trimmed fields — keeps identity, status, risk score, and analytic rollups; drops filesystems, SHA-256, exploit trees, and credential counts.
- [query_assets_relay_summary](operations/query_assets_relay_summary.md): Retrieve minimal asset data — ID, name, and analytic counts only — for fast org-wide sweeps to decide which assets need deeper queries.
- [query_binary_protections](operations/query_binary_protections.md): List security hardening details for binaries found within the asset.
- [query_binary_protections_summary](operations/query_binary_protections_summary.md): Get aggregated counts of binary hardening features like NX or PIE.
- [query_certificate_external_filters](operations/query_certificate_external_filters.md): Retrieve available filter options for certificate queries.
- [query_certificates](operations/query_certificates.md): List X.509 certificates and validity status found in the asset.
- [query_credentials](operations/query_credentials.md): Identify user accounts and password hashes discovered within the filesystem.
- [query_dependencies](operations/query_dependencies.md): List all software components and libraries identified in the asset.
- [query_dependencies_lite](operations/query_dependencies_lite.md): List dependencies with trimmed fields — keeps identity, version, license, purls, and analytic rollups; drops file metadata, digests, and nested correlation details.
- [query_dependency_known_exploits](operations/query_dependency_known_exploits.md): Check if specific dependencies are linked to known public exploits.
- [query_detailed_vulnerabilities](operations/query_detailed_vulnerabilities.md): Retrieve in-depth vulnerability data including descriptions and CVSS vector strings.
- [query_detailed_vulnerabilities_lite](operations/query_detailed_vulnerabilities_lite.md): Retrieve vulnerability descriptions with preferred CVSS v3.1 scores only — drops full v2/v4 impact blocks, exploit timelines, references, and problem type details.
- [query_download_extracted_firmware](operations/query_download_extracted_firmware.md): Generate a URL to download the full unpacked file system.
- [query_download_file](operations/query_download_file.md): Create a secure link to download a specific individual file.
- [query_download_file_list](operations/query_download_file_list.md): Generate a URL to download a list of all files.
- [query_download_firmware](operations/query_download_firmware.md): Generate a link to download the original uploaded firmware image.
- [query_get_ai_model_data](operations/query_get_ai_model_data.md): Retrieve configuration and metadata for a specific AI model integration.
- [query_get_vuln_reachability](operations/query_get_vuln_reachability.md): Determine if a vulnerability can be executed via system paths.
- [query_grouped_dependencies](operations/query_grouped_dependencies.md): View dependencies aggregated by vendor, license, or specific component type.
- [query_hashes](operations/query_hashes.md): List cryptographic hashes for files identified within the asset filesystem.
- [query_identified_components_preview](operations/query_identified_components_preview.md): Return organization-wide component counts filtered by enabled identification methods, with before/after deltas when verification settings change.
- [query_license](operations/query_license.md): Retrieve detailed information for a specific software license.
- [query_license_issue](operations/query_license_issue.md): Get details about a specific license compliance issue.
- [query_license_issues](operations/query_license_issues.md): List license compliance issues identified across asset components.
- [query_license_issues_external_filters](operations/query_license_issues_external_filters.md): Retrieve available filter options for license issue queries.
- [query_licenses_spdx_ids](operations/query_licenses_spdx_ids.md): List available SPDX license identifiers for filtering and reference.
- [query_list_ai_providers](operations/query_list_ai_providers.md): List available AI provider integrations and their current status.
- [query_list_asset_correlations](operations/query_list_asset_correlations.md): Retrieve cross-asset correlation data linking shared components and vulnerabilities.
- [query_list_asset_crypto_libraries](operations/query_list_asset_crypto_libraries.md): List cryptographic libraries and algorithms detected within an asset.
- [query_match_vulnerabilities](operations/query_match_vulnerabilities.md): Find specific vulnerabilities matching a provided component identifier or package.
- [query_metrics](operations/query_metrics.md): View organization-wide statistics on asset counts, processing, and risk.
- [query_misconfigurations](operations/query_misconfigurations.md): List failed security checks and configuration risks found in assets.
- [query_misconfigurations_lite](operations/query_misconfigurations_lite.md): List misconfigurations with trimmed fields — keeps check ID, name, severity, result, and correlation count; drops nested correlation objects.
- [query_org_level_information](operations/query_org_level_information.md): Retrieve organization-level metadata such as last-updated time, optionally scoped by asset groups.
- [query_org_level_settings](operations/query_org_level_settings.md): Check how the tenant organization is configured.
- [query_package_dependencies_by_id](operations/query_package_dependencies_by_id.md): View the dependency tree hierarchy for a specific software package.
- [query_private_key_external_filters](operations/query_private_key_external_filters.md): Retrieve available filter options for private key queries.
- [query_private_keys](operations/query_private_keys.md): Detect private cryptographic keys stored insecurely on the asset filesystem.
- [query_public_key_external_filters](operations/query_public_key_external_filters.md): Retrieve available filter options for public key queries.
- [query_public_keys](operations/query_public_keys.md): List public cryptographic keys found within the asset's file system.
- [query_rise_ai_analysis_data](operations/query_rise_ai_analysis_data.md): Check for the contents of the RISE AI analysis report.
- [query_rise_ai_availability](operations/query_rise_ai_availability.md): Check eligibility and status of RISE AI analysis for an asset.
- [query_search](operations/query_search.md): Execute keyword searches across all artifacts and files in organization.
- [query_secret](operations/query_secret.md): Retrieve detailed information about a specific discovered secret.
- [query_secret_categories_summary](operations/query_secret_categories_summary.md): Get aggregated counts of secrets grouped by category type.
- [query_secret_status_count](operations/query_secret_status_count.md): Retrieve counts of secrets grouped by remediation status.
- [query_secret_types_and_count](operations/query_secret_types_and_count.md): List secret types discovered with their occurrence counts.
- [query_secrets](operations/query_secrets.md): List all secrets and sensitive data discovered within an asset.
- [query_secrets_summary](operations/query_secrets_summary.md): Get a high-level overview of secret findings and exposure metrics.
- [query_sift](operations/query_sift.md): Perform fuzzy hash matching to find similar code or files.
- [query_user_orgs](operations/query_user_orgs.md): List all organizations the current user is authorized to access.
- [query_users](operations/query_users.md): Retrieve a detailed list of all users and their assigned roles.
- [query_vulnerabilities](operations/query_vulnerabilities.md): List CVEs and associated risks for components in an asset.
- [query_vulnerabilities_lite](operations/query_vulnerabilities_lite.md): List vulnerabilities with trimmed fields — keeps CVE, severity, CVSS/EPSS scores, fix versions, and correlation count; drops nested correlations and remediation details.
- [query_vulnerabilities_overview](operations/query_vulnerabilities_overview.md): Get a summary of vulnerability counts and severity across assets.
- [query_vulnerability](operations/query_vulnerability.md): Retrieve detailed metadata, scores, and descriptions for a specific vulnerability.
- [query_vulnerability_external_filters](operations/query_vulnerability_external_filters.md): Count vulnerabilities matching external threat feeds like CISA or botnets.
- [query_vulnerability_lite](operations/query_vulnerability_lite.md): Retrieve a single vulnerability with preferred CVSS v3.1 score only — drops full v2/v4 impact blocks, exploit references, and problem type details.
