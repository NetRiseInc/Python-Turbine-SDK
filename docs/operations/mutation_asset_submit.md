<!-- Generated file: do not edit by hand -->

# mutation_asset_submit

## Parameters

| name | type | required |
| --- | --- | --- |
| `asset_submit_file_name` | `str` | `true` |
| `asset_submit_args` | `Union[SubmitAssetInput, None, UnsetType]` | `false` |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.mutation_asset_submit(asset_submit_file_name='example')
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
