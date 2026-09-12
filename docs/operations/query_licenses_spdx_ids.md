<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# query_licenses_spdx_ids

[Back to the index](../README.md)

List SPDX license identifiers.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |

## Response fields

Typed attributes on the response model.

| Field | Type | Nullable |
| --- | --- | --- |
| `licensesSpdxIds[]` | `string` | yes |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_licenses_spdx_ids()
        # Responses are typed Pydantic models: read fields as attributes.
        for value in resp.licenses_spdx_ids or []:
            print(value)


if __name__ == "__main__":
    main()
```
