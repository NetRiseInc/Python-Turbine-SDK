<!-- Generated file: do not edit by hand -->
<!-- Source: turbine/sdk-tools/generate_python_sdk_docs/generate_python_sdk_docs.py -->

# query_download_file

[Back to the index](../README.md)

Get a URL to download one extracted file.

## Parameters

Arguments on the generated client method.

| name | type | required |
| --- | --- | --- |
| `download_file_args` | `FileDownloadInput` | `true` |

## Response fields

Typed attributes on the response model.

| Field | Type | Nullable |
| --- | --- | --- |
| `download` | `object` | yes |
| `download.file` | `object` | no |
| `download.file.downloadUrlsList[]` | `string` | yes |
| `download.file.pathsList[]` | `string` | yes |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    FileDownloadInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_download_file(download_file_args=FileDownloadInput(asset_id='asset_123', file_paths=['./path/to/file']))
        # Responses are typed Pydantic models: read fields as attributes.
        for value in resp.download.file.download_urls_list or []:
            print(value)


if __name__ == "__main__":
    main()
```
