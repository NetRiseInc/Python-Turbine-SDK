<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# mutation_select_sso_identity_provider

[Back to the index](../README.md)

Choose the identity provider for the SSO connection.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |
| `select_sso_identity_provider_args` | `SelectSsoIdentityProviderInput` | `true` |

## Response fields

Typed attributes on the response model.

| Field | Type | Nullable |
| --- | --- | --- |
| `selectSsoIdentityProvider` | `object` | no |
| `selectSsoIdentityProvider.change` | `object` | yes |
| `selectSsoIdentityProvider.change.claimDefaultsApplied` | `boolean` | no |
| `selectSsoIdentityProvider.change.clearedFields[]` | `SsoResetField` | no |
| `selectSsoIdentityProvider.change.mappingsDropped` | `integer` | no |
| `selectSsoIdentityProvider.change.providerChanged` | `boolean` | no |
| `selectSsoIdentityProvider.connection` | `object` | yes |
| `selectSsoIdentityProvider.connection.acsUrl` | `string` | yes |
| `selectSsoIdentityProvider.connection.allowedActions[]` | `SsoAction` | no |
| `selectSsoIdentityProvider.connection.certExpiry` | `string` | yes |
| `selectSsoIdentityProvider.connection.certFingerprint` | `string` | yes |
| `selectSsoIdentityProvider.connection.certSubject` | `string` | yes |
| `selectSsoIdentityProvider.connection.connectionId` | `string` | no |
| `selectSsoIdentityProvider.connection.connectionName` | `string` | no |
| `selectSsoIdentityProvider.connection.connectionType` | `SsoConnectionType` | no |
| `selectSsoIdentityProvider.connection.emailClaim` | `string` | yes |
| `selectSsoIdentityProvider.connection.encryptionCertificatePem` | `string` | yes |
| `selectSsoIdentityProvider.connection.etag` | `string` | yes |
| `selectSsoIdentityProvider.connection.groupKeyType` | `SsoGroupKeyType` | no |
| `selectSsoIdentityProvider.connection.groupMappings[]` | `object` | no |
| `selectSsoIdentityProvider.connection.groupMappings[].createdAt` | `string` | yes |
| `selectSsoIdentityProvider.connection.groupMappings[].idpGroupKey` | `string` | yes |
| `selectSsoIdentityProvider.connection.groupMappings[].idpGroupLabel` | `string` | yes |
| `selectSsoIdentityProvider.connection.groupMappings[].lastSyncedAt` | `string` | yes |
| `selectSsoIdentityProvider.connection.groupMappings[].mappingId` | `string` | no |
| `selectSsoIdentityProvider.connection.groupMappings[].memberCount` | `integer` | yes |
| `selectSsoIdentityProvider.connection.groupMappings[].ruleType` | `SsoGroupRuleType` | no |
| `selectSsoIdentityProvider.connection.groupMappings[].securityGroupId` | `string` | yes |
| `selectSsoIdentityProvider.connection.groupMappings[].securityGroupName` | `string` | yes |
| `selectSsoIdentityProvider.connection.groupsClaim` | `string` | yes |
| `selectSsoIdentityProvider.connection.identityProvider` | `SsoIdentityProvider` | no |
| `selectSsoIdentityProvider.connection.idpIdentifier` | `string` | yes |
| `selectSsoIdentityProvider.connection.idpSignInUrl` | `string` | yes |
| `selectSsoIdentityProvider.connection.idpSignOutUrl` | `string` | yes |
| `selectSsoIdentityProvider.connection.issues[]` | `SsoConnectionIssue` | no |
| `selectSsoIdentityProvider.connection.loginButtonLabel` | `string` | yes |
| `selectSsoIdentityProvider.connection.loginButtonLogoUrl` | `string` | yes |
| `selectSsoIdentityProvider.connection.metadataAvailable` | `boolean` | no |
| `selectSsoIdentityProvider.connection.nameClaim` | `string` | yes |
| `selectSsoIdentityProvider.connection.orgId` | `string` | no |
| `selectSsoIdentityProvider.connection.resettableFields[]` | `SsoResetField` | no |
| `selectSsoIdentityProvider.connection.spEntityId` | `string` | yes |
| `selectSsoIdentityProvider.connection.spMetadataUrl` | `string` | yes |
| `selectSsoIdentityProvider.connection.status` | `SsoConnectionStatus` | no |
| `selectSsoIdentityProvider.connection.statusDetail` | `string` | yes |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    SelectSsoIdentityProviderInput,
)
from netrise_turbine_sdk_graphql.enums import (
    SsoConnectionType,
    SsoIdentityProvider,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.mutation_select_sso_identity_provider(select_sso_identity_provider_args=SelectSsoIdentityProviderInput(connection_type=SsoConnectionType.UNSPECIFIED, identity_provider=SsoIdentityProvider.UNSPECIFIED))
        # Responses are typed Pydantic models: read fields as attributes.
        print(resp.select_sso_identity_provider.connection.status)


if __name__ == "__main__":
    main()
```
