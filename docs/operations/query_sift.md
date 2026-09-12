<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# query_sift

[Back to the index](../README.md)

Fuzzy-hash match to find similar code or files.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |

## Response fields

Typed attributes on the response model.

| Field | Type | Nullable |
| --- | --- | --- |
| `sift` | `object` | yes |
| `sift.count` | `object` | yes |
| `sift.count.assetCount` | `integer` | no |
| `sift.count.fileCount` | `integer` | no |
| `sift.count.pythonFileCount` | `integer` | no |
| `sift.count.scriptFileCount` | `integer` | no |
| `sift.count.textFileCount` | `integer` | no |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_sift()
        # Responses are typed Pydantic models: read fields as attributes.
        print(resp.sift.count.asset_count, resp.sift.count.file_count)


if __name__ == "__main__":
    main()
```
