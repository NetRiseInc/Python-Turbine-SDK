<!-- Generated file: do not edit by hand -->

# query_user_orgs

List all organizations the current user is authorized to access.

## Parameters

| name | type | required |
| --- | --- | --- |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `userOrgs[]` | `object` | yes |
| `userOrgs[].DisplayName` | `string` | no |
| `userOrgs[].Id` | `string` | no |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_user_orgs()
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
