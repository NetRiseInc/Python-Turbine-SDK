<!-- Generated file: do not edit by hand -->

# query_certificates

List X.509 certificates and validity status found in the asset.

## Parameters

| name | type | required |
| --- | --- | --- |
| `certificates_args` | `CertificatesInput` | `true` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `certificates` | `object` | yes |
| `certificates.edges[]` | `object` | yes |
| `certificates.edges[].cursor` | `string` | no |
| `certificates.edges[].node` | `object` | yes |
| `certificates.edges[].node.algorithmType` | `CryptoAlgorithmType` | yes |
| `certificates.edges[].node.altDnsNames[]` | `string` | yes |
| `certificates.edges[].node.altEmailAddresses[]` | `string` | yes |
| `certificates.edges[].node.altIps[]` | `string` | yes |
| `certificates.edges[].node.altUris[]` | `string` | yes |
| `certificates.edges[].node.basicConstraintsValid` | `boolean` | yes |
| `certificates.edges[].node.bitSize` | `string` | yes |
| `certificates.edges[].node.correlations[]` | `object` | yes |
| `certificates.edges[].node.correlations[].artifact` | `string` | yes |
| `certificates.edges[].node.correlations[].assetId` | `string` | yes |
| `certificates.edges[].node.correlations[].assetName` | `string` | yes |
| `certificates.edges[].node.correlations[].location` | `string` | yes |
| `certificates.edges[].node.correlations[].risk` | `object` | yes |
| `certificates.edges[].node.correlations[].risk.category` | `RiskCategory` | yes |
| `certificates.edges[].node.correlations[].risk.rawScore` | `float` | yes |
| `certificates.edges[].node.correlations[].risk.score` | `float` | yes |
| `certificates.edges[].node.correlations[].updatedAt` | `string` | yes |
| `certificates.edges[].node.correlationsCount` | `integer` | yes |
| `certificates.edges[].node.crlDistributionPoints[]` | `string` | yes |
| `certificates.edges[].node.currentRemediation` | `object` | yes |
| `certificates.edges[].node.currentRemediation.author` | `string` | yes |
| `certificates.edges[].node.currentRemediation.certificate` | `object` | no |
| `certificates.edges[].node.currentRemediation.certificate.filePath` | `string` | no |
| `certificates.edges[].node.currentRemediation.certificate.sha256` | `string` | no |
| `certificates.edges[].node.currentRemediation.createdAt` | `string` | yes |
| `certificates.edges[].node.currentRemediation.description` | `string` | yes |
| `certificates.edges[].node.currentRemediation.errorMessage` | `string` | yes |
| `certificates.edges[].node.currentRemediation.status` | `CryptoRemediationStatus` | no |
| `certificates.edges[].node.curve` | `string` | yes |
| `certificates.edges[].node.decapsulationKey` | `string` | yes |
| `certificates.edges[].node.e` | `string` | yes |
| `certificates.edges[].node.effectivePermissions` | `string` | yes |
| `certificates.edges[].node.encapsulationKey` | `string` | yes |
| `certificates.edges[].node.expireDate` | `string` | yes |
| `certificates.edges[].node.expired` | `boolean` | yes |
| `certificates.edges[].node.fileOffset` | `integer` | yes |
| `certificates.edges[].node.filePath` | `string` | yes |
| `certificates.edges[].node.invalid` | `boolean` | yes |
| `certificates.edges[].node.invalidities[]` | `string` | yes |
| `certificates.edges[].node.invaliditiesCount` | `integer` | no |
| `certificates.edges[].node.isCa` | `boolean` | yes |
| `certificates.edges[].node.issuerCommonName` | `string` | yes |
| `certificates.edges[].node.issuerCountry` | `string` | yes |
| `certificates.edges[].node.issuerDN` | `string` | yes |
| `certificates.edges[].node.issuerLocality` | `string` | yes |
| `certificates.edges[].node.issuerOrgUnit` | `string` | yes |
| `certificates.edges[].node.issuerOrganization` | `string` | yes |
| `certificates.edges[].node.issuerPostalCode` | `string` | yes |
| `certificates.edges[].node.issuerProvince` | `string` | yes |
| `certificates.edges[].node.issuerRdn` | `string` | yes |
| `certificates.edges[].node.issuerSerialNumber` | `string` | yes |
| `certificates.edges[].node.issuerStreetAddress` | `string` | yes |
| `certificates.edges[].node.issuingCertUrl` | `string` | yes |
| `certificates.edges[].node.keyUsage[]` | `string` | yes |
| `certificates.edges[].node.ocspServer` | `string` | yes |
| `certificates.edges[].node.passwordProtected` | `boolean` | yes |
| `certificates.edges[].node.privKeyCompromised` | `boolean` | yes |
| `certificates.edges[].node.privateDsaKey` | `string` | yes |
| `certificates.edges[].node.publicDsaKey` | `string` | yes |
| `certificates.edges[].node.publicKeyAlgorithm` | `string` | yes |
| `certificates.edges[].node.revoked[]` | `string` | yes |
| `certificates.edges[].node.seed` | `string` | yes |
| `certificates.edges[].node.selfSigned` | `boolean` | yes |
| `certificates.edges[].node.serial` | `string` | yes |
| `certificates.edges[].node.sha1` | `string` | yes |
| `certificates.edges[].node.sha256` | `string` | yes |
| `certificates.edges[].node.signature` | `string` | yes |
| `certificates.edges[].node.signatureAlgorithm` | `string` | yes |
| `certificates.edges[].node.signatureValid` | `boolean` | yes |
| `certificates.edges[].node.startDate` | `string` | yes |
| `certificates.edges[].node.subjectCommonName` | `string` | yes |
| `certificates.edges[].node.subjectCountry` | `string` | yes |
| `certificates.edges[].node.subjectDN` | `string` | yes |
| `certificates.edges[].node.subjectLocality` | `string` | yes |
| `certificates.edges[].node.subjectOrgUnit` | `string` | yes |
| `certificates.edges[].node.subjectOrganization` | `string` | yes |
| `certificates.edges[].node.subjectPostalCode` | `string` | yes |
| `certificates.edges[].node.subjectProvince` | `string` | yes |
| `certificates.edges[].node.subjectRdn` | `string` | yes |
| `certificates.edges[].node.subjectSerialNumber` | `string` | yes |
| `certificates.edges[].node.subjectStreetAddress` | `string` | yes |
| `certificates.edges[].node.uniqueHash` | `string` | yes |
| `certificates.edges[].node.version` | `integer` | yes |
| `certificates.pageInfo` | `object` | yes |
| `certificates.pageInfo.endCursor` | `string` | yes |
| `certificates.pageInfo.hasNextPage` | `boolean` | no |
| `certificates.pageInfo.hasPreviousPage` | `boolean` | no |
| `certificates.pageInfo.startCursor` | `string` | yes |
| `certificates.pageInfo.totalCount` | `integer` | yes |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    CertificatesInput,
    Cursor,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_certificates(certificates_args=CertificatesInput(asset_id='asset_123', cursor=Cursor()))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
