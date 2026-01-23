# Turbine Python SDK

Minimal, sync-first Python client for the Turbine GraphQL API.

## Getting Started

### Installation from PyPI

Install from PyPI as `netrise-turbine-sdk`:

```bash
# pip
pip install netrise-turbine-sdk

# poetry
poetry add netrise-turbine-sdk

# uv
uv add netrise-turbine-sdk
```

### Configure environment variables

The SDK automatically loads environment variables from a `.env` file in your current working directory when you call `TurbineClientConfig.from_env()`. You can also set environment variables directly.

**Option 1: Using a `.env` file (recommended)**

Create a `.env` file in your project directory:

```bash
endpoint=https://apollo.turbine.netrise.io/graphql/v3
audience=https://prod.turbine.netrise.io/
domain=https://authn.turbine.netrise.io
client_id=<client_id>
client_secret=<client_secret>
organization_id=<org_id>
```

The SDK will automatically load these when you call `TurbineClientConfig.from_env()`. The `.env` file is searched in:
- Current working directory (most common)
- Parent directories (walks up the directory tree)

**Option 2: Set environment variables directly**

```python
import os
os.environ["endpoint"] = "https://apollo.turbine.netrise.io/graphql/v3"
# ... set other variables

cfg = TurbineClientConfig.from_env(load_env_file=False)
```

**Option 3: Disable automatic .env loading**

If you prefer to load `.env` files manually:

```python
from dotenv import load_dotenv
load_dotenv()  # Your custom loading logic

cfg = TurbineClientConfig.from_env(load_env_file=False)
```

## API Documentation & Code Samples

<!-- Index is auto-generated below this point -->

- [mutation_add_asset_groups_to_assets](operations/mutation_add_asset_groups_to_assets.md): Associate a list of existing asset groups with selected assets.
- [mutation_add_assets_to_asset_group](operations/mutation_add_assets_to_asset_group.md): Add specified assets to an existing asset group for organization.
- [mutation_asset_add_dependency](operations/mutation_asset_add_dependency.md): Manually inject a missing dependency component into an asset's inventory.
- [mutation_asset_modify_dependency](operations/mutation_asset_modify_dependency.md): Update metadata or details for a manually added asset dependency.
- [mutation_asset_remove_dependencies](operations/mutation_asset_remove_dependencies.md): Remove specific dependencies from the component list of an asset.
- [mutation_asset_submit](operations/mutation_asset_submit.md): Upload firmware or SBOMs with metadata, group assignments, and CPEs.
- [mutation_asset_update](operations/mutation_asset_update.md): Modify metadata such as name, vendor, or version for assets.
- [mutation_create_asset_group](operations/mutation_create_asset_group.md): Create a new named group to organize and track assets.
- [mutation_delete_asset_group](operations/mutation_delete_asset_group.md): Permanently remove an asset group while keeping contained assets intact.
- [mutation_remediate_all_asset_vulnerabilities](operations/mutation_remediate_all_asset_vulnerabilities.md): Apply a remediation status to all vulnerabilities matching specific filters.
- [mutation_remediate_asset_vulnerabilities](operations/mutation_remediate_asset_vulnerabilities.md): Bulk apply VEX remediation status to multiple vulnerabilities on assets.
- [mutation_remediate_asset_vulnerability](operations/mutation_remediate_asset_vulnerability.md): Update remediation status and justification for a single asset vulnerability.
- [mutation_remediate_license_issues](operations/mutation_remediate_license_issues.md): Update status and add notes to resolve identified license issues.
- [mutation_remove_all_asset_groups_from_assets](operations/mutation_remove_all_asset_groups_from_assets.md): Disassociate all asset groups from a specified list of assets.
- [mutation_remove_assets_from_asset_group](operations/mutation_remove_assets_from_asset_group.md): Remove selected assets from a specific asset group container configuration.
- [mutation_set_asset_groups_to_asset](operations/mutation_set_asset_groups_to_asset.md): Replace all current group associations for an asset with new ones.
- [mutation_set_assets_to_asset_group](operations/mutation_set_assets_to_asset_group.md): Overwrite the member list of an asset group with new assets.
- [mutation_update_asset_group](operations/mutation_update_asset_group.md): Rename or update the description of an existing asset group.
- [mutation_update_org_level_settings](operations/mutation_update_org_level_settings.md): Configure global organization settings such as idle session timeout duration.
- [mutation_user_action](operations/mutation_user_action.md): Perform administrative actions like enabling or disabling specific user accounts.
- [mutation_user_delete](operations/mutation_user_delete.md): Permanently delete a user account and remove their access rights.
- [mutation_user_invite](operations/mutation_user_invite.md): Invite a new user to the organization with a specific role.
- [mutation_user_remove](operations/mutation_user_remove.md): Remove a user from the organization without deleting their account.
- [mutation_user_reset_password](operations/mutation_user_reset_password.md): Trigger a password reset email for a specific user account.
- [mutation_user_set_user_role](operations/mutation_user_set_user_role.md): Assign a new permission role like Owner or Operator to users.
- [mutation_user_update_user](operations/mutation_user_update_user.md): Modify user profile information including name and contact email details.
- [query_activity](operations/query_activity.md): Retrieve a comprehensive log of actions and events for assets.
- [query_analytics](operations/query_analytics.md): Access high-level risk data and charts for organization dashboards.
- [query_asset](operations/query_asset.md): Retrieve detailed metadata and risk information for a single asset.
- [query_asset_group_analytics](operations/query_asset_group_analytics.md): View risk metrics and exploit counts for a specific group.
- [query_asset_group_members](operations/query_asset_group_members.md): List all assets associated with a specific asset group container.
- [query_asset_groups](operations/query_asset_groups.md): Retrieve a detailed paginated list of all asset groups available.
- [query_asset_status](operations/query_asset_status.md): Check if an asset is currently processing or has finished.
- [query_asset_upload](operations/query_asset_upload.md): Obtain a secure pre-signed URL to upload files for analysis.
- [query_asset_vulnerability_remediation](operations/query_asset_vulnerability_remediation.md): Retrieve current VEX status and justification for a specific vulnerability.
- [query_assets_overview](operations/query_assets_overview.md): View high-level risk and threat exposure metrics for multiple assets.
- [query_assets_relay](operations/query_assets_relay.md): Retrieve a paginated, sortable list of assets with filtering options.
- [query_binary_protections](operations/query_binary_protections.md): List security hardening details for binaries found within the asset.
- [query_binary_protections_summary](operations/query_binary_protections_summary.md): Get aggregated counts of binary hardening features like NX or PIE.
- [query_caas_availability](operations/query_caas_availability.md): Check for the availability of the RISE AI analysis report.
- [query_certificates](operations/query_certificates.md): List X.509 certificates and validity status found in the asset.
- [query_credentials](operations/query_credentials.md): Identify user accounts and password hashes discovered within the filesystem.
- [query_dependencies](operations/query_dependencies.md): List all software components and libraries identified in the asset.
- [query_dependency_known_exploits](operations/query_dependency_known_exploits.md): Check if specific dependencies are linked to known public exploits.
- [query_detailed_vulnerabilities](operations/query_detailed_vulnerabilities.md): Retrieve in-depth vulnerability data including descriptions and CVSS vector strings.
- [query_download_extracted_firmware](operations/query_download_extracted_firmware.md): Generate a URL to download the full unpacked file system.
- [query_download_file](operations/query_download_file.md): Create a secure link to download a specific individual file.
- [query_download_file_list](operations/query_download_file_list.md): Generate a URL to download a list of all files.
- [query_download_firmware](operations/query_download_firmware.md): Generate a link to download the original uploaded firmware image.
- [query_get_vuln_reachability](operations/query_get_vuln_reachability.md): Determine if a vulnerability can be executed via system paths.
- [query_grouped_dependencies](operations/query_grouped_dependencies.md): View dependencies aggregated by vendor, license, or specific component type.
- [query_hashes](operations/query_hashes.md): List cryptographic hashes for files identified within the asset filesystem.
- [query_match_vulnerabilities](operations/query_match_vulnerabilities.md): Find specific vulnerabilities matching a provided component identifier or package.
- [query_metrics](operations/query_metrics.md): View organization-wide statistics on asset counts, processing, and risk.
- [query_misconfigurations](operations/query_misconfigurations.md): List failed security checks and configuration risks found in assets.
- [query_org_level_settings](operations/query_org_level_settings.md): Check how the tenant organization is configured.
- [query_package_dependencies_by_id](operations/query_package_dependencies_by_id.md): View the dependency tree hierarchy for a specific software package.
- [query_private_keys](operations/query_private_keys.md): Detect private cryptographic keys stored insecurely on the asset filesystem.
- [query_public_keys](operations/query_public_keys.md): List public cryptographic keys found within the asset's file system.
- [query_rise_ai_analysis_data](operations/query_rise_ai_analysis_data.md): Check for the contents of the RISE AI analysis report.
- [query_search](operations/query_search.md): Execute keyword searches across all artifacts and files in organization.
- [query_sift](operations/query_sift.md): Perform fuzzy hash matching to find similar code or files.
- [query_user_orgs](operations/query_user_orgs.md): List all organizations the current user is authorized to access.
- [query_users](operations/query_users.md): Retrieve a detailed list of all users and their assigned roles.
- [query_vulnerabilities](operations/query_vulnerabilities.md): List CVEs and associated risks for components in an asset.
- [query_vulnerabilities_overview](operations/query_vulnerabilities_overview.md): Get a summary of vulnerability counts and severity across assets.
- [query_vulnerability](operations/query_vulnerability.md): Retrieve detailed metadata, scores, and descriptions for a specific vulnerability.
- [query_vulnerability_external_filters](operations/query_vulnerability_external_filters.md): Count vulnerabilities matching external threat feeds like CISA or botnets.
