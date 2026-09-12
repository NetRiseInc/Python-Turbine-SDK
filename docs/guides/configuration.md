# Configuration

## Constructor

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
    extra_headers=None,              # Extra HTTP headers on every GraphQL request
)
```

## Alternate configuration

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

## Extra headers

Useful when your organization has a header-based exemption (for example a rate-limit bypass secret):

```python
from netrise_turbine_sdk import TurbineClient, TurbineClientConfig

sdk = TurbineClient(
    TurbineClientConfig.from_env(),
    extra_headers={"X-RateLimit-Bypass": "<your-secret>"},
)
```

Or set `TURBINE_EXTRA_HEADERS` to a JSON object — no code changes needed, and the `turbine` CLI picks it up too:

```bash
TURBINE_EXTRA_HEADERS='{"X-RateLimit-Bypass": "<your-secret>"}'
```

An explicit `extra_headers=` argument takes precedence over the environment variable (pass `{}` to disable it). The `Authorization` header is always managed by the client and cannot be overridden.

## Union field aliasing

When GraphQL union members declare same-named fields with different types, the generator aliases them as `{camelCaseTypeName}{PascalCaseFieldName}` so each gets its own Python type. Read the aliased attribute that matches the concrete member you have, or check with `hasattr` before accessing.

## Client lifecycle

`TurbineClient` manages an HTTP connection pool internally. Always close it when you're done, or use it as a context manager:

```python
# Context manager (recommended)
with TurbineClient(TurbineClientConfig.from_env()) as sdk:
    for asset in sdk.iter_assets():
        print(asset.name)

# Manual close
sdk = TurbineClient(TurbineClientConfig.from_env())
try:
    for asset in sdk.iter_assets():
        print(asset.name)
finally:
    sdk.close()
```
