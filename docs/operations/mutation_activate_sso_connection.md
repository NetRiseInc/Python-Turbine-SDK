<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# mutation_activate_sso_connection

[Back to the index](../README.md)

Put a tested draft SSO connection into service.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |
| `activate_sso_connection_args` | `ActivateSsoConnectionInput` | `true` |

## Response fields

Typed attributes on the response model.

| Field | Type | Nullable |
| --- | --- | --- |
| `activateSsoConnection` | `object` | no |
| `activateSsoConnection.connection` | `object` | yes |
| `activateSsoConnection.connection.acsUrl` | `string` | yes |
| `activateSsoConnection.connection.allowedActions[]` | `SsoAction` | no |
| `activateSsoConnection.connection.certExpiry` | `string` | yes |
| `activateSsoConnection.connection.certFingerprint` | `string` | yes |
| `activateSsoConnection.connection.certSubject` | `string` | yes |
| `activateSsoConnection.connection.connectionId` | `string` | no |
| `activateSsoConnection.connection.connectionName` | `string` | no |
| `activateSsoConnection.connection.connectionType` | `SsoConnectionType` | no |
| `activateSsoConnection.connection.emailClaim` | `string` | yes |
| `activateSsoConnection.connection.encryptionCertificatePem` | `string` | yes |
| `activateSsoConnection.connection.etag` | `string` | yes |
| `activateSsoConnection.connection.groupKeyType` | `SsoGroupKeyType` | no |
| `activateSsoConnection.connection.groupMappings[]` | `object` | no |
| `activateSsoConnection.connection.groupMappings[].createdAt` | `string` | yes |
| `activateSsoConnection.connection.groupMappings[].idpGroupKey` | `string` | yes |
| `activateSsoConnection.connection.groupMappings[].idpGroupLabel` | `string` | yes |
| `activateSsoConnection.connection.groupMappings[].lastSyncedAt` | `string` | yes |
| `activateSsoConnection.connection.groupMappings[].mappingId` | `string` | no |
| `activateSsoConnection.connection.groupMappings[].memberCount` | `integer` | yes |
| `activateSsoConnection.connection.groupMappings[].ruleType` | `SsoGroupRuleType` | no |
| `activateSsoConnection.connection.groupMappings[].securityGroupId` | `string` | yes |
| `activateSsoConnection.connection.groupMappings[].securityGroupName` | `string` | yes |
| `activateSsoConnection.connection.groupsClaim` | `string` | yes |
| `activateSsoConnection.connection.identityProvider` | `SsoIdentityProvider` | no |
| `activateSsoConnection.connection.idpIdentifier` | `string` | yes |
| `activateSsoConnection.connection.idpSignInUrl` | `string` | yes |
| `activateSsoConnection.connection.idpSignOutUrl` | `string` | yes |
| `activateSsoConnection.connection.issues[]` | `SsoConnectionIssue` | no |
| `activateSsoConnection.connection.loginButtonLabel` | `string` | yes |
| `activateSsoConnection.connection.loginButtonLogoUrl` | `string` | yes |
| `activateSsoConnection.connection.metadataAvailable` | `boolean` | no |
| `activateSsoConnection.connection.nameClaim` | `string` | yes |
| `activateSsoConnection.connection.orgId` | `string` | no |
| `activateSsoConnection.connection.resettableFields[]` | `SsoResetField` | no |
| `activateSsoConnection.connection.spEntityId` | `string` | yes |
| `activateSsoConnection.connection.spMetadataUrl` | `string` | yes |
| `activateSsoConnection.connection.status` | `SsoConnectionStatus` | no |
| `activateSsoConnection.connection.statusDetail` | `string` | yes |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    ActivateSsoConnectionInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.mutation_activate_sso_connection(activate_sso_connection_args=ActivateSsoConnectionInput())
        # Responses are typed Pydantic models: read fields as attributes.
        print(resp.activate_sso_connection.connection.status)


if __name__ == "__main__":
    main()
```
