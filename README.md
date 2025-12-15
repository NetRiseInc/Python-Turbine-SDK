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

Create a `.env` file in your project root:

```bash
TURBINE_API_URL=https://your-turbine-instance.com/graphql
TURBINE_API_TOKEN=your_api_token_here
```

### Basic usage

```python
from netrise_turbine_sdk import TurbineClient, TurbineClientConfig

# Initialize client (reads from .env automatically)
config = TurbineClientConfig()
client = TurbineClient(config)

# Example: Query assets
result = client.assets_relay()
print(result.data)
```

## Documentation

- [Operations documentation](docs/operations/) - detailed examples for all GraphQL operations
- [API Reference](docs/README.md) - complete API documentation

## License

See [LICENSE](LICENSE) for details.
