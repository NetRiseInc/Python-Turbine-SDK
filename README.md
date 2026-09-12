# Turbine Python SDK

Minimal, sync-first Python client for the Turbine GraphQL API.

## Getting started

```bash
pip install netrise-turbine-sdk
```

Also available via `poetry add` or `uv add`.

Create a `.env` in your project directory — `TurbineClientConfig.from_env()` loads it automatically (current directory, then parents):

```bash
endpoint=https://apollo.turbine.netrise.io/graphql/v3
audience=https://prod.turbine.netrise.io/
domain=https://authn.turbine.netrise.io
client_id=<client_id>
client_secret=<client_secret>
organization_id=<org_id>
```

Prefer plain environment variables? Set the same names and call `TurbineClientConfig.from_env(load_env_file=False)`.

Need credentials? Contact [support@netrise.io](mailto:support@netrise.io).

```python
from netrise_turbine_sdk import TurbineClient, TurbineClientConfig

sdk = TurbineClient(TurbineClientConfig.from_env())

for asset in sdk.iter_assets(page_size=10, max_pages=1):
    print(asset.name, asset.risk.score)
```

Want the CLI and agent skill too? `uv tool install netrise-turbine-cli`, then `turbine skill install`.

## Versioning and stability

- `netrise_turbine_sdk` (the wrapper) is semver-stable: existing imports, method names, and call signatures do not break without an intentional minor/major bump.
- `netrise_turbine_sdk_graphql` (generated) tracks the Turbine GraphQL schema. Fully typed; schema refreshes are guarded by API-surface snapshot tests and a schema-diff gate.

See `CHANGELOG.md` for release notes.

## Documentation

| Page | Covers |
| --- | --- |
| [Docs hub](https://github.com/NetRiseInc/Python-Turbine-SDK/blob/main/docs/README.md) | Quick start, level picker, operations index |
| [Iterators](https://github.com/NetRiseInc/Python-Turbine-SDK/blob/main/docs/guides/iterators.md) | Lite / Full / Summary, pagination |
| [Filtering](https://github.com/NetRiseInc/Python-Turbine-SDK/blob/main/docs/guides/filtering.md) | kwargs, `where()`, sorting |
| [Custom GraphQL](https://github.com/NetRiseInc/Python-Turbine-SDK/blob/main/docs/guides/custom-graphql.md) | `execute()`, manual pagination |
| [Errors](https://github.com/NetRiseInc/Python-Turbine-SDK/blob/main/docs/guides/errors.md) | Exception types and retries |
| [Files and uploads](https://github.com/NetRiseInc/Python-Turbine-SDK/blob/main/docs/guides/files-and-uploads.md) | `list_files`, `upload_asset` |
| [Configuration](https://github.com/NetRiseInc/Python-Turbine-SDK/blob/main/docs/guides/configuration.md) | Constructor, extra headers, lifecycle |

Lite iterators cut response size for everyday work; Full and custom GraphQL cover the rest — details in the iterators and custom-GraphQL guides. Union field aliasing is covered under configuration.

## License

See [LICENSE](https://github.com/NetRiseInc/Python-Turbine-SDK/blob/main/LICENSE).
