# Turbine Python SDK

Minimal, sync-first Python client for the Turbine GraphQL API.

## Getting started

Install from PyPI (`pip`, `poetry add`, or `uv add`):

```bash
pip install netrise-turbine-sdk
```

Create a `.env` file in your project directory — `TurbineClientConfig.from_env()` loads it automatically (current directory, then parents):

```bash
endpoint=https://apollo.turbine.netrise.io/graphql/v3
audience=https://prod.turbine.netrise.io/
domain=https://authn.turbine.netrise.io
client_id=<client_id>
client_secret=<client_secret>
organization_id=<org_id>
```

Prefer plain environment variables or your own dotenv loading? Set the same names in the environment and call `TurbineClientConfig.from_env(load_env_file=False)`.

Need credentials? Contact [support@netrise.io](mailto:support@netrise.io).

Want the full experience? `uv tool install netrise-turbine-cli` adds the `turbine` CLI (SDK included), and `turbine skill install` adds the agent skill to Cursor, Claude Code, Codex, and opencode.

## Versioning and stability

- `netrise_turbine_sdk` (the wrapper) is semver-stable: existing imports, method names, and call signatures do not break without an intentional minor/major bump.
- `netrise_turbine_sdk_graphql` (generated) tracks the Turbine GraphQL schema. Fully typed, power-user surface; schema refreshes are guarded by API-surface snapshot tests and a schema-diff gate.

See `CHANGELOG.md` for release notes.

## Union field aliasing

When GraphQL union members declare same-named fields with different types, the generator aliases them as `{camelCaseTypeName}{PascalCaseFieldName}` so each gets its own Python type. Example — both `NotificationControl` members define `events`:

```python
for pref in client.query_notification_settings().preferences:
    for control in pref.controls:
        if hasattr(control, "assetAnalysisControlEvents"):
            events = control.assetAnalysisControlEvents
        elif hasattr(control, "userManagementControlEvents"):
            events = control.userManagementControlEvents
```

## Reducing response size (Lite / Summary)

Full `query_*` / `iter_*` methods request every field the server exposes. The trimmed counterparts typically cut response bytes 70–80%:

| Full | Lite | Summary |
| --- | --- | --- |
| `iter_assets_relay` | `iter_assets_relay_lite` | `iter_assets_relay_summary` |
| `iter_vulnerabilities` | `iter_vulnerabilities_lite` | — |
| `iter_dependencies` | `iter_dependencies_lite` | — |
| `iter_misconfigurations` | `iter_misconfigurations_lite` | — |
| `iter_detailed_vulnerabilities` | `iter_detailed_vulnerabilities_lite` | — |
| `query_vulnerability` | `query_vulnerability_lite` | — |

Rule of thumb: **Full** for audit/export, **Lite** for tables and CSVs (identifiers, severity, CVSS/EPSS, rollup counts), **Summary** for org-wide sweeps (`id`, `name`, `analytic` counts only). Sweep with Summary, then drill in only where counts are non-zero:

```python
from netrise_turbine_sdk import TurbineClient, TurbineClientConfig

sdk = TurbineClient(TurbineClientConfig.from_env())

for asset in sdk.iter_assets_relay_summary(page_size=100):
    counts = asset.analytic
    if counts.vulnerability.critical + counts.vulnerability.high > 0:
        for vuln in sdk.iter_vulnerabilities_lite(asset_id=asset.id):
            print(asset.name, vuln.cve, vuln.severity, vuln.cvss_score)
```

## File listing

`list_files` returns the complete recursive file listing for an asset in one call:

```python
files = sdk.list_files("your-asset-id")
for f in files:
    print(f["filesystemPath"], f.get("size"), f.get("mimeType"))
```

Entries are dicts with keys like `path`, `filesystemPath`, `size`, `mimeType`, `hashSha256`, `permissions`, and `hasChildren`.

## Documentation

[API documentation and code samples](https://github.com/NetRiseInc/Python-Turbine-SDK/blob/main/docs/README.md) — quick start, filtering cookbook, error handling, and per-operation pages.

## License

See [LICENSE](https://github.com/NetRiseInc/Python-Turbine-SDK/blob/main/LICENSE).
