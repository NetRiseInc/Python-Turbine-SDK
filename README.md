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

## License

See [LICENSE](https://github.com/NetRiseInc/Python-Turbine-SDK/blob/main/LICENSE) for details.

## Documentation

- [API Documentation & Code Samples](https://github.com/NetRiseInc/Python-Turbine-SDK/blob/main/docs/README.md) - detailed examples for all client SDK operations.
