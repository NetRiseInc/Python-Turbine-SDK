<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# query_get_sso_connection

[Back to the index](../README.md)

Get the org's SSO connection, or null if none exists.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |
| `get_sso_connection_connection_id` | `Union[str, None, UnsetType]` | `false` |

## Response fields

Typed attributes on the response model.

| Field | Type | Nullable |
| --- | --- | --- |
| `getSsoConnection` | `object` | yes |
| `getSsoConnection.acsUrl` | `string` | yes |
| `getSsoConnection.allowedActions[]` | `SsoAction` | no |
| `getSsoConnection.certExpiry` | `string` | yes |
| `getSsoConnection.certFingerprint` | `string` | yes |
| `getSsoConnection.certSubject` | `string` | yes |
| `getSsoConnection.connectionId` | `string` | no |
| `getSsoConnection.connectionName` | `string` | no |
| `getSsoConnection.connectionType` | `SsoConnectionType` | no |
| `getSsoConnection.emailClaim` | `string` | yes |
| `getSsoConnection.encryptionCertificatePem` | `string` | yes |
| `getSsoConnection.etag` | `string` | yes |
| `getSsoConnection.groupKeyType` | `SsoGroupKeyType` | no |
| `getSsoConnection.groupMappings[]` | `object` | no |
| `getSsoConnection.groupMappings[].createdAt` | `string` | yes |
| `getSsoConnection.groupMappings[].idpGroupKey` | `string` | yes |
| `getSsoConnection.groupMappings[].idpGroupLabel` | `string` | yes |
| `getSsoConnection.groupMappings[].lastSyncedAt` | `string` | yes |
| `getSsoConnection.groupMappings[].mappingId` | `string` | no |
| `getSsoConnection.groupMappings[].memberCount` | `integer` | yes |
| `getSsoConnection.groupMappings[].ruleType` | `SsoGroupRuleType` | no |
| `getSsoConnection.groupMappings[].securityGroupId` | `string` | yes |
| `getSsoConnection.groupMappings[].securityGroupName` | `string` | yes |
| `getSsoConnection.groupsClaim` | `string` | yes |
| `getSsoConnection.identityProvider` | `SsoIdentityProvider` | no |
| `getSsoConnection.idpIdentifier` | `string` | yes |
| `getSsoConnection.idpSignInUrl` | `string` | yes |
| `getSsoConnection.idpSignOutUrl` | `string` | yes |
| `getSsoConnection.issues[]` | `SsoConnectionIssue` | no |
| `getSsoConnection.loginButtonLabel` | `string` | yes |
| `getSsoConnection.loginButtonLogoUrl` | `string` | yes |
| `getSsoConnection.metadataAvailable` | `boolean` | no |
| `getSsoConnection.nameClaim` | `string` | yes |
| `getSsoConnection.orgId` | `string` | no |
| `getSsoConnection.resettableFields[]` | `SsoResetField` | no |
| `getSsoConnection.spEntityId` | `string` | yes |
| `getSsoConnection.spMetadataUrl` | `string` | yes |
| `getSsoConnection.status` | `SsoConnectionStatus` | no |
| `getSsoConnection.statusDetail` | `string` | yes |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_get_sso_connection()
        # Responses are typed Pydantic models: read fields as attributes.
        print(resp.get_sso_connection.status)


if __name__ == "__main__":
    main()
```
