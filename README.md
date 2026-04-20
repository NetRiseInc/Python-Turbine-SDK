# Turbine Python SDK

Minimal, sync-first Python client for the Turbine GraphQL API.

## Getting Started

### Installation from PyPI

Install from PyPI as `netrise-turbine-sdk`:

```bash
# pip
pip install netrise-turbine-sdk

# poetry
poetry add netrise-turbine-sdk

# uv
uv add netrise-turbine-sdk
```

### Configure environment variables

The SDK automatically loads environment variables from a `.env` file in your current working directory when you call `TurbineClientConfig.from_env()`. You can also set environment variables directly.

**Option 1: Using a `.env` file (recommended)**

Create a `.env` file in your project directory:

```bash
endpoint=https://apollo.turbine.netrise.io/graphql/v3
audience=https://prod.turbine.netrise.io/
domain=https://authn.turbine.netrise.io
client_id=<client_id>
client_secret=<client_secret>
organization_id=<org_id>
```

The SDK will automatically load these when you call `TurbineClientConfig.from_env()`. The `.env` file is searched in:

- Current working directory (most common)
- Parent directories (walks up the directory tree)

**Option 2: Set environment variables directly**

```python
import os
os.environ["endpoint"] = "https://apollo.turbine.netrise.io/graphql/v3"
# ... set other variables

cfg = TurbineClientConfig.from_env(load_env_file=False)
```

**Option 3: Disable automatic .env loading**

If you prefer to load `.env` files manually:

```python
from dotenv import load_dotenv
load_dotenv()  # Your custom loading logic

cfg = TurbineClientConfig.from_env(load_env_file=False)
```

Populate the missing values. Reach out to [mailto:support@netrise.io](support@netrise.io) if you need assistance.

## Union Field Aliasing Convention

When GraphQL union types have members with identically-named fields that return different types, the SDK automatically applies aliases to disambiguate them. This is necessary because code generators cannot create a single Python type for fields with conflicting return types.

### Naming Convention

Aliased fields follow the pattern: `{camelCaseTypeName}{PascalCaseFieldName}`

For example, the `NotificationControl` union has `AssetAnalysisControl` and `UserManagementControl` types that both define an `events` field with different return types. In the generated SDK, these become:

- `AssetAnalysisControl.events` → `assetAnalysisControlEvents`
- `UserManagementControl.events` → `userManagementControlEvents`

### Example Usage

```python
# Accessing aliased fields on union type members
notification_settings = client.query_notification_settings()

for pref in notification_settings.preferences:
    for control in pref.controls:
        # Access the aliased field based on the control type
        if hasattr(control, 'assetAnalysisControlEvents'):
            events = control.assetAnalysisControlEvents
        elif hasattr(control, 'userManagementControlEvents'):
            events = control.userManagementControlEvents
```

This aliasing is applied automatically during SDK generation and only affects fields that would otherwise cause type conflicts.

## Reducing response size (Lite / Summary queries)

The default `query_*` and `iter_*` methods request every scalar and nested
object the server exposes. That is convenient for exploration but can be
expensive: for a large asset sweep the full `query_assets_relay` payload
includes full `analytic`, `risk`, `filesystems`, exploit rollups, and
asset-group metadata per node. When you only need enough data to decide
"should I fetch deeper?" the SDK ships trimmed counterparts that typically
cut the response body by ~70–80%:

| Full paginator | Lite variant | Summary variant |
| --- | --- | --- |
| `iter_assets_relay` | `iter_assets_relay_lite` | `iter_assets_relay_summary` |
| `iter_vulnerabilities` | `iter_vulnerabilities_lite` | — |
| `iter_dependencies` | `iter_dependencies_lite` | — |
| `iter_misconfigurations` | `iter_misconfigurations_lite` | — |
| `iter_detailed_vulnerabilities` | `iter_detailed_vulnerabilities_lite` | — |
| `query_vulnerability` | `query_vulnerability_lite` | — |

The Lite variants keep the fields most callers use (top-level identifiers,
severity, CVSS score, rollup counts) and drop deeply-nested objects like
`exploit.references`, `correlations`, `currentRemediation`, full CVSS v2 /
v3 / v4 blocks, and component digests. The `Summary` variant of the assets
query is even thinner and returns only `id`, `name`, and
`analytic.{vulnerability,misconfigurations,components}`.

### When to pick which

1. **Full (`iter_assets_relay`, etc.)** — you need every field for audit /
   export / BI use cases and bandwidth is not a concern.
2. **Lite (`iter_*_lite`)** — you want a table-friendly view plus a couple
   of CVSS / EPSS scalars. Good default for UIs and CSV exports.
3. **Summary (`iter_assets_relay_summary`)** — you are performing an
   org-wide sweep to decide which assets to drill into. Combine with a
   follow-up `iter_vulnerabilities`/`iter_misconfigurations`/`iter_dependencies`
   call gated on non-zero counts in `analytic` to avoid the N+1 fanout
   described in the SDK FAQ.

### Example: surgical sweep

```python
from netrise_turbine_sdk import TurbineClient, TurbineClientConfig

sdk = TurbineClient(TurbineClientConfig.from_env())

for asset in sdk.iter_assets_relay_summary(page_size=100):
    counts = asset.analytic
    if counts.vulnerability.critical + counts.vulnerability.high > 0:
        for vuln in sdk.iter_vulnerabilities_lite(asset_id=asset.id):
            print(asset.name, vuln.cve, vuln.severity, vuln.cvss_score)
    if counts.misconfigurations.failed > 0:
        for m in sdk.iter_misconfigurations_lite(asset_id=asset.id):
            print(asset.name, m.check_id, m.severity, m.result)
```

With the asset sweep payload trimmed to `~3` fields per node and
`iter_vulnerabilities_lite` dropping CVSS v2/v4 plus exploit / correlation
blocks, scenario A from the customer write-up (`100 assets × 60 vulns`)
moves from ~601 full-weight calls to ~601 Lite calls at roughly 20–30%
of the original wire bytes.

## License

See [LICENSE](https://github.com/NetRiseInc/Python-Turbine-SDK/blob/main/LICENSE) for details.

## Documentation

- [API Documentation & Code Samples](https://github.com/NetRiseInc/Python-Turbine-SDK/blob/main/docs/README.md) - detailed examples for all client SDK operations.
