<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# query_download_firmware

[Back to the index](../README.md)

Get a URL to download the original uploaded image.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |
| `download_firmware_args` | `FirmwareDownloadInput` | `true` |

## Response fields

Typed attributes on the response model.

| Field | Type | Nullable |
| --- | --- | --- |
| `download` | `object` | yes |
| `download.firmware` | `object` | no |
| `download.firmware.downloadUrlsList[]` | `string` | yes |
| `download.firmware.pathsList[]` | `string` | yes |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    FirmwareDownloadInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_download_firmware(download_firmware_args=FirmwareDownloadInput(asset_id='asset_123'))
        # Responses are typed Pydantic models: read fields as attributes.
        for value in resp.download.firmware.download_urls_list or []:
            print(value)


if __name__ == "__main__":
    main()
```
