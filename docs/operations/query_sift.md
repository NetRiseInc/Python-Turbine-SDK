<!-- Generated file: do not edit by hand -->

# query_sift

Perform fuzzy hash matching to find similar code or files.

## Parameters

| name | type | required |
| --- | --- | --- |

## Response Schema

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
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
