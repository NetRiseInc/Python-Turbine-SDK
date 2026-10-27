<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# mutation_disable_sso_connection

[Back to the index](../README.md)

Stop new SSO logins; existing sessions stay active.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |
| `disable_sso_connection_args` | `DisableSsoConnectionInput` | `true` |

## Response fields

Typed attributes on the response model.

| Field | Type | Nullable |
| --- | --- | --- |
| `disableSsoConnection` | `object` | no |
| `disableSsoConnection.connection` | `object` | yes |
| `disableSsoConnection.connection.acsUrl` | `string` | yes |
| `disableSsoConnection.connection.allowedActions[]` | `SsoAction` | no |
| `disableSsoConnection.connection.certExpiry` | `string` | yes |
| `disableSsoConnection.connection.certFingerprint` | `string` | yes |
| `disableSsoConnection.connection.certSubject` | `string` | yes |
| `disableSsoConnection.connection.connectionId` | `string` | no |
| `disableSsoConnection.connection.connectionName` | `string` | no |
| `disableSsoConnection.connection.connectionType` | `SsoConnectionType` | no |
| `disableSsoConnection.connection.emailClaim` | `string` | yes |
| `disableSsoConnection.connection.encryptionCertificatePem` | `string` | yes |
| `disableSsoConnection.connection.etag` | `string` | yes |
| `disableSsoConnection.connection.groupKeyType` | `SsoGroupKeyType` | no |
| `disableSsoConnection.connection.groupMappings[]` | `object` | no |
| `disableSsoConnection.connection.groupMappings[].createdAt` | `string` | yes |
| `disableSsoConnection.connection.groupMappings[].idpGroupKey` | `string` | yes |
| `disableSsoConnection.connection.groupMappings[].idpGroupLabel` | `string` | yes |
| `disableSsoConnection.connection.groupMappings[].lastSyncedAt` | `string` | yes |
| `disableSsoConnection.connection.groupMappings[].mappingId` | `string` | no |
| `disableSsoConnection.connection.groupMappings[].memberCount` | `integer` | yes |
| `disableSsoConnection.connection.groupMappings[].ruleType` | `SsoGroupRuleType` | no |
| `disableSsoConnection.connection.groupMappings[].securityGroupId` | `string` | yes |
| `disableSsoConnection.connection.groupMappings[].securityGroupName` | `string` | yes |
| `disableSsoConnection.connection.groupsClaim` | `string` | yes |
| `disableSsoConnection.connection.identityProvider` | `SsoIdentityProvider` | no |
| `disableSsoConnection.connection.idpIdentifier` | `string` | yes |
| `disableSsoConnection.connection.idpSignInUrl` | `string` | yes |
| `disableSsoConnection.connection.idpSignOutUrl` | `string` | yes |
| `disableSsoConnection.connection.issues[]` | `SsoConnectionIssue` | no |
| `disableSsoConnection.connection.loginButtonLabel` | `string` | yes |
| `disableSsoConnection.connection.loginButtonLogoUrl` | `string` | yes |
| `disableSsoConnection.connection.metadataAvailable` | `boolean` | no |
| `disableSsoConnection.connection.nameClaim` | `string` | yes |
| `disableSsoConnection.connection.orgId` | `string` | no |
| `disableSsoConnection.connection.resettableFields[]` | `SsoResetField` | no |
| `disableSsoConnection.connection.spEntityId` | `string` | yes |
| `disableSsoConnection.connection.spMetadataUrl` | `string` | yes |
| `disableSsoConnection.connection.status` | `SsoConnectionStatus` | no |
| `disableSsoConnection.connection.statusDetail` | `string` | yes |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    DisableSsoConnectionInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.mutation_disable_sso_connection(disable_sso_connection_args=DisableSsoConnectionInput())
        # Responses are typed Pydantic models: read fields as attributes.
        print(resp.disable_sso_connection.connection.status)


if __name__ == "__main__":
    main()
```
