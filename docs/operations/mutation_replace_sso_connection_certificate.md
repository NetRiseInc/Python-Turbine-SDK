<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# mutation_replace_sso_connection_certificate

[Back to the index](../README.md)

Replace the SSO connection's signing certificate.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |
| `replace_sso_connection_certificate_args` | `ReplaceSsoConnectionCertificateInput` | `true` |

## Response fields

Typed attributes on the response model.

| Field | Type | Nullable |
| --- | --- | --- |
| `replaceSsoConnectionCertificate` | `object` | no |
| `replaceSsoConnectionCertificate.connection` | `object` | yes |
| `replaceSsoConnectionCertificate.connection.acsUrl` | `string` | yes |
| `replaceSsoConnectionCertificate.connection.allowedActions[]` | `SsoAction` | no |
| `replaceSsoConnectionCertificate.connection.certExpiry` | `string` | yes |
| `replaceSsoConnectionCertificate.connection.certFingerprint` | `string` | yes |
| `replaceSsoConnectionCertificate.connection.certSubject` | `string` | yes |
| `replaceSsoConnectionCertificate.connection.connectionId` | `string` | no |
| `replaceSsoConnectionCertificate.connection.connectionName` | `string` | no |
| `replaceSsoConnectionCertificate.connection.connectionType` | `SsoConnectionType` | no |
| `replaceSsoConnectionCertificate.connection.emailClaim` | `string` | yes |
| `replaceSsoConnectionCertificate.connection.encryptionCertificatePem` | `string` | yes |
| `replaceSsoConnectionCertificate.connection.etag` | `string` | yes |
| `replaceSsoConnectionCertificate.connection.groupKeyType` | `SsoGroupKeyType` | no |
| `replaceSsoConnectionCertificate.connection.groupMappings[]` | `object` | no |
| `replaceSsoConnectionCertificate.connection.groupMappings[].createdAt` | `string` | yes |
| `replaceSsoConnectionCertificate.connection.groupMappings[].idpGroupKey` | `string` | yes |
| `replaceSsoConnectionCertificate.connection.groupMappings[].idpGroupLabel` | `string` | yes |
| `replaceSsoConnectionCertificate.connection.groupMappings[].lastSyncedAt` | `string` | yes |
| `replaceSsoConnectionCertificate.connection.groupMappings[].mappingId` | `string` | no |
| `replaceSsoConnectionCertificate.connection.groupMappings[].memberCount` | `integer` | yes |
| `replaceSsoConnectionCertificate.connection.groupMappings[].ruleType` | `SsoGroupRuleType` | no |
| `replaceSsoConnectionCertificate.connection.groupMappings[].securityGroupId` | `string` | yes |
| `replaceSsoConnectionCertificate.connection.groupMappings[].securityGroupName` | `string` | yes |
| `replaceSsoConnectionCertificate.connection.groupsClaim` | `string` | yes |
| `replaceSsoConnectionCertificate.connection.identityProvider` | `SsoIdentityProvider` | no |
| `replaceSsoConnectionCertificate.connection.idpIdentifier` | `string` | yes |
| `replaceSsoConnectionCertificate.connection.idpSignInUrl` | `string` | yes |
| `replaceSsoConnectionCertificate.connection.idpSignOutUrl` | `string` | yes |
| `replaceSsoConnectionCertificate.connection.issues[]` | `SsoConnectionIssue` | no |
| `replaceSsoConnectionCertificate.connection.loginButtonLabel` | `string` | yes |
| `replaceSsoConnectionCertificate.connection.loginButtonLogoUrl` | `string` | yes |
| `replaceSsoConnectionCertificate.connection.metadataAvailable` | `boolean` | no |
| `replaceSsoConnectionCertificate.connection.nameClaim` | `string` | yes |
| `replaceSsoConnectionCertificate.connection.orgId` | `string` | no |
| `replaceSsoConnectionCertificate.connection.resettableFields[]` | `SsoResetField` | no |
| `replaceSsoConnectionCertificate.connection.spEntityId` | `string` | yes |
| `replaceSsoConnectionCertificate.connection.spMetadataUrl` | `string` | yes |
| `replaceSsoConnectionCertificate.connection.status` | `SsoConnectionStatus` | no |
| `replaceSsoConnectionCertificate.connection.statusDetail` | `string` | yes |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    ReplaceSsoConnectionCertificateInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.mutation_replace_sso_connection_certificate(replace_sso_connection_certificate_args=ReplaceSsoConnectionCertificateInput(etag='value', signing_certificate_pem='value'))
        # Responses are typed Pydantic models: read fields as attributes.
        print(resp.replace_sso_connection_certificate.connection.status)


if __name__ == "__main__":
    main()
```
