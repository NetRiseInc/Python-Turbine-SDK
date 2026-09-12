<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# query_user_orgs

[Back to the index](../README.md)

List organizations the current user can access.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |

## Response fields

Typed attributes on the response model.

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
        # Responses are typed Pydantic models: read fields as attributes.
        for item in resp.user_orgs or []:
            print(item.id, item.display_name)


if __name__ == "__main__":
    main()
```
