# Files and uploads

## list_files

Return the complete recursive file listing for an asset in a single call:

```python
from netrise_turbine_sdk import TurbineClient, TurbineClientConfig

sdk = TurbineClient(TurbineClientConfig.from_env())
files = sdk.list_files("your-asset-id")

for f in files:
    print(f["filesystemPath"], f.get("size"), f.get("mimeType"))

print(f"Total files: {len(files)}")
```

Internally the SDK fetches a signed URL via `query_download_file_list`, then downloads and parses the NDJSON listing — one call, one plain list. Pass the asset identifier without its revision suffix.

**Returns:** `list[dict]` — one dict per file. Common keys:

| Key | Type | Description |
| --- | --- | --- |
| `path` | `str` | Full path including archive structure (e.g. `/tar/blobs/.../etc/passwd`) |
| `filesystemPath` | `str` | Logical filesystem path (e.g. `/etc/passwd`) |
| `size` | `int` | File size in bytes (absent for directories) |
| `mimeType` | `str` | MIME type (e.g. `text/plain`, `inode/directory`) |
| `permissions` | `str` | Unix permission string (e.g. `-rw-r--r--`) |
| `hashMd5` | `str` | MD5 digest (files only) |
| `hashSha1` | `str` | SHA-1 digest (files only) |
| `hashSha256` | `str` | SHA-256 digest (files only) |
| `hasChildren` | `bool` | Whether the entry is a directory with children |
| `createdAt` | `str` | Creation timestamp |
| `updatedAt` | `str` | Last modification timestamp |

## upload_asset

Upload helpers wrap the two-step flow (signed URL, then PUT) in one call and stream from disk, so file size is not a constraint.

```python
from netrise_turbine_sdk import TurbineClient, TurbineClientConfig
from netrise_turbine_sdk_graphql.input_types import SubmitAssetInput

sdk = TurbineClient(TurbineClientConfig.from_env())

# Simple -- uses the filename as the asset name
resp = sdk.upload_asset("./firmware.bin")
print(f"Upload ID: {resp.asset.submit.upload_id}")

# With a display name
resp = sdk.upload_asset("./firmware.bin", name="My Firmware v1.0")

# With full metadata
resp = sdk.upload_asset(
    "./image.tar",
    submit_args=SubmitAssetInput(
        name="Router Firmware",
        product="home-router",
        manufacturer="Acme Corp",
        version="2.1.0",
    ),
)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `file_path` | `str \| Path` | Path to the file to upload |
| `submit_args` | `SubmitAssetInput` | Optional metadata (name, manufacturer, model, version, type, etc.) |
| `name` | `str` | Optional display name. Defaults to the filename. Ignored if `submit_args.name` is set |

**Returns:** `MutationAssetSubmit` response containing asset info and upload details.

## upload_assets

Upload all files in a directory as assets (batch):

```python
# Simple: upload all files with default names
results = sdk.upload_assets("./firmware_images/")

# With per-file metadata
def make_args(path):
    return SubmitAssetInput(name=f"device-{path.name}", product="iot-devices")

results = sdk.upload_assets("./firmware/", submit_args_fn=make_args)

for file_path, resp in results:
    print(f"{file_path.name}: {resp.asset.submit.upload_id}")
```

| Parameter | Type | Description |
| --- | --- | --- |
| `directory` | `str \| Path` | Path to directory containing files to upload |
| `submit_args_fn` | `callable` | Optional function `(Path) -> SubmitAssetInput`. If omitted, the filename is used as the asset name |

**Returns:** List of `(Path, MutationAssetSubmit)` tuples for successfully uploaded files. Failed uploads are logged to stderr but do not stop the batch.

## Upload timeout

File uploads default to a 5-minute timeout. For very large files over slow connections, override it at construction:

```python
sdk = TurbineClient(TurbineClientConfig.from_env(), upload_timeout=600.0)
```
