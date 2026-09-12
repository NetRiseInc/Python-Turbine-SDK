<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# query_download_extracted_firmware

[Back to the index](../README.md)

Get a URL to download the unpacked filesystem.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |
| `download_extracted_firmware_args` | `ExtractedFirmwareDownloadInput` | `true` |

## Response fields

Typed attributes on the response model.

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
        # Responses are typed Pydantic models: read fields as attributes.
        for value in resp.download.extracted_firmware.download_urls_list or []:
            print(value)


if __name__ == "__main__":
    main()
```
