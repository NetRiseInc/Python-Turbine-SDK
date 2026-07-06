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

### Changed

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

## 0.1.17

### Added

- Generated Turbine GraphQL Python client and handwritten synchronous wrapper.
- High-level iterator helpers for Relay-style pagination.
- Upload, file-listing, remediation, and user-management helpers.
