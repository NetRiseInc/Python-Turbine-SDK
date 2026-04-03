<!-- Generated file: do not edit by hand -->

# query_org_level_information

Retrieve organization-level metadata such as last-updated time, optionally scoped by asset groups.

## Parameters

| name | type | required |
| --- | --- | --- |
| `org_level_information_args` | `OrgLevelInformationInput` | `true` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `orgLevelInformation` | `object` | no |
| `orgLevelInformation.lastUpdatedAt` | `typing.Annotated[datetime.datetime, BeforeValidator(func=<function parse_datetime at 0x1093f3060>, json_schema_input_type=PydanticUndefined)]` | yes |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    OrgLevelInformationInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_org_level_information(org_level_information_args=OrgLevelInformationInput())
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
