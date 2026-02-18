<!-- Generated file: do not edit by hand -->

# query_download_extracted_firmware

Generate a URL to download the full unpacked file system.

## Parameters

| name | type | required |
| --- | --- | --- |
| `download_extracted_firmware_args` | `ExtractedFirmwareDownloadInput` | `true` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `download` | `object` | yes |
| `download.extractedFirmware` | `object` | no |
| `download.extractedFirmware.downloadUrlsList[]` | `string` | yes |
| `download.extractedFirmware.pathsList[]` | `string` | yes |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    ExtractedFirmwareDownloadInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_download_extracted_firmware(download_extracted_firmware_args=ExtractedFirmwareDownloadInput(asset_id='asset_123'))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
