<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# query_get_sso_activation_readiness

[Back to the index](../README.md)

Check whether the SSO connection can be activated.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |
| `get_sso_activation_readiness_connection_id` | `Union[str, None, UnsetType]` | `false` |

## Response fields

Typed attributes on the response model.

| Field | Type | Nullable |
| --- | --- | --- |
| `getSsoActivationReadiness` | `object` | no |
| `getSsoActivationReadiness.blockers[]` | `object` | no |
| `getSsoActivationReadiness.blockers[].message` | `string` | yes |
| `getSsoActivationReadiness.blockers[].reason` | `SsoReadinessBlockerReason` | no |
| `getSsoActivationReadiness.ready` | `boolean` | no |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_get_sso_activation_readiness()
        # Responses are typed Pydantic models: read fields as attributes.
        for item in resp.get_sso_activation_readiness.blockers or []:
            print(item.message, item.reason)


if __name__ == "__main__":
    main()
```
