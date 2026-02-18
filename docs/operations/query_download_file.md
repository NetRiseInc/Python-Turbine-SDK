<!-- Generated file: do not edit by hand -->

# query_download_file

Create a secure link to download a specific individual file.

## Parameters

| name | type | required |
| --- | --- | --- |
| `download_file_args` | `FileDownloadInput` | `true` |

## Response Schema

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
        print(resp.model_dump())


if __name__ == "__main__":
    main()
```
