<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# mutation_enable_sso_connection

[Back to the index](../README.md)

Resume logins through an active SSO connection.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |
| `enable_sso_connection_args` | `EnableSsoConnectionInput` | `true` |

## Response fields

Typed attributes on the response model.

| Field | Type | Nullable |
| --- | --- | --- |
| `enableSsoConnection` | `object` | no |
| `enableSsoConnection.connection` | `object` | yes |
| `enableSsoConnection.connection.acsUrl` | `string` | yes |
| `enableSsoConnection.connection.allowedActions[]` | `SsoAction` | no |
| `enableSsoConnection.connection.certExpiry` | `string` | yes |
| `enableSsoConnection.connection.certFingerprint` | `string` | yes |
| `enableSsoConnection.connection.certSubject` | `string` | yes |
| `enableSsoConnection.connection.connectionId` | `string` | no |
| `enableSsoConnection.connection.connectionName` | `string` | no |
| `enableSsoConnection.connection.connectionType` | `SsoConnectionType` | no |
| `enableSsoConnection.connection.emailClaim` | `string` | yes |
| `enableSsoConnection.connection.encryptionCertificatePem` | `string` | yes |
| `enableSsoConnection.connection.etag` | `string` | yes |
| `enableSsoConnection.connection.groupKeyType` | `SsoGroupKeyType` | no |
| `enableSsoConnection.connection.groupMappings[]` | `object` | no |
| `enableSsoConnection.connection.groupMappings[].createdAt` | `string` | yes |
| `enableSsoConnection.connection.groupMappings[].idpGroupKey` | `string` | yes |
| `enableSsoConnection.connection.groupMappings[].idpGroupLabel` | `string` | yes |
| `enableSsoConnection.connection.groupMappings[].lastSyncedAt` | `string` | yes |
| `enableSsoConnection.connection.groupMappings[].mappingId` | `string` | no |
| `enableSsoConnection.connection.groupMappings[].memberCount` | `integer` | yes |
| `enableSsoConnection.connection.groupMappings[].ruleType` | `SsoGroupRuleType` | no |
| `enableSsoConnection.connection.groupMappings[].securityGroupId` | `string` | yes |
| `enableSsoConnection.connection.groupMappings[].securityGroupName` | `string` | yes |
| `enableSsoConnection.connection.groupsClaim` | `string` | yes |
| `enableSsoConnection.connection.identityProvider` | `SsoIdentityProvider` | no |
| `enableSsoConnection.connection.idpIdentifier` | `string` | yes |
| `enableSsoConnection.connection.idpSignInUrl` | `string` | yes |
| `enableSsoConnection.connection.idpSignOutUrl` | `string` | yes |
| `enableSsoConnection.connection.issues[]` | `SsoConnectionIssue` | no |
| `enableSsoConnection.connection.loginButtonLabel` | `string` | yes |
| `enableSsoConnection.connection.loginButtonLogoUrl` | `string` | yes |
| `enableSsoConnection.connection.metadataAvailable` | `boolean` | no |
| `enableSsoConnection.connection.nameClaim` | `string` | yes |
| `enableSsoConnection.connection.orgId` | `string` | no |
| `enableSsoConnection.connection.resettableFields[]` | `SsoResetField` | no |
| `enableSsoConnection.connection.spEntityId` | `string` | yes |
| `enableSsoConnection.connection.spMetadataUrl` | `string` | yes |
| `enableSsoConnection.connection.status` | `SsoConnectionStatus` | no |
| `enableSsoConnection.connection.statusDetail` | `string` | yes |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    EnableSsoConnectionInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.mutation_enable_sso_connection(enable_sso_connection_args=EnableSsoConnectionInput())
        # Responses are typed Pydantic models: read fields as attributes.
        print(resp.enable_sso_connection.connection.status)


if __name__ == "__main__":
    main()
```
