<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# query_get_sso_connection_test

[Back to the index](../README.md)

Get an SSO login test's status, claims, or failure.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |
| `get_sso_connection_test_test_id` | `str` | `true` |

## Response fields

Typed attributes on the response model.

| Field | Type | Nullable |
| --- | --- | --- |
| `getSsoConnectionTest` | `object` | yes |
| `getSsoConnectionTest.createdAt` | `string` | yes |
| `getSsoConnectionTest.expiresAt` | `string` | yes |
| `getSsoConnectionTest.failure` | `typing.Annotated[typing.Union[netrise_turbine_sdk_graphql.query_get_sso_connection_test.QueryGetSsoConnectionTestGetSsoConnectionTestFailureSsoTestNetworkFailure, netrise_turbine_sdk_graphql.query_get_sso_connection_test.QueryGetSsoConnectionTestGetSsoConnectionTestFailureSsoTestIdpError, netrise_turbine_sdk_graphql.query_get_sso_connection_test.QueryGetSsoConnectionTestGetSsoConnectionTestFailureSsoTestMissingRequiredClaims], FieldInfo(annotation=NoneType, required=True, discriminator='typename__')]` | yes |
| `getSsoConnectionTest.initiatedBy` | `string` | yes |
| `getSsoConnectionTest.observedClaims[]` | `object` | no |
| `getSsoConnectionTest.observedClaims[].name` | `string` | no |
| `getSsoConnectionTest.observedClaims[].values[]` | `string` | no |
| `getSsoConnectionTest.state` | `SsoTestState` | no |
| `getSsoConnectionTest.testId` | `string` | no |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_get_sso_connection_test(get_sso_connection_test_test_id='id_123')
        # Responses are typed Pydantic models: read fields as attributes.
        for item in resp.get_sso_connection_test.observed_claims or []:
            print(item.name)


if __name__ == "__main__":
    main()
```
