<!-- Generated file: do not edit by hand -->

# query_asset_group_members

List all assets associated with a specific asset group container.

## Parameters

| name | type | required |
| --- | --- | --- |
| `asset_group_members_args` | `AssetGroupMembersInput` | `true` |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    AssetGroupMembersInput,
    Cursor,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_asset_group_members(asset_group_members_args=AssetGroupMembersInput(group_id='group_123', cursor=Cursor()))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
