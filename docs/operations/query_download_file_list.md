<!-- Generated file: do not edit by hand -->

# query_download_file_list

Generate a URL to download a list of all files.

## Parameters

| name | type | required |
| --- | --- | --- |
| `download_file_list_args` | `FileListDownloadInput` | `true` |

## Response Schema

| Field | Type | Nullable |
| --- | --- | --- |
| `download` | `object` | yes |
| `download.fileList` | `object` | no |
| `download.fileList.downloadUrlsList[]` | `string` | yes |
| `download.fileList.pathsList[]` | `string` | yes |

## Example

```python
from __future__ import annotations

from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import (
    FileListDownloadInput,
)


def main() -> None:
    cfg = TurbineClientConfig.from_env()
    sdk = TurbineClient(cfg)

    with sdk.graphql() as client:
        resp = client.query_download_file_list(download_file_list_args=FileListDownloadInput(asset_id='asset_123'))
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
