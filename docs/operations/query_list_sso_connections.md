<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# query_list_sso_connections

[Back to the index](../README.md)

List the org's SSO connections, including drafts.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |

## Response fields

Typed attributes on the response model.

| Field | Type | Nullable |
| --- | --- | --- |
| `listSsoConnections` | `object` | no |
| `listSsoConnections.connections[]` | `object` | no |
| `listSsoConnections.connections[].acsUrl` | `string` | yes |
| `listSsoConnections.connections[].allowedActions[]` | `SsoAction` | no |
| `listSsoConnections.connections[].certExpiry` | `string` | yes |
| `listSsoConnections.connections[].certFingerprint` | `string` | yes |
| `listSsoConnections.connections[].certSubject` | `string` | yes |
| `listSsoConnections.connections[].connectionId` | `string` | no |
| `listSsoConnections.connections[].connectionName` | `string` | no |
| `listSsoConnections.connections[].connectionType` | `SsoConnectionType` | no |
| `listSsoConnections.connections[].emailClaim` | `string` | yes |
| `listSsoConnections.connections[].encryptionCertificatePem` | `string` | yes |
| `listSsoConnections.connections[].etag` | `string` | yes |
| `listSsoConnections.connections[].groupKeyType` | `SsoGroupKeyType` | no |
| `listSsoConnections.connections[].groupMappings[]` | `object` | no |
| `listSsoConnections.connections[].groupMappings[].createdAt` | `string` | yes |
| `listSsoConnections.connections[].groupMappings[].idpGroupKey` | `string` | yes |
| `listSsoConnections.connections[].groupMappings[].idpGroupLabel` | `string` | yes |
| `listSsoConnections.connections[].groupMappings[].lastSyncedAt` | `string` | yes |
| `listSsoConnections.connections[].groupMappings[].mappingId` | `string` | no |
| `listSsoConnections.connections[].groupMappings[].memberCount` | `integer` | yes |
| `listSsoConnections.connections[].groupMappings[].ruleType` | `SsoGroupRuleType` | no |
| `listSsoConnections.connections[].groupMappings[].securityGroupId` | `string` | yes |
| `listSsoConnections.connections[].groupMappings[].securityGroupName` | `string` | yes |
| `listSsoConnections.connections[].groupsClaim` | `string` | yes |
| `listSsoConnections.connections[].identityProvider` | `SsoIdentityProvider` | no |
| `listSsoConnections.connections[].idpIdentifier` | `string` | yes |
| `listSsoConnections.connections[].idpSignInUrl` | `string` | yes |
| `listSsoConnections.connections[].idpSignOutUrl` | `string` | yes |
| `listSsoConnections.connections[].issues[]` | `SsoConnectionIssue` | no |
| `listSsoConnections.connections[].loginButtonLabel` | `string` | yes |
| `listSsoConnections.connections[].loginButtonLogoUrl` | `string` | yes |
| `listSsoConnections.connections[].metadataAvailable` | `boolean` | no |
| `listSsoConnections.connections[].nameClaim` | `string` | yes |
| `listSsoConnections.connections[].orgId` | `string` | no |
| `listSsoConnections.connections[].resettableFields[]` | `SsoResetField` | no |
| `listSsoConnections.connections[].spEntityId` | `string` | yes |
| `listSsoConnections.connections[].spMetadataUrl` | `string` | yes |
| `listSsoConnections.connections[].status` | `SsoConnectionStatus` | no |
| `listSsoConnections.connections[].statusDetail` | `string` | yes |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_list_sso_connections()
        # Responses are typed Pydantic models: read fields as attributes.
        for item in resp.list_sso_connections.connections or []:
            print(item.status, item.acs_url, item.cert_expiry)


if __name__ == "__main__":
    main()
```
