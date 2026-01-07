<!-- Generated file: do not edit by hand -->

# query_search

Execute keyword searches across all artifacts and files in organization.

## Parameters

| name | type | required |
| --- | --- | --- |
| `search_args` | `Union[SearchInput, None, UnsetType]` | `false` |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_search()
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
