<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# mutation_create_sso_connection

[Back to the index](../README.md)

Create the org's SSO connection as an inactive draft.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |
| `create_sso_connection_args` | `CreateSsoConnectionInput` | `true` |

## Response fields

Typed attributes on the response model.

| Field | Type | Nullable |
| --- | --- | --- |
| `createSsoConnection` | `object` | no |
| `createSsoConnection.connection` | `object` | yes |
| `createSsoConnection.connection.acsUrl` | `string` | yes |
| `createSsoConnection.connection.allowedActions[]` | `SsoAction` | no |
| `createSsoConnection.connection.certExpiry` | `string` | yes |
| `createSsoConnection.connection.certFingerprint` | `string` | yes |
| `createSsoConnection.connection.certSubject` | `string` | yes |
| `createSsoConnection.connection.connectionId` | `string` | no |
| `createSsoConnection.connection.connectionName` | `string` | no |
| `createSsoConnection.connection.connectionType` | `SsoConnectionType` | no |
| `createSsoConnection.connection.emailClaim` | `string` | yes |
| `createSsoConnection.connection.encryptionCertificatePem` | `string` | yes |
| `createSsoConnection.connection.etag` | `string` | yes |
| `createSsoConnection.connection.groupKeyType` | `SsoGroupKeyType` | no |
| `createSsoConnection.connection.groupMappings[]` | `object` | no |
| `createSsoConnection.connection.groupMappings[].createdAt` | `string` | yes |
| `createSsoConnection.connection.groupMappings[].idpGroupKey` | `string` | yes |
| `createSsoConnection.connection.groupMappings[].idpGroupLabel` | `string` | yes |
| `createSsoConnection.connection.groupMappings[].lastSyncedAt` | `string` | yes |
| `createSsoConnection.connection.groupMappings[].mappingId` | `string` | no |
| `createSsoConnection.connection.groupMappings[].memberCount` | `integer` | yes |
| `createSsoConnection.connection.groupMappings[].ruleType` | `SsoGroupRuleType` | no |
| `createSsoConnection.connection.groupMappings[].securityGroupId` | `string` | yes |
| `createSsoConnection.connection.groupMappings[].securityGroupName` | `string` | yes |
| `createSsoConnection.connection.groupsClaim` | `string` | yes |
| `createSsoConnection.connection.identityProvider` | `SsoIdentityProvider` | no |
| `createSsoConnection.connection.idpIdentifier` | `string` | yes |
| `createSsoConnection.connection.idpSignInUrl` | `string` | yes |
| `createSsoConnection.connection.idpSignOutUrl` | `string` | yes |
| `createSsoConnection.connection.issues[]` | `SsoConnectionIssue` | no |
| `createSsoConnection.connection.loginButtonLabel` | `string` | yes |
| `createSsoConnection.connection.loginButtonLogoUrl` | `string` | yes |
| `createSsoConnection.connection.metadataAvailable` | `boolean` | no |
| `createSsoConnection.connection.nameClaim` | `string` | yes |
| `createSsoConnection.connection.orgId` | `string` | no |
| `createSsoConnection.connection.resettableFields[]` | `SsoResetField` | no |
| `createSsoConnection.connection.spEntityId` | `string` | yes |
| `createSsoConnection.connection.spMetadataUrl` | `string` | yes |
| `createSsoConnection.connection.status` | `SsoConnectionStatus` | no |
| `createSsoConnection.connection.statusDetail` | `string` | yes |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    CreateSsoConnectionInput,
)
from netrise_turbine_sdk_graphql.enums import (
    SsoConnectionType,
    SsoIdentityProvider,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.mutation_create_sso_connection(create_sso_connection_args=CreateSsoConnectionInput(connection_type=SsoConnectionType.UNSPECIFIED, identity_provider=SsoIdentityProvider.UNSPECIFIED))
        # Responses are typed Pydantic models: read fields as attributes.
        print(resp.create_sso_connection.connection.status)


if __name__ == "__main__":
    main()
```
