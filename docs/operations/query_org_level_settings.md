<!-- Generated file: do not edit by hand -->

# query_org_level_settings

Check how the tenant organization is configured.

## Parameters

| name | type | required |
| --- | --- | --- |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `orgLevelSettings` | `object` | yes |
| `orgLevelSettings.advancedSettingsJobsProcessing` | `boolean` | yes |
| `orgLevelSettings.binaryFingerprintEnabled` | `object` | yes |
| `orgLevelSettings.binaryFingerprintEnabled.componentCount` | `integer` | yes |
| `orgLevelSettings.binaryFingerprintEnabled.confidence` | `Confidence` | yes |
| `orgLevelSettings.binaryFingerprintEnabled.enabled` | `boolean` | yes |
| `orgLevelSettings.curatedHashEnabled` | `object` | yes |
| `orgLevelSettings.curatedHashEnabled.componentCount` | `integer` | yes |
| `orgLevelSettings.curatedHashEnabled.confidence` | `Confidence` | yes |
| `orgLevelSettings.curatedHashEnabled.enabled` | `boolean` | yes |
| `orgLevelSettings.idleTimeoutSeconds` | `integer` | yes |
| `orgLevelSettings.idleTimoutEnabled` | `boolean` | yes |
| `orgLevelSettings.kernelModuleEnabled` | `object` | yes |
| `orgLevelSettings.kernelModuleEnabled.componentCount` | `integer` | yes |
| `orgLevelSettings.kernelModuleEnabled.confidence` | `Confidence` | yes |
| `orgLevelSettings.kernelModuleEnabled.enabled` | `boolean` | yes |
| `orgLevelSettings.legacyHashEnabled` | `object` | yes |
| `orgLevelSettings.legacyHashEnabled.componentCount` | `integer` | yes |
| `orgLevelSettings.legacyHashEnabled.confidence` | `Confidence` | yes |
| `orgLevelSettings.legacyHashEnabled.enabled` | `boolean` | yes |
| `orgLevelSettings.libraryNameEnabled` | `object` | yes |
| `orgLevelSettings.libraryNameEnabled.componentCount` | `integer` | yes |
| `orgLevelSettings.libraryNameEnabled.confidence` | `Confidence` | yes |
| `orgLevelSettings.libraryNameEnabled.enabled` | `boolean` | yes |
| `orgLevelSettings.libraryVersionEnabled` | `object` | yes |
| `orgLevelSettings.libraryVersionEnabled.componentCount` | `integer` | yes |
| `orgLevelSettings.libraryVersionEnabled.confidence` | `Confidence` | yes |
| `orgLevelSettings.libraryVersionEnabled.enabled` | `boolean` | yes |
| `orgLevelSettings.packageManifestEnabled` | `object` | yes |
| `orgLevelSettings.packageManifestEnabled.componentCount` | `integer` | yes |
| `orgLevelSettings.packageManifestEnabled.confidence` | `Confidence` | yes |
| `orgLevelSettings.packageManifestEnabled.enabled` | `boolean` | yes |
| `orgLevelSettings.peMetaDataEnabled` | `object` | yes |
| `orgLevelSettings.peMetaDataEnabled.componentCount` | `integer` | yes |
| `orgLevelSettings.peMetaDataEnabled.confidence` | `Confidence` | yes |
| `orgLevelSettings.peMetaDataEnabled.enabled` | `boolean` | yes |
| `orgLevelSettings.riseAiInsightsReportEnabled` | `boolean` | yes |
| `orgLevelSettings.signatureEnabled` | `object` | yes |
| `orgLevelSettings.signatureEnabled.componentCount` | `integer` | yes |
| `orgLevelSettings.signatureEnabled.confidence` | `Confidence` | yes |
| `orgLevelSettings.signatureEnabled.enabled` | `boolean` | yes |
| `orgLevelSettings.symbolIndexEnabled` | `object` | yes |
| `orgLevelSettings.symbolIndexEnabled.componentCount` | `integer` | yes |
| `orgLevelSettings.symbolIndexEnabled.confidence` | `Confidence` | yes |
| `orgLevelSettings.symbolIndexEnabled.enabled` | `boolean` | yes |
| `orgLevelSettings.userModifiedEnabled` | `object` | yes |
| `orgLevelSettings.userModifiedEnabled.componentCount` | `integer` | yes |
| `orgLevelSettings.userModifiedEnabled.confidence` | `Confidence` | yes |
| `orgLevelSettings.userModifiedEnabled.enabled` | `boolean` | yes |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_org_level_settings()
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
