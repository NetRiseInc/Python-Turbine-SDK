# Turbine Python SDK

Minimal, sync-first Python client for the Turbine GraphQL API.

The stable user-facing package is `netrise_turbine_sdk`. The generated
`netrise_turbine_sdk_graphql` package tracks the upstream GraphQL schema for
power users. See the packaged `README.md` and `CHANGELOG.md` for the full
versioning policy and release notes.

---

## Quick start

### 1. Install

```bash
pip install netrise-turbine-sdk
```

Also available via `poetry add netrise-turbine-sdk` or `uv add netrise-turbine-sdk`.

### 2. Configure credentials

Create a `.env` file in your project directory:

```bash
endpoint=https://apollo.turbine.netrise.io/graphql/v3
audience=https://prod.turbine.netrise.io/
domain=https://authn.turbine.netrise.io
client_id=<your_client_id>
client_secret=<your_client_secret>
organization_id=<your_org_id>
```

The SDK loads this automatically. Reach out to [support@netrise.io](mailto:support@netrise.io) if you need credentials.

### 3. Run your first query

```python
from netrise_turbine_sdk import TurbineClient, TurbineClientConfig

sdk = TurbineClient(TurbineClientConfig.from_env())

for asset in sdk.iter_assets(page_size=10, max_pages=1):
    critical = asset.analytic.vulnerability.critical if asset.analytic else 0
    print(f"{asset.name}  risk={asset.risk.score}  critical_vulns={critical}")
```

Authentication, pagination, and connection pooling are handled for you.

---

## Pick a level

| Level | What you get | When to use |
| --- | --- | --- |
| **1. Lite iterators** | Typed, auto-paginated iterators with lean payloads | Most workflows — lists, reports, triage, CSV exports |
| **2. Full iterators** | Same iterators but every field to depth 5 | Deeply nested data (correlations, remediation, exploit metadata) |
| **3. Custom GraphQL** | Your own queries against the full schema | Field combinations no pre-built query provides |

Start at Level 1. Move to Level 2 or 3 only when Lite does not include the fields you need.

OAuth client credentials (`domain`, `client_id`, `client_secret`, `audience`, `organization_id`) are fetched and cached automatically. See [Configuration](guides/configuration.md) for constructor options, extra headers, and client lifecycle.

---

## Guides

| Guide | Covers |
| --- | --- |
| [Iterators](guides/iterators.md) | Lite / Full / Summary, kwargs, `Paginator`, triage and CSV examples |
| [Filtering](guides/filtering.md) | Convenience kwargs, `where()`, dicts, merging, sorting |
| [Custom GraphQL](guides/custom-graphql.md) | `execute()`, dict responses, manual pagination |
| [Errors](guides/errors.md) | Exception types, retries, `x-request-id` |
| [Files and uploads](guides/files-and-uploads.md) | `list_files`, `upload_asset`, `upload_assets` |
| [Configuration](guides/configuration.md) | Constructor, env loading, extra headers, lifecycle |

---

## Operations index

<!-- Index is auto-generated below this point -->

### Vulnerabilities

- [query_asset_vulnerability_remediation](operations/query_asset_vulnerability_remediation.md): Get VEX status and justification for one vuln on an asset.
- [query_detailed_vulnerabilities](operations/query_detailed_vulnerabilities.md): List vulns with descriptions and full CVSS vectors.
- [query_detailed_vulnerabilities_lite](operations/query_detailed_vulnerabilities_lite.md): List vulns with description and preferred CVSS v3.1 only.
- [query_get_vuln_reachability](operations/query_get_vuln_reachability.md): Check whether a vulnerability is reachable via system paths.
- [query_match_vulnerabilities](operations/query_match_vulnerabilities.md): Find vulnerabilities matching a component or package.
- [query_remediated_vulnerabilities_by_asset](operations/query_remediated_vulnerabilities_by_asset.md): List remediated vulns for one status bucket, by asset.
- [query_vulnerabilities](operations/query_vulnerabilities.md): List CVEs on an asset with scores and fix versions.
- [query_vulnerabilities_lite](operations/query_vulnerabilities_lite.md): List vulns with CVE, severity, scores, and counts.
- [query_vulnerabilities_overview](operations/query_vulnerabilities_overview.md): Get vulnerability counts and severity across assets.
- [query_vulnerability](operations/query_vulnerability.md): Get scores and metadata for one vulnerability.
- [query_vulnerability_external_filters](operations/query_vulnerability_external_filters.md): Count vulns matching threat feeds such as CISA KEV.
- [query_vulnerability_jira_tickets](operations/query_vulnerability_jira_tickets.md): List Jira tickets linked to a vuln on an asset.
- [query_vulnerability_lite](operations/query_vulnerability_lite.md): Get one vuln with preferred CVSS v3.1 only.
- [query_vulnerability_remediation_summary](operations/query_vulnerability_remediation_summary.md): Get org-wide counts of applied VEX statuses.
- [mutation_remediate_all_asset_vulnerabilities](operations/mutation_remediate_all_asset_vulnerabilities.md): Apply a VEX status to every vuln matching a filter.
- [mutation_remediate_asset_vulnerabilities](operations/mutation_remediate_asset_vulnerabilities.md): Bulk-apply VEX status to selected asset vulns.
- [mutation_remediate_asset_vulnerability](operations/mutation_remediate_asset_vulnerability.md): Set VEX status and justification for one asset vuln.

### Reports and search

- [query_get_asset_comparison_report](operations/query_get_asset_comparison_report.md): Get a finished asset comparison report.
- [query_list_asset_comparison_reports](operations/query_list_asset_comparison_reports.md): List asset comparison reports with filters and sorting.
- [query_list_asset_correlations](operations/query_list_asset_correlations.md): List cross-asset correlations for shared components or vulns.
- [query_search](operations/query_search.md): Keyword-search artifacts and files across the org.
- [query_sift](operations/query_sift.md): Fuzzy-hash match to find similar code or files.
- [mutation_create_asset_comparison_report](operations/mutation_create_asset_comparison_report.md): Start a comparison report between two assets.
- [mutation_delete_asset_comparison_report](operations/mutation_delete_asset_comparison_report.md): Delete an asset comparison report by ID.

### Components and SBOM

- [query_dependencies](operations/query_dependencies.md): List software components identified in an asset.
- [query_dependencies_lite](operations/query_dependencies_lite.md): List components with identity, version, license, and rollups.
- [query_dependency_known_exploits](operations/query_dependency_known_exploits.md): Check whether dependencies link to known public exploits.
- [query_get_dependency_reachability](operations/query_get_dependency_reachability.md): Check whether a dependency is reachable via paths or scripts.
- [query_grouped_dependencies](operations/query_grouped_dependencies.md): List dependencies grouped by vendor, license, or type.
- [query_identified_components_preview](operations/query_identified_components_preview.md): Preview org-wide component counts under identification settings.
- [query_list_asset_crypto_libraries](operations/query_list_asset_crypto_libraries.md): List crypto libraries detected in an asset.
- [query_package_dependencies_by_id](operations/query_package_dependencies_by_id.md): Get the dependency tree for one package.
- [mutation_asset_add_dependency](operations/mutation_asset_add_dependency.md): Add a manual dependency component to an asset.
- [mutation_asset_modify_dependency](operations/mutation_asset_modify_dependency.md): Update a manually added asset dependency.
- [mutation_asset_remove_dependencies](operations/mutation_asset_remove_dependencies.md): Remove selected dependencies from an asset.

### Assets

- [query_activity](operations/query_activity.md): List activity-log events for an asset.
- [query_asset](operations/query_asset.md): Get metadata and risk for one asset.
- [query_asset_group_analytics](operations/query_asset_group_analytics.md): Get risk metrics for one asset group.
- [query_asset_group_members](operations/query_asset_group_members.md): List assets in an asset group.
- [query_asset_groups](operations/query_asset_groups.md): List asset groups with pagination and filters.
- [query_asset_status](operations/query_asset_status.md): Check whether an asset is still processing.
- [query_asset_upload](operations/query_asset_upload.md): Get a pre-signed URL to upload a file for analysis.
- [query_assets_overview](operations/query_assets_overview.md): Get risk and threat rollups across assets.
- [query_assets_relay](operations/query_assets_relay.md): List assets with full nested fields (paginated).
- [query_assets_relay_lite](operations/query_assets_relay_lite.md): List assets with identity, status, risk, and analytic rollups.
- [query_assets_relay_summary](operations/query_assets_relay_summary.md): List assets as id, name, and analytic counts only.
- [query_download_extracted_firmware](operations/query_download_extracted_firmware.md): Get a URL to download the unpacked filesystem.
- [query_download_file](operations/query_download_file.md): Get a URL to download one extracted file.
- [query_download_file_list](operations/query_download_file_list.md): Get a URL to download the asset file listing.
- [query_download_firmware](operations/query_download_firmware.md): Get a URL to download the original uploaded image.
- [query_hashes](operations/query_hashes.md): List file hashes from an asset filesystem.
- [query_list_entity_assets](operations/query_list_entity_assets.md): List assets a user or security group can access.
- [mutation_add_asset_groups_to_assets](operations/mutation_add_asset_groups_to_assets.md): Attach asset groups to one or more assets.
- [mutation_add_assets_to_asset_group](operations/mutation_add_assets_to_asset_group.md): Add assets to an existing asset group.
- [mutation_asset_submit](operations/mutation_asset_submit.md): Submit firmware or an SBOM for analysis.
- [mutation_asset_update](operations/mutation_asset_update.md): Update asset metadata such as name, vendor, or version.
- [mutation_create_asset_group](operations/mutation_create_asset_group.md): Create a named asset group.
- [mutation_delete_asset_group](operations/mutation_delete_asset_group.md): Delete an asset group; assets stay in the org.
- [mutation_remove_all_asset_groups_from_assets](operations/mutation_remove_all_asset_groups_from_assets.md): Detach every asset group from the given assets.
- [mutation_remove_assets_from_asset_group](operations/mutation_remove_assets_from_asset_group.md): Remove selected assets from an asset group.
- [mutation_set_asset_groups_to_asset](operations/mutation_set_asset_groups_to_asset.md): Replace an asset's group memberships.
- [mutation_set_assets_to_asset_group](operations/mutation_set_assets_to_asset_group.md): Replace an asset group's member list.
- [mutation_update_asset_group](operations/mutation_update_asset_group.md): Rename or update an asset group's description.

### Secrets and credentials

- [query_credentials](operations/query_credentials.md): List accounts and password hashes found in an asset.
- [query_get_secret_reachability](operations/query_get_secret_reachability.md): Check whether secrets are reachable via paths or scripts.
- [query_secret](operations/query_secret.md): Get details for one discovered secret.
- [query_secret_categories_summary](operations/query_secret_categories_summary.md): Get secret counts grouped by category.
- [query_secret_status_count](operations/query_secret_status_count.md): Get secret counts grouped by remediation status.
- [query_secret_types_and_count](operations/query_secret_types_and_count.md): List secret types with occurrence counts.
- [query_secrets](operations/query_secrets.md): List secrets discovered in an asset.
- [query_secrets_summary](operations/query_secrets_summary.md): Get a summary of secret findings on an asset.
- [mutation_remediate_secrets](operations/mutation_remediate_secrets.md): Set remediation status and justification on secrets.

### Cryptography

- [query_binary_protections](operations/query_binary_protections.md): List binary hardening details for an asset.
- [query_binary_protections_summary](operations/query_binary_protections_summary.md): Get counts of hardening features such as NX or PIE.
- [query_certificate_external_filters](operations/query_certificate_external_filters.md): List filter options for certificate queries.
- [query_certificates](operations/query_certificates.md): List X.509 certificates found in an asset.
- [query_get_certificate_reachability](operations/query_get_certificate_reachability.md): Check whether certificates are reachable via paths or scripts.
- [query_private_key_external_filters](operations/query_private_key_external_filters.md): List filter options for private-key queries.
- [query_private_keys](operations/query_private_keys.md): List private keys found in an asset filesystem.
- [query_public_key_external_filters](operations/query_public_key_external_filters.md): List filter options for public-key queries.
- [query_public_keys](operations/query_public_keys.md): List public keys found in an asset filesystem.
- [mutation_remediate_certificates](operations/mutation_remediate_certificates.md): Set remediation status and notes on certificate findings.
- [mutation_remediate_private_keys](operations/mutation_remediate_private_keys.md): Set remediation status on private key findings.
- [mutation_remediate_public_keys](operations/mutation_remediate_public_keys.md): Set remediation status on public key findings.

### Licenses

- [query_license](operations/query_license.md): Get details for one software license.
- [query_license_issue](operations/query_license_issue.md): Get details for one license compliance issue.
- [query_license_issues](operations/query_license_issues.md): List license compliance issues on an asset.
- [query_license_issues_external_filters](operations/query_license_issues_external_filters.md): List filter options for license-issue queries.
- [query_licenses_spdx_ids](operations/query_licenses_spdx_ids.md): List SPDX license identifiers.
- [mutation_remediate_license_issues](operations/mutation_remediate_license_issues.md): Set status and notes on license compliance issues.

### Misconfigurations and hardening

- [query_misconfigurations](operations/query_misconfigurations.md): List failed security checks on an asset.
- [query_misconfigurations_lite](operations/query_misconfigurations_lite.md): List misconfigs with check ID, severity, result, and counts.

### Users and access

- [query_get_my_permissions](operations/query_get_my_permissions.md): List permission IDs held by the calling user.
- [query_get_resource_permissions](operations/query_get_resource_permissions.md): List the caller's effective permissions on a resource.
- [query_get_role](operations/query_get_role.md): Get one RBAC role by ID.
- [query_get_role_delete_impact](operations/query_get_role_delete_impact.md): Preview who loses access if a custom role is deleted.
- [query_get_security_group_delete_impact](operations/query_get_security_group_delete_impact.md): Preview who loses access if a security group is deleted.
- [query_list_ac_rs](operations/query_list_ac_rs.md): List access control records, optionally for one user.
- [query_list_my_ac_rs](operations/query_list_my_ac_rs.md): List access control records that apply to you.
- [query_list_my_security_groups](operations/query_list_my_security_groups.md): List security groups you belong to.
- [query_list_org_users](operations/query_list_org_users.md): List org users with groups and accessible asset counts.
- [query_list_permissions](operations/query_list_permissions.md): List the permission catalog for custom roles.
- [query_list_roles](operations/query_list_roles.md): List RBAC roles for the current organization.
- [query_list_security_group_members](operations/query_list_security_group_members.md): List members of a security group.
- [query_list_security_groups](operations/query_list_security_groups.md): List RBAC security groups for the current org.
- [query_me](operations/query_me.md): Get the authenticated user's profile.
- [query_metrics](operations/query_metrics.md): Get org-wide counts for assets, processing, and risk.
- [query_user_orgs](operations/query_user_orgs.md): List organizations the current user can access.
- [query_users](operations/query_users.md): List users and their assigned roles.
- [mutation_add_security_group_member](operations/mutation_add_security_group_member.md): Add a user to an RBAC security group.
- [mutation_bulk_delete_ac_rs](operations/mutation_bulk_delete_ac_rs.md): Delete many access control records; missing ones count as success.
- [mutation_create_acr](operations/mutation_create_acr.md): Grant a user or security group a role on a resource.
- [mutation_create_custom_role](operations/mutation_create_custom_role.md): Create an org-scoped custom role with chosen permissions.
- [mutation_create_security_group](operations/mutation_create_security_group.md): Create an RBAC security group in the current org.
- [mutation_delete_acr](operations/mutation_delete_acr.md): Delete one access control record.
- [mutation_delete_custom_role](operations/mutation_delete_custom_role.md): Delete a custom role from the organization.
- [mutation_delete_security_group](operations/mutation_delete_security_group.md): Delete a security group from the organization.
- [mutation_invite_user](operations/mutation_invite_user.md): Invite a user with a role and optional security groups.
- [mutation_remove_org_user](operations/mutation_remove_org_user.md): Remove a user from the current organization.
- [mutation_remove_security_group_member](operations/mutation_remove_security_group_member.md): Remove a user from an RBAC security group.
- [mutation_replace_acr](operations/mutation_replace_acr.md): Replace an access control record in one delete-and-create.
- [mutation_set_org_user_status](operations/mutation_set_org_user_status.md): Enable or disable a user in the current org.
- [mutation_update_custom_role](operations/mutation_update_custom_role.md): Update a custom role's name, description, or permissions.
- [mutation_update_security_group](operations/mutation_update_security_group.md): Update a security group's name or description.
- [mutation_user_action](operations/mutation_user_action.md): Enable or disable a user account.
- [mutation_user_delete](operations/mutation_user_delete.md): Delete a user account and revoke access.
- [mutation_user_invite](operations/mutation_user_invite.md): Invite a user to the organization with a role.
- [mutation_user_remove](operations/mutation_user_remove.md): Remove a user from the org without deleting the account.
- [mutation_user_reset_password](operations/mutation_user_reset_password.md): Send a password-reset email to a user.
- [mutation_user_set_user_role](operations/mutation_user_set_user_role.md): Assign a role such as Owner or Operator.
- [mutation_user_update_user](operations/mutation_user_update_user.md): Update a user's name or email.

### Notifications

- [query_list_notification_configurations](operations/query_list_notification_configurations.md): List notification configurations and their triggers.
- [query_list_notification_logs](operations/query_list_notification_logs.md): List notification delivery events and statuses.
- [mutation_create_notification_configuration](operations/mutation_create_notification_configuration.md): Create a notification channel, scopes, and triggers.
- [mutation_delete_notification_configuration](operations/mutation_delete_notification_configuration.md): Delete a notification configuration by ID.
- [mutation_notify_notification_configuration](operations/mutation_notify_notification_configuration.md): Send a test notification for a configuration.
- [mutation_update_notification_configuration](operations/mutation_update_notification_configuration.md): Update a notification configuration's channel or triggers.

### Jira

- [query_jira_integration](operations/query_jira_integration.md): Get Jira integration summary and connection health.
- [query_jira_integration_setup](operations/query_jira_integration_setup.md): Get the current Jira setup-wizard state.
- [query_jira_project_components](operations/query_jira_project_components.md): List Jira project components for a connected space.
- [query_jira_project_labels](operations/query_jira_project_labels.md): Search Jira labels for a connected space.
- [query_jira_project_sprints](operations/query_jira_project_sprints.md): Search Jira sprints for a connected space.
- [query_jira_project_teams](operations/query_jira_project_teams.md): Search Atlassian Teams for a connected Jira space.
- [query_jira_project_users](operations/query_jira_project_users.md): Search assignable Jira users for a connected space.
- [query_jira_project_versions](operations/query_jira_project_versions.md): List Jira project versions for a connected space.
- [query_jira_space_issue_fields](operations/query_jira_space_issue_fields.md): List creatable fields for a Jira space and issue type.
- [query_jira_space_issue_types](operations/query_jira_space_issue_types.md): List issue types for a connected Jira space.
- [query_jira_space_workflow_config](operations/query_jira_space_workflow_config.md): Get status mappings and workflow config for a Jira space.
- [query_jira_status_mapping_problems](operations/query_jira_status_mapping_problems.md): List status-mapping problems across connected Jira spaces.
- [mutation_jira_integration_add_connected_space](operations/mutation_jira_integration_add_connected_space.md): Connect a Jira space to the integration.
- [mutation_jira_integration_create_issue](operations/mutation_jira_integration_create_issue.md): Create a Jira issue, optionally linked to a finding.
- [mutation_jira_integration_delete_connected_space](operations/mutation_jira_integration_delete_connected_space.md): Disconnect a Jira space from the integration.
- [mutation_jira_integration_disconnect](operations/mutation_jira_integration_disconnect.md): Disconnect the Jira integration from the org.
- [mutation_jira_integration_reconnect](operations/mutation_jira_integration_reconnect.md): Re-enable Jira when OAuth and app install are already done.
- [mutation_jira_integration_set_status_mapping_auto_sync](operations/mutation_jira_integration_set_status_mapping_auto_sync.md): Enable or disable auto-sync for Jira status mappings.
- [mutation_jira_integration_setup_action](operations/mutation_jira_integration_setup_action.md): Run a step in the Jira setup or reconnect flow.
- [mutation_jira_integration_test_connection](operations/mutation_jira_integration_test_connection.md): Check that the Jira integration connection is healthy.
- [mutation_save_jira_space_workflow_config](operations/mutation_save_jira_space_workflow_config.md): Save status mappings and workflow config for a Jira space.

### RiseAI

- [query_caas_availability](operations/query_caas_availability.md): Check whether a RiseAI analysis report is available.
- [query_get_ai_model_data](operations/query_get_ai_model_data.md): Get config and metadata for an AI model integration.
- [query_list_ai_providers](operations/query_list_ai_providers.md): List AI provider integrations and their status.
- [query_rise_ai_analysis_data](operations/query_rise_ai_analysis_data.md): Get the contents of a RiseAI analysis report.
- [query_rise_ai_availability](operations/query_rise_ai_availability.md): Check RiseAI eligibility and status for an asset.
- [mutation_submit_rise_ai_analysis](operations/mutation_submit_rise_ai_analysis.md): Request a RiseAI analysis for an eligible asset.

### Organization

- [query_analytics](operations/query_analytics.md): Get org dashboard risk metrics and chart data.
- [query_org_level_information](operations/query_org_level_information.md): Get org metadata such as last-updated time.
- [query_org_level_settings](operations/query_org_level_settings.md): Get the tenant organization's settings.
- [mutation_update_org_level_settings](operations/mutation_update_org_level_settings.md): Update org settings such as idle session timeout.

