<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# query_org_level_information

[Back to the index](../README.md)

Get org metadata such as last-updated time.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |
| `org_level_information_args` | `OrgLevelInformationInput` | `true` |

## Response fields

Typed attributes on the response model.

| Field | Type | Nullable |
| --- | --- | --- |
| `orgLevelInformation` | `object` | no |
| `orgLevelInformation.lastUpdatedAt` | `typing.Annotated[datetime.datetime, BeforeValidator(func=<function parse_datetime at 0x1090c2660>, json_schema_input_type=PydanticUndefined)]` | yes |

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
        # Responses are typed Pydantic models: read fields as attributes.
        print(resp.org_level_information.last_updated_at)


if __name__ == "__main__":
    main()
```
