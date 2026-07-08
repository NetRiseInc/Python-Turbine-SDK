# Changelog

All notable changes to `netrise-turbine-sdk` are documented here.

## Unreleased

### Added

- REST-friendly SDK helpers: `iter_assets`, `iter_assets_full`,
  `iter_assets_summary`, `get_asset`, and `get_vulnerability`.
- Convenience filtering via iterator keyword arguments and `where(...)`.
- `Paginator` metadata and helpers: `total_count`, `last_cursor`,
  `pages_fetched`, `first()`, `to_list(limit=...)`, `start_after`, and
  `max_items`.
- API-surface snapshot tests, schema-diff gate, `py.typed` markers, and
  test-gated publishing.
- TypeScript SDK codegen now reads the shared query directory so Lite
  operations are generated for both SDKs.
- Tiered install: the CLI is PyPI-publishable (version dependency on the SDK
  instead of a path), bundles a self-contained agent skill in the wheel, and
  gains `turbine skill install/uninstall/status` targeting Cursor, Claude
  Code, and Codex skill directories.
- Upload lifecycle helpers: `resolve_upload(upload_id)` maps an upload to its
  asset, and `wait_for_asset(asset_id=…|upload_id=…)` blocks until analysis
  completes. CLI: `asset status` accepts `--upload-id` and `--wait`
  (`--interval` / `--timeout`), and `asset upload` gains `--wait` plus
  enriched output (`assetId`, `uploadId`) instead of the raw submit response.
- Docs-driven CLI contract tests: every `turbine …` example advertised in
  README, SKILL.md, reference.md, docs/human.md, and docs/agent.md is
  extracted and executed — offline dry-run always (`make turbine-cli-test`),
  and live read-only against the org via `make turbine-cli-docs-test`
  (mutations always stay `--dry-run`). Includes a reference.md flag-existence
  check and a coverage guard that fails if a registered command is
  undocumented.
- CLI: `turbine api schema` now works from any install — the GraphQL schema
  snapshot is bundled into the wheel (`_generated/schema.graphql`).

### Changed

- Composed asset IDs (`<id>|<revision>`) are no longer exposed: the SDK's
  `resolve_upload` strips the internal `|<revision>` suffix from `asset_id`,
  and the CLI strips it from every output value under `composedAssetId` /
  `assetId` keys (all commands and output modes). Inputs named
  `composedAssetId` are interchangeable with the plain asset ID — SKILL.md
  and docs/agent.md now say to always pass the bare `ASSET_ID`.
- `--limit` in curated CLI list commands now flows through SDK `max_items`
  while preserving existing client-side truncation behavior as a backstop.
- Per-operation docs now show typed-attribute examples, "prefer the wrapper"
  callouts, and generated filter-field tables; docs README gained "Handling
  errors" and a filtering cookbook.

### Fixed

- CLI: explicit `-o table` is honored when stdout is piped (previously fell
  back to JSON).
- CLI: the documented `turbine search <term>` invocation works; `artifacts`
  defaults to all artifact types with an optional `--artifacts` override.
- CLI: `api graphql` failures emit structured errors and exit codes instead
  of raw tracebacks.
- CLI: generated `api` commands whose input requires a pagination cursor
  (e.g. `api assets-overview`) now default it to `{"first": 100}`, so bare
  invocations work instead of failing validation.
- CLI: validation errors no longer suggest options that don't exist (e.g.
  `--cursor: Field required`); fields without a real flag are reported as
  input fields with a `--input` hint.
- CLI: `turbine org info` no longer crashes with a missing-argument error
  (the operation's args object is now passed explicitly).
- CLI: `turbine component grouped` defaults `--group-by` to `VENDOR` — the
  API rejects requests without a group-by field.
- Docs: fixed broken examples caught by the contract suite — `vuln
  remediate` inputs now use the real `remediationId`/`remediationIds`/
  `vulnerabilityFilter` shapes with valid enum justifications, list-typed
  nested inputs are emitted as arrays, boolean flags are emitted value-less,
  `api secret` uses a `SECRET_ID` placeholder (not `ASSET_ID`), `api
  asset-upload` shows `--upload-id`, `api grouped-dependencies` includes
  `--grouped-by VENDOR`, and `api schema --type` uses a type that exists
  (`Asset`).

## 0.1.17

### Added

- Generated Turbine GraphQL Python client and handwritten synchronous wrapper.
- High-level iterator helpers for Relay-style pagination.
- Upload, file-listing, remediation, and user-management helpers.
