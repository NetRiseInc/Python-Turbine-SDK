<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# mutation_update_sso_connection

[Back to the index](../README.md)

Update settings on a draft or disabled SSO connection.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |
| `update_sso_connection_args` | `UpdateSsoConnectionInput` | `true` |

## Response fields

Typed attributes on the response model.

| Field | Type | Nullable |
| --- | --- | --- |
| `updateSsoConnection` | `object` | no |
| `updateSsoConnection.connection` | `object` | yes |
| `updateSsoConnection.connection.acsUrl` | `string` | yes |
| `updateSsoConnection.connection.allowedActions[]` | `SsoAction` | no |
| `updateSsoConnection.connection.certExpiry` | `string` | yes |
| `updateSsoConnection.connection.certFingerprint` | `string` | yes |
| `updateSsoConnection.connection.certSubject` | `string` | yes |
| `updateSsoConnection.connection.connectionId` | `string` | no |
| `updateSsoConnection.connection.connectionName` | `string` | no |
| `updateSsoConnection.connection.connectionType` | `SsoConnectionType` | no |
| `updateSsoConnection.connection.emailClaim` | `string` | yes |
| `updateSsoConnection.connection.encryptionCertificatePem` | `string` | yes |
| `updateSsoConnection.connection.etag` | `string` | yes |
| `updateSsoConnection.connection.groupKeyType` | `SsoGroupKeyType` | no |
| `updateSsoConnection.connection.groupMappings[]` | `object` | no |
| `updateSsoConnection.connection.groupMappings[].createdAt` | `string` | yes |
| `updateSsoConnection.connection.groupMappings[].idpGroupKey` | `string` | yes |
| `updateSsoConnection.connection.groupMappings[].idpGroupLabel` | `string` | yes |
| `updateSsoConnection.connection.groupMappings[].lastSyncedAt` | `string` | yes |
| `updateSsoConnection.connection.groupMappings[].mappingId` | `string` | no |
| `updateSsoConnection.connection.groupMappings[].memberCount` | `integer` | yes |
| `updateSsoConnection.connection.groupMappings[].ruleType` | `SsoGroupRuleType` | no |
| `updateSsoConnection.connection.groupMappings[].securityGroupId` | `string` | yes |
| `updateSsoConnection.connection.groupMappings[].securityGroupName` | `string` | yes |
| `updateSsoConnection.connection.groupsClaim` | `string` | yes |
| `updateSsoConnection.connection.identityProvider` | `SsoIdentityProvider` | no |
| `updateSsoConnection.connection.idpIdentifier` | `string` | yes |
| `updateSsoConnection.connection.idpSignInUrl` | `string` | yes |
| `updateSsoConnection.connection.idpSignOutUrl` | `string` | yes |
| `updateSsoConnection.connection.issues[]` | `SsoConnectionIssue` | no |
| `updateSsoConnection.connection.loginButtonLabel` | `string` | yes |
| `updateSsoConnection.connection.loginButtonLogoUrl` | `string` | yes |
| `updateSsoConnection.connection.metadataAvailable` | `boolean` | no |
| `updateSsoConnection.connection.nameClaim` | `string` | yes |
| `updateSsoConnection.connection.orgId` | `string` | no |
| `updateSsoConnection.connection.resettableFields[]` | `SsoResetField` | no |
| `updateSsoConnection.connection.spEntityId` | `string` | yes |
| `updateSsoConnection.connection.spMetadataUrl` | `string` | yes |
| `updateSsoConnection.connection.status` | `SsoConnectionStatus` | no |
| `updateSsoConnection.connection.statusDetail` | `string` | yes |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    UpdateSsoConnectionInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.mutation_update_sso_connection(update_sso_connection_args=UpdateSsoConnectionInput(etag='value'))
        # Responses are typed Pydantic models: read fields as attributes.
        print(resp.update_sso_connection.connection.status)


if __name__ == "__main__":
    main()
```
