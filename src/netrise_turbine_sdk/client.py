from __future__ import annotations

import os
import time
from collections.abc import Iterable, Iterator
from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING, Any, Dict, Optional

import httpx
from dotenv import find_dotenv, load_dotenv

from netrise_turbine_sdk_graphql import Client as GeneratedClient
from netrise_turbine_sdk_graphql import input_types as inputs

from .pagination import iter_all_pages
from .transport import _build_http_client


class _NonClosingClient(GeneratedClient):
    """Thin proxy that prevents ``with sdk.graphql() as client:`` from
    closing the shared ``httpx.Client`` owned by ``TurbineClient``.

    ``BaseClient.__exit__`` calls ``self.http_client.close()``.  When the
    ``httpx.Client`` is pooled across calls (Tranche A memoization), that
    close kills the connection pool and every subsequent request fails with
    ``RuntimeError: Cannot send a request, as the client has been closed.``

    This subclass overrides ``__exit__`` to be a no-op — lifecycle is
    managed exclusively by ``TurbineClient.close()``.
    """

    def __exit__(
        self, exc_type: object, exc_val: object, exc_tb: object
    ) -> None:
        pass

if TYPE_CHECKING:
    # Import the generated response node types only for type-checking so
    # runtime import cost stays low. Each entry corresponds to an edge node
    # returned by one of the `iter_*` methods below.
    from netrise_turbine_sdk_graphql.query_activity import (
        QueryActivityActivityEdgesNode,
    )
    from netrise_turbine_sdk_graphql.query_asset_group_members import (
        QueryAssetGroupMembersAssetGroupMembersEdgesNode,
    )
    from netrise_turbine_sdk_graphql.query_asset_groups import (
        QueryAssetGroupsAssetGroupsEdgesNode,
    )
    from netrise_turbine_sdk_graphql.query_assets_overview import (
        QueryAssetsOverviewAssetsOverviewEdgesNode,
    )
    from netrise_turbine_sdk_graphql.query_assets_relay import (
        QueryAssetsRelayAssetsRelayEdgesNode,
    )
    from netrise_turbine_sdk_graphql.query_assets_relay_lite import (
        QueryAssetsRelayLiteAssetsRelayEdgesNode,
    )
    from netrise_turbine_sdk_graphql.query_assets_relay_summary import (
        QueryAssetsRelaySummaryAssetsRelayEdgesNode,
    )
    from netrise_turbine_sdk_graphql.query_binary_protections import (
        QueryBinaryProtectionsBinaryProtectionsEdgesNode,
    )
    from netrise_turbine_sdk_graphql.query_certificates import (
        QueryCertificatesCertificatesEdgesNode,
    )
    from netrise_turbine_sdk_graphql.query_credentials import (
        QueryCredentialsCredentialsEdgesNode,
    )
    from netrise_turbine_sdk_graphql.query_dependencies import (
        QueryDependenciesDependenciesEdgesNode,
    )
    from netrise_turbine_sdk_graphql.query_dependencies_lite import (
        QueryDependenciesLiteDependenciesEdgesNode,
    )
    from netrise_turbine_sdk_graphql.query_detailed_vulnerabilities import (
        QueryDetailedVulnerabilitiesDetailedVulnerabilitiesEdgesNode,
    )
    from netrise_turbine_sdk_graphql.query_detailed_vulnerabilities_lite import (
        QueryDetailedVulnerabilitiesLiteDetailedVulnerabilitiesEdgesNode,
    )
    from netrise_turbine_sdk_graphql.query_grouped_dependencies import (
        QueryGroupedDependenciesGroupedDependenciesEdgesNode,
    )
    from netrise_turbine_sdk_graphql.query_hashes import (
        QueryHashesHashesEdgesNode,
    )
    from netrise_turbine_sdk_graphql.query_license_issues import (
        QueryLicenseIssuesLicenseIssuesEdgesNode,
    )
    from netrise_turbine_sdk_graphql.query_list_asset_crypto_libraries import (
        QueryListAssetCryptoLibrariesListAssetCryptoLibrariesEdgesNode,
    )
    from netrise_turbine_sdk_graphql.query_misconfigurations import (
        QueryMisconfigurationsMisconfigurationsEdgesNode,
    )
    from netrise_turbine_sdk_graphql.query_misconfigurations_lite import (
        QueryMisconfigurationsLiteMisconfigurationsEdgesNode,
    )
    from netrise_turbine_sdk_graphql.query_private_keys import (
        QueryPrivateKeysPrivateKeysEdgesNode,
    )
    from netrise_turbine_sdk_graphql.query_public_keys import (
        QueryPublicKeysPublicKeysEdgesNode,
    )
    from netrise_turbine_sdk_graphql.query_secrets import (
        QuerySecretsSecretsEdgesNode,
    )
    from netrise_turbine_sdk_graphql.query_users import (
        QueryUsersUsersEdgesNode,
    )
    from netrise_turbine_sdk_graphql.query_vulnerabilities import (
        QueryVulnerabilitiesVulnerabilitiesEdgesNode,
    )
    from netrise_turbine_sdk_graphql.query_vulnerabilities_lite import (
        QueryVulnerabilitiesLiteVulnerabilitiesEdgesNode,
    )
    from netrise_turbine_sdk_graphql.query_vulnerabilities_overview import (
        QueryVulnerabilitiesOverviewVulnerabilitiesOverviewEdgesNode,
    )


_DEFAULT_RETRY_STATUSES: tuple[int, ...] = (429, 502, 503, 504)


@dataclass(frozen=True)
class TurbineClientConfig:
    endpoint: str

    # Client credentials
    domain: Optional[str] = None
    client_id: Optional[str] = None
    client_secret: Optional[str] = None
    audience: Optional[str] = None
    organization_id: Optional[str] = None

    # Manual token override
    turbine_api_token: Optional[str] = None

    @staticmethod
    def from_env(load_env_file: bool = True) -> "TurbineClientConfig":
        """Load config from environment variables.

        If `load_env_file` is True, automatically loads a `.env` file from:
        - Current working directory (most common)
        - Parent directories (walks up the directory tree)

        Environment variables can also be set directly without a `.env` file.
        Set `load_env_file=False` to disable automatic `.env` file loading.
        """
        if load_env_file:
            # Prioritize .env file in current working directory
            # This ensures local .env files take precedence over parent directories
            current_dir_env = Path.cwd() / ".env"
            if current_dir_env.exists():
                load_dotenv(current_dir_env, override=False)
            else:
                # If no .env in current directory, search parent directories
                dotenv_path = find_dotenv(usecwd=True)
                if dotenv_path:
                    load_dotenv(dotenv_path, override=False)
                else:
                    # Fallback to default behavior if find_dotenv doesn't find anything
                    load_dotenv(override=False)

        endpoint = (os.getenv("endpoint") or "").strip()
        if not endpoint:
            raise ValueError(
                "endpoint is required (e.g. https://apollo.turbine.netrise.io/graphql/v3)"
            )

        return TurbineClientConfig(
            endpoint=endpoint,
            domain=_strip_or_none(os.getenv("domain")),
            client_id=_strip_or_none(os.getenv("client_id")),
            client_secret=_strip_or_none(os.getenv("client_secret")),
            audience=_strip_or_none(os.getenv("audience")),
            organization_id=_strip_or_none(os.getenv("organization_id")),
            turbine_api_token=_strip_or_none(os.getenv("TURBINE_API_TOKEN")),
        )


class TurbineClient:
    """Sync-first Turbine GraphQL client.

    - Uses ``TURBINE_API_TOKEN`` if provided.
    - Otherwise uses client credentials to fetch a token.

    Underlying request execution is provided by the generated client from
    ``ariadne-codegen``. The underlying ``httpx.Client`` is built with a
    composable transport stack that adds retries (on by default), and,
    when requested, concurrency and rate-limit guards.

    Args:
        config: Endpoint + auth configuration.
        timeout: Per-request timeout in seconds.
        upload_timeout: Per-request timeout in seconds for file uploads.
            Defaults to 300 (5 minutes) to accommodate large firmware images.
        httpx_client: Pre-built ``httpx.Client`` to use verbatim. When provided
            the transport-stack kwargs below are ignored: the caller is
            responsible for any retry / concurrency / rate-limit behavior.
        max_retries: Number of retry attempts for failed requests. Set to 0
            to disable retries. Default 5.
        backoff_factor: Exponential backoff base (with jitter). ``sleep =
            backoff_factor * 2 ** attempt * uniform(0, 1)``. Default 0.5.
        retry_statuses: HTTP status codes that trigger a retry. Default
            ``(429, 502, 503, 504)``. ``Retry-After`` is honored when present.
        max_in_flight: Cap on concurrent in-flight requests. ``None`` (default)
            disables concurrency limiting.
        rate_limit_per_second: Max requests per second across this client.
            ``None`` disables per-second rate limiting.
        rate_limit_per_minute: Max requests per minute across this client.
            ``None`` disables per-minute rate limiting.
    """

    def __init__(
        self,
        config: TurbineClientConfig,
        *,
        timeout: float = 30.0,
        upload_timeout: float = 300.0,
        httpx_client: Optional[httpx.Client] = None,
        max_retries: int = 5,
        backoff_factor: float = 0.5,
        retry_statuses: Iterable[int] = _DEFAULT_RETRY_STATUSES,
        max_in_flight: Optional[int] = None,
        rate_limit_per_second: Optional[float] = None,
        rate_limit_per_minute: Optional[float] = None,
    ) -> None:
        self._config = config
        self._timeout = timeout
        self._upload_timeout = upload_timeout
        self._httpx_client = httpx_client
        self._owns_httpx_client = httpx_client is None

        self._max_retries = max_retries
        self._backoff_factor = backoff_factor
        self._retry_statuses = tuple(retry_statuses)
        self._max_in_flight = max_in_flight
        self._rate_limit_per_second = rate_limit_per_second
        self._rate_limit_per_minute = rate_limit_per_minute

        self._cached_token: Optional[str] = None
        self._cached_token_expires_at: float = 0.0

        # Built lazily on the first graphql() call so construction stays cheap
        # and tests that never touch the network can build a TurbineClient
        # without triggering the transport stack setup.
        self._graphql_client: Optional[GeneratedClient] = None
        self._util_http_client: Optional[httpx.Client] = None
        self._closed = False

    @property
    def config(self) -> TurbineClientConfig:
        return self._config

    @property
    def _util_http(self) -> httpx.Client:
        """Lazily-built plain ``httpx.Client`` for non-GraphQL HTTP work.

        Used for auth token fetches and file uploads. Separate from the
        GraphQL transport-stack client because these requests do not need
        retry / rate-limit / concurrency wrappers, and uploads override
        the timeout per-request via ``self._upload_timeout``.
        """
        if self._util_http_client is None:
            self._util_http_client = httpx.Client(timeout=self._timeout)
        return self._util_http_client

    def close(self) -> None:
        """Close the underlying httpx connection pools.

        Idempotent. Safe to call multiple times. Only closes the httpx
        client if this ``TurbineClient`` owns it (i.e. was constructed
        without a caller-supplied ``httpx_client``).
        """
        if self._closed:
            return
        self._closed = True
        if self._graphql_client is not None and self._owns_httpx_client:
            try:
                self._graphql_client.http_client.close()
            except Exception:
                pass
        self._graphql_client = None
        if self._util_http_client is not None:
            try:
                self._util_http_client.close()
            except Exception:
                pass
            self._util_http_client = None

    def __del__(self) -> None:
        try:
            self.close()
        except Exception:
            pass

    def __enter__(self) -> "TurbineClient":
        return self

    def __exit__(
        self, exc_type: object, exc_val: object, exc_tb: object
    ) -> None:
        self.close()

    def _get_auth_header(self) -> Dict[str, str]:
        token = self._get_token()
        if not token.startswith("Bearer "):
            token = f"Bearer {token}"
        return {"Authorization": token}

    def _get_token(self) -> str:
        # 1) Manual token override
        if self._config.turbine_api_token:
            return self._config.turbine_api_token

        # 2) Cached token
        now = time.time()
        if self._cached_token and now < self._cached_token_expires_at:
            return self._cached_token

        # 3) Fetch via client credentials
        token, expires_in = _fetch_token(
            http_client=self._util_http,
            domain=self._config.domain,
            client_id=self._config.client_id,
            client_secret=self._config.client_secret,
            audience=self._config.audience,
            organization_id=self._config.organization_id,
        )

        # Cache with a small safety buffer.
        self._cached_token = token
        self._cached_token_expires_at = time.time() + max(0, expires_in - 30)
        return token

    def graphql(self) -> GeneratedClient:
        """Return the memoized generated client, refreshing auth on each call.

        The underlying ``httpx.Client`` is built once on first call and reused
        for every subsequent call, so connection pooling actually kicks in
        across queries.

        When ``TurbineClient`` owns the httpx client the returned instance is
        a ``_NonClosingClient`` whose ``__exit__`` is a no-op, so
        ``with sdk.graphql() as client:`` is safe to use repeatedly without
        closing the shared connection pool. Connection lifecycle is managed
        exclusively by ``TurbineClient.close()``.

        When the caller supplied their own ``httpx_client=``, a standard
        ``GeneratedClient`` is returned and ``__exit__`` behaves normally.
        """
        if self._closed:
            raise RuntimeError(
                "TurbineClient is closed; construct a new instance to issue more queries"
            )

        headers = self._get_auth_header()

        if self._graphql_client is not None:
            self._graphql_client.http_client.headers.update(headers)
            return self._graphql_client

        if self._httpx_client is not None:
            self._httpx_client.headers.update(headers)
            http_client = self._httpx_client
        else:
            http_client = _build_http_client(
                timeout=self._timeout,
                headers=headers,
                max_retries=self._max_retries,
                backoff_factor=self._backoff_factor,
                retry_statuses=self._retry_statuses,
                max_in_flight=self._max_in_flight,
                rate_limit_per_second=self._rate_limit_per_second,
                rate_limit_per_minute=self._rate_limit_per_minute,
            )

        client_cls = GeneratedClient if not self._owns_httpx_client else _NonClosingClient
        self._graphql_client = client_cls(
            url=self._config.endpoint,
            http_client=http_client,
        )
        return self._graphql_client

    # --- Paginated iterators -------------------------------------------------
    #
    # Each method below is a thin wrapper around ``iter_all_pages`` that:
    #   1. reconstructs the operation's input object with a fresh cursor for
    #      each page (so existing filter / sort kwargs flow through unchanged),
    #   2. issues the query via the memoized generated client,
    #   3. returns an iterator of the operation's node type.
    #
    # Every method has backward-compatible defaults so users can drop in a
    # call site without touching existing arguments.

    def iter_activity(
        self,
        *,
        asset_id: str,
        page_size: int = 100,
        max_pages: Optional[int] = None,
    ) -> "Iterator[QueryActivityActivityEdgesNode]":
        def fetch(cursor: inputs.Cursor) -> Any:
            return self.graphql().query_activity(
                activity_args=inputs.ActivityInput(
                    assetId=asset_id,
                    cursor=cursor,
                )
            ).activity

        return iter_all_pages(fetch, page_size=page_size, max_pages=max_pages)

    def iter_asset_group_members(
        self,
        *,
        group_id: str,
        sort: Optional["inputs.AssetsSort"] = None,
        page_size: int = 100,
        max_pages: Optional[int] = None,
    ) -> "Iterator[QueryAssetGroupMembersAssetGroupMembersEdgesNode]":
        def fetch(cursor: inputs.Cursor) -> Any:
            return self.graphql().query_asset_group_members(
                asset_group_members_args=inputs.AssetGroupMembersInput(
                    groupId=group_id,
                    cursor=cursor,
                    sort=sort,
                )
            ).asset_group_members

        return iter_all_pages(fetch, page_size=page_size, max_pages=max_pages)

    def iter_asset_groups(
        self,
        *,
        filter: Optional[str] = None,
        sort: Optional["inputs.AssetGroupsSort"] = None,
        page_size: int = 100,
        max_pages: Optional[int] = None,
    ) -> "Iterator[QueryAssetGroupsAssetGroupsEdgesNode]":
        def fetch(cursor: inputs.Cursor) -> Any:
            return self.graphql().query_asset_groups(
                asset_groups_args=inputs.AssetGroupsInput(
                    cursor=cursor,
                    filter=filter,
                    sort=sort,
                )
            ).asset_groups

        return iter_all_pages(fetch, page_size=page_size, max_pages=max_pages)

    def iter_assets_overview(
        self,
        *,
        asset_group_ids: Optional[list[str]] = None,
        filter: Optional["inputs.AssetOverviewFilter"] = None,
        sort: Optional["inputs.AssetOverviewSort"] = None,
        page_size: int = 100,
        max_pages: Optional[int] = None,
    ) -> "Iterator[QueryAssetsOverviewAssetsOverviewEdgesNode]":
        def fetch(cursor: inputs.Cursor) -> Any:
            return self.graphql().query_assets_overview(
                assets_overview_args=inputs.AssetOverviewInput(
                    assetGroupIds=asset_group_ids,
                    cursor=cursor,
                    filter=filter,
                    sort=sort,
                )
            ).assets_overview

        return iter_all_pages(fetch, page_size=page_size, max_pages=max_pages)

    def iter_assets_relay(
        self,
        *,
        filter: Optional["inputs.AssetsFilter"] = None,
        sort: Optional["inputs.AssetsSort"] = None,
        page_size: int = 100,
        max_pages: Optional[int] = None,
    ) -> "Iterator[QueryAssetsRelayAssetsRelayEdgesNode]":
        def fetch(cursor: inputs.Cursor) -> Any:
            return self.graphql().query_assets_relay(
                assets_relay_args=inputs.AssetsRelayInput(
                    cursor=cursor,
                    filter=filter,
                    sort=sort,
                )
            ).assets_relay

        return iter_all_pages(fetch, page_size=page_size, max_pages=max_pages)

    def iter_binary_protections(
        self,
        *,
        asset_id: str,
        filter: Optional["inputs.BinaryProtectionsFilter"] = None,
        sort: Optional["inputs.BinaryProtectionsSort"] = None,
        page_size: int = 100,
        max_pages: Optional[int] = None,
    ) -> "Iterator[QueryBinaryProtectionsBinaryProtectionsEdgesNode]":
        def fetch(cursor: inputs.Cursor) -> Any:
            return self.graphql().query_binary_protections(
                binary_protections_args=inputs.BinaryProtectionsInput(
                    assetId=asset_id,
                    cursor=cursor,
                    filter=filter,
                    sort=sort,
                )
            ).binary_protections

        return iter_all_pages(fetch, page_size=page_size, max_pages=max_pages)

    def iter_certificates(
        self,
        *,
        asset_id: str,
        filter: Optional["inputs.ListCertificatesFilter"] = None,
        sort: Optional["inputs.ListCertificatesSort"] = None,
        page_size: int = 100,
        max_pages: Optional[int] = None,
    ) -> "Iterator[QueryCertificatesCertificatesEdgesNode]":
        def fetch(cursor: inputs.Cursor) -> Any:
            return self.graphql().query_certificates(
                certificates_args=inputs.CertificatesInput(
                    assetId=asset_id,
                    cursor=cursor,
                    filter=filter,
                    sort=sort,
                )
            ).certificates

        return iter_all_pages(fetch, page_size=page_size, max_pages=max_pages)

    def iter_credentials(
        self,
        *,
        asset_id: str,
        filter: Optional["inputs.CredentialsFilter"] = None,
        sort: Optional["inputs.CredentialsSort"] = None,
        page_size: int = 100,
        max_pages: Optional[int] = None,
    ) -> "Iterator[QueryCredentialsCredentialsEdgesNode]":
        def fetch(cursor: inputs.Cursor) -> Any:
            return self.graphql().query_credentials(
                credentials_args=inputs.CredentialsInput(
                    assetId=asset_id,
                    cursor=cursor,
                    filter=filter,
                    sort=sort,
                )
            ).credentials

        return iter_all_pages(fetch, page_size=page_size, max_pages=max_pages)

    def iter_dependencies(
        self,
        *,
        composed_asset_id: str,
        filter: Optional["inputs.DependencyFilter"] = None,
        sort: Optional["inputs.DependencySort"] = None,
        page_size: int = 100,
        max_pages: Optional[int] = None,
    ) -> "Iterator[QueryDependenciesDependenciesEdgesNode]":
        def fetch(cursor: inputs.Cursor) -> Any:
            return self.graphql().query_dependencies(
                dependencies_args=inputs.DependencyInput(
                    composedAssetId=composed_asset_id,
                    cursor=cursor,
                    filter=filter,
                    sort=sort,
                )
            ).dependencies

        return iter_all_pages(fetch, page_size=page_size, max_pages=max_pages)

    def iter_detailed_vulnerabilities(
        self,
        *,
        asset_id: str,
        filter: Optional["inputs.DetailedVulnerabilityFilter"] = None,
        page_size: int = 100,
        max_pages: Optional[int] = None,
    ) -> "Iterator[QueryDetailedVulnerabilitiesDetailedVulnerabilitiesEdgesNode]":
        def fetch(cursor: inputs.Cursor) -> Any:
            return self.graphql().query_detailed_vulnerabilities(
                detailed_vulnerabilities_args=inputs.PaginatedDetailedVulnerabilitiesInput(
                    assetId=asset_id,
                    cursor=cursor,
                    filter=filter,
                )
            ).detailed_vulnerabilities

        return iter_all_pages(fetch, page_size=page_size, max_pages=max_pages)

    def iter_grouped_dependencies(
        self,
        *,
        composed_asset_id: str,
        filter: Optional["inputs.GroupedDependencyFilter"] = None,
        sort: Optional["inputs.GroupedDependencySort"] = None,
        grouped_by: Optional[Any] = None,
        page_size: int = 100,
        max_pages: Optional[int] = None,
    ) -> "Iterator[QueryGroupedDependenciesGroupedDependenciesEdgesNode]":
        def fetch(cursor: inputs.Cursor) -> Any:
            return self.graphql().query_grouped_dependencies(
                grouped_dependencies_args=inputs.GroupedDependenciesInput(
                    composedAssetId=composed_asset_id,
                    cursor=cursor,
                    filter=filter,
                    sort=sort,
                    groupedBy=grouped_by,
                )
            ).grouped_dependencies

        return iter_all_pages(fetch, page_size=page_size, max_pages=max_pages)

    def iter_hashes(
        self,
        *,
        asset_id: str,
        filter: Optional["inputs.HashesFilter"] = None,
        sort: Optional["inputs.HashesSort"] = None,
        page_size: int = 100,
        max_pages: Optional[int] = None,
    ) -> "Iterator[QueryHashesHashesEdgesNode]":
        def fetch(cursor: inputs.Cursor) -> Any:
            return self.graphql().query_hashes(
                hashes_args=inputs.HashesInput(
                    assetId=asset_id,
                    cursor=cursor,
                    filter=filter,
                    sort=sort,
                )
            ).hashes

        return iter_all_pages(fetch, page_size=page_size, max_pages=max_pages)

    def iter_license_issues(
        self,
        *,
        asset_id: str,
        filter: Optional["inputs.LicenseIssuesFilter"] = None,
        sort: Optional["inputs.LicenseIssuesSort"] = None,
        page_size: int = 100,
        max_pages: Optional[int] = None,
    ) -> "Iterator[QueryLicenseIssuesLicenseIssuesEdgesNode]":
        def fetch(cursor: inputs.Cursor) -> Any:
            return self.graphql().query_license_issues(
                license_issues_args=inputs.LicenseIssuesInput(
                    assetId=asset_id,
                    cursor=cursor,
                    filter=filter,
                    sort=sort,
                )
            ).license_issues

        return iter_all_pages(fetch, page_size=page_size, max_pages=max_pages)

    def iter_list_asset_crypto_libraries(
        self,
        *,
        asset_id: str,
        filter: Optional[str] = None,
        sort: Optional["inputs.ListCryptoLibrariesSort"] = None,
        page_size: int = 100,
        max_pages: Optional[int] = None,
    ) -> (
        "Iterator[QueryListAssetCryptoLibrariesListAssetCryptoLibrariesEdgesNode]"
    ):
        def fetch(cursor: inputs.Cursor) -> Any:
            return self.graphql().query_list_asset_crypto_libraries(
                list_asset_crypto_libraries_args=inputs.ListAssetCryptoLibrariesInput(
                    assetId=asset_id,
                    cursor=cursor,
                    filter=filter,
                    sort=sort,
                )
            ).list_asset_crypto_libraries

        return iter_all_pages(fetch, page_size=page_size, max_pages=max_pages)

    def iter_misconfigurations(
        self,
        *,
        asset_id: str,
        filter: Optional["inputs.MisconfigurationsFilter"] = None,
        sort: Optional["inputs.MisconfigurationsSort"] = None,
        page_size: int = 100,
        max_pages: Optional[int] = None,
    ) -> "Iterator[QueryMisconfigurationsMisconfigurationsEdgesNode]":
        def fetch(cursor: inputs.Cursor) -> Any:
            return self.graphql().query_misconfigurations(
                misconfigurations_args=inputs.MisconfigurationsInput(
                    assetId=asset_id,
                    cursor=cursor,
                    filter=filter,
                    sort=sort,
                )
            ).misconfigurations

        return iter_all_pages(fetch, page_size=page_size, max_pages=max_pages)

    def iter_private_keys(
        self,
        *,
        asset_id: str,
        filter: Optional["inputs.ListPrivateKeysFilter"] = None,
        sort: Optional["inputs.ListPrivateKeysSort"] = None,
        page_size: int = 100,
        max_pages: Optional[int] = None,
    ) -> "Iterator[QueryPrivateKeysPrivateKeysEdgesNode]":
        def fetch(cursor: inputs.Cursor) -> Any:
            return self.graphql().query_private_keys(
                private_keys_args=inputs.PrivateKeysInput(
                    assetId=asset_id,
                    cursor=cursor,
                    filter=filter,
                    sort=sort,
                )
            ).private_keys

        return iter_all_pages(fetch, page_size=page_size, max_pages=max_pages)

    def iter_public_keys(
        self,
        *,
        asset_id: str,
        filter: Optional["inputs.ListPublicKeysFilter"] = None,
        sort: Optional["inputs.ListPublicKeysSort"] = None,
        page_size: int = 100,
        max_pages: Optional[int] = None,
    ) -> "Iterator[QueryPublicKeysPublicKeysEdgesNode]":
        def fetch(cursor: inputs.Cursor) -> Any:
            return self.graphql().query_public_keys(
                public_keys_args=inputs.PublicKeysInput(
                    assetId=asset_id,
                    cursor=cursor,
                    filter=filter,
                    sort=sort,
                )
            ).public_keys

        return iter_all_pages(fetch, page_size=page_size, max_pages=max_pages)

    def iter_secrets(
        self,
        *,
        asset_id: str,
        filter: Optional["inputs.SecretsFilter"] = None,
        sort: Optional["inputs.SecretsSort"] = None,
        page_size: int = 100,
        max_pages: Optional[int] = None,
    ) -> "Iterator[QuerySecretsSecretsEdgesNode]":
        def fetch(cursor: inputs.Cursor) -> Any:
            return self.graphql().query_secrets(
                secrets_args=inputs.SecretsInput(
                    assetId=asset_id,
                    cursor=cursor,
                    filter=filter,
                    sort=sort,
                )
            ).secrets

        return iter_all_pages(fetch, page_size=page_size, max_pages=max_pages)

    def iter_users(
        self,
        *,
        page_size: int = 100,
        max_pages: Optional[int] = None,
    ) -> "Iterator[QueryUsersUsersEdgesNode]":
        def fetch(cursor: inputs.Cursor) -> Any:
            return self.graphql().query_users(
                users_args=inputs.UsersInput(cursor=cursor)
            ).users

        return iter_all_pages(fetch, page_size=page_size, max_pages=max_pages)

    def iter_vulnerabilities(
        self,
        *,
        asset_id: str,
        filter: Optional["inputs.VulnerabilityFilter"] = None,
        sort: Optional["inputs.VulnerabilitySort"] = None,
        page_size: int = 100,
        max_pages: Optional[int] = None,
    ) -> "Iterator[QueryVulnerabilitiesVulnerabilitiesEdgesNode]":
        def fetch(cursor: inputs.Cursor) -> Any:
            return self.graphql().query_vulnerabilities(
                vulnerabilities_args=inputs.PaginatedVulnerabilitiesInput(
                    assetId=asset_id,
                    cursor=cursor,
                    filter=filter,
                    sort=sort,
                )
            ).vulnerabilities

        return iter_all_pages(fetch, page_size=page_size, max_pages=max_pages)

    def iter_vulnerabilities_overview(
        self,
        *,
        asset_group_ids: Optional[list[str]] = None,
        filter: Optional["inputs.VulnerabilityOverviewFilter"] = None,
        sort: Optional["inputs.VulnerabilityOverviewSort"] = None,
        page_size: int = 100,
        max_pages: Optional[int] = None,
    ) -> (
        "Iterator[QueryVulnerabilitiesOverviewVulnerabilitiesOverviewEdgesNode]"
    ):
        def fetch(cursor: inputs.Cursor) -> Any:
            return self.graphql().query_vulnerabilities_overview(
                vulnerabilities_overview_args=inputs.VulnerabilityOverviewInput(
                    assetGroupIds=asset_group_ids,
                    cursor=cursor,
                    filter=filter,
                    sort=sort,
                )
            ).vulnerabilities_overview

        return iter_all_pages(fetch, page_size=page_size, max_pages=max_pages)

    # --- Lite / Summary paginators -----------------------------------------
    # These mirror the full-weight `iter_*` methods above but trim the
    # response payload by ~70-80%. Use them when you only need top-level
    # identifiers, severity rollups, or counts and don't want to pay for
    # deeply-nested exploit / remediation / correlation data. See the
    # "Reducing response size" section of the README for guidance on when
    # Lite vs full is appropriate.

    def iter_assets_relay_lite(
        self,
        *,
        filter: Optional["inputs.AssetsFilter"] = None,
        sort: Optional["inputs.AssetsSort"] = None,
        page_size: int = 100,
        max_pages: Optional[int] = None,
    ) -> "Iterator[QueryAssetsRelayLiteAssetsRelayEdgesNode]":
        def fetch(cursor: inputs.Cursor) -> Any:
            return self.graphql().query_assets_relay_lite(
                assets_relay_args=inputs.AssetsRelayInput(
                    cursor=cursor,
                    filter=filter,
                    sort=sort,
                )
            ).assets_relay

        return iter_all_pages(fetch, page_size=page_size, max_pages=max_pages)

    def iter_assets_relay_summary(
        self,
        *,
        filter: Optional["inputs.AssetsFilter"] = None,
        sort: Optional["inputs.AssetsSort"] = None,
        page_size: int = 100,
        max_pages: Optional[int] = None,
    ) -> "Iterator[QueryAssetsRelaySummaryAssetsRelayEdgesNode]":
        def fetch(cursor: inputs.Cursor) -> Any:
            return self.graphql().query_assets_relay_summary(
                assets_relay_args=inputs.AssetsRelayInput(
                    cursor=cursor,
                    filter=filter,
                    sort=sort,
                )
            ).assets_relay

        return iter_all_pages(fetch, page_size=page_size, max_pages=max_pages)

    def iter_vulnerabilities_lite(
        self,
        *,
        asset_id: str,
        filter: Optional["inputs.VulnerabilityFilter"] = None,
        sort: Optional["inputs.VulnerabilitySort"] = None,
        page_size: int = 100,
        max_pages: Optional[int] = None,
    ) -> "Iterator[QueryVulnerabilitiesLiteVulnerabilitiesEdgesNode]":
        def fetch(cursor: inputs.Cursor) -> Any:
            return self.graphql().query_vulnerabilities_lite(
                vulnerabilities_args=inputs.PaginatedVulnerabilitiesInput(
                    assetId=asset_id,
                    cursor=cursor,
                    filter=filter,
                    sort=sort,
                )
            ).vulnerabilities

        return iter_all_pages(fetch, page_size=page_size, max_pages=max_pages)

    def iter_dependencies_lite(
        self,
        *,
        composed_asset_id: str,
        filter: Optional["inputs.DependencyFilter"] = None,
        sort: Optional["inputs.DependencySort"] = None,
        page_size: int = 100,
        max_pages: Optional[int] = None,
    ) -> "Iterator[QueryDependenciesLiteDependenciesEdgesNode]":
        def fetch(cursor: inputs.Cursor) -> Any:
            return self.graphql().query_dependencies_lite(
                dependencies_args=inputs.DependencyInput(
                    composedAssetId=composed_asset_id,
                    cursor=cursor,
                    filter=filter,
                    sort=sort,
                )
            ).dependencies

        return iter_all_pages(fetch, page_size=page_size, max_pages=max_pages)

    def iter_misconfigurations_lite(
        self,
        *,
        asset_id: str,
        filter: Optional["inputs.MisconfigurationsFilter"] = None,
        sort: Optional["inputs.MisconfigurationsSort"] = None,
        page_size: int = 100,
        max_pages: Optional[int] = None,
    ) -> "Iterator[QueryMisconfigurationsLiteMisconfigurationsEdgesNode]":
        def fetch(cursor: inputs.Cursor) -> Any:
            return self.graphql().query_misconfigurations_lite(
                misconfigurations_args=inputs.MisconfigurationsInput(
                    assetId=asset_id,
                    cursor=cursor,
                    filter=filter,
                    sort=sort,
                )
            ).misconfigurations

        return iter_all_pages(fetch, page_size=page_size, max_pages=max_pages)

    def iter_detailed_vulnerabilities_lite(
        self,
        *,
        asset_id: str,
        filter: Optional["inputs.DetailedVulnerabilityFilter"] = None,
        page_size: int = 100,
        max_pages: Optional[int] = None,
    ) -> "Iterator[QueryDetailedVulnerabilitiesLiteDetailedVulnerabilitiesEdgesNode]":
        def fetch(cursor: inputs.Cursor) -> Any:
            return self.graphql().query_detailed_vulnerabilities_lite(
                detailed_vulnerabilities_args=inputs.PaginatedDetailedVulnerabilitiesInput(
                    assetId=asset_id,
                    cursor=cursor,
                    filter=filter,
                )
            ).detailed_vulnerabilities

        return iter_all_pages(fetch, page_size=page_size, max_pages=max_pages)

    # --- File / asset uploads ------------------------------------------------

    def upload_asset(
        self,
        file_path: str | Path,
        *,
        submit_args: Optional[Any] = None,
        name: Optional[str] = None,
    ) -> Any:
        """Upload a file and submit it as an asset.

        Args:
            file_path: Path to the file to upload.
            submit_args: Optional SubmitAssetInput with metadata (name, manufacturer,
                model, version, type, etc.). Import from netrise_turbine_sdk_graphql.input_types.
            name: Optional display name for the asset. Defaults to the filename.
                Ignored if submit_args.name is already set.

        Returns:
            MutationAssetSubmit response containing asset info and upload details.

        Example:
            >>> from netrise_turbine_sdk_graphql.input_types import SubmitAssetInput
            >>> sdk = TurbineClient(TurbineClientConfig.from_env())
            >>> resp = sdk.upload_asset("firmware.bin", name="My Firmware v1.0")
            >>> print(resp.asset.submit.asset.id)
        """
        from netrise_turbine_sdk_graphql.input_types import SubmitAssetInput

        path = Path(file_path)
        if not path.exists():
            raise FileNotFoundError(f"File not found: {path}")

        file_name = path.name

        if submit_args is None:
            submit_args = SubmitAssetInput(name=name or file_name)
        elif name and submit_args.name is None:
            submit_args = SubmitAssetInput(
                **{**submit_args.model_dump(exclude_unset=True), "name": name}
            )

        client = self.graphql()
        resp = client.mutation_asset_submit(
            asset_submit_file_name=file_name,
            asset_submit_args=submit_args,
        )

        upload_url = resp.asset.submit.upload_url

        with open(path, "rb") as f:
            put_resp = self._util_http.put(
                upload_url,
                content=f,
                timeout=self._upload_timeout,
            )
            put_resp.raise_for_status()

        return resp

    def upload_assets(
        self,
        directory: str | Path,
        *,
        submit_args_fn: Optional[Any] = None,
    ) -> list[tuple[Path, Any]]:
        """Upload all files in a directory as assets.

        Args:
            directory: Path to directory containing files to upload.
            submit_args_fn: Optional callable that takes a file Path and returns
                a SubmitAssetInput for that file. If not provided, each file is
                uploaded with its filename as the asset name.

        Returns:
            List of (Path, MutationAssetSubmit) tuples for successfully uploaded files.
            Failed uploads are printed to stderr but do not stop the batch.

        Example:
            >>> from netrise_turbine_sdk_graphql.input_types import SubmitAssetInput
            >>> sdk = TurbineClient(TurbineClientConfig.from_env())
            >>>
            >>> # Simple: upload all files with default names
            >>> results = sdk.upload_assets("./firmware_images/")
            >>>
            >>> # Custom: add metadata per file
            >>> def make_args(path):
            ...     return SubmitAssetInput(
            ...         name=f"chainguard-{path.name}",
            ...         product="chainguard",
            ...     )
            >>> results = sdk.upload_assets("./images/", submit_args_fn=make_args)
        """
        import sys

        dir_path = Path(directory)
        if not dir_path.exists():
            raise FileNotFoundError(f"Directory not found: {dir_path}")
        if not dir_path.is_dir():
            raise NotADirectoryError(f"Not a directory: {dir_path}")

        files = [f for f in dir_path.iterdir() if f.is_file()]
        if not files:
            print(f"No files found in {dir_path}", file=sys.stderr)
            return []

        results: list[tuple[Path, Any]] = []

        for file_path in files:
            try:
                submit_args = None
                if submit_args_fn is not None:
                    submit_args = submit_args_fn(file_path)

                resp = self.upload_asset(file_path, submit_args=submit_args)
                results.append((file_path, resp))
                print(f"[OK] Uploaded: {file_path.name}")

            except Exception as e:
                print(f"[FAILED] {file_path.name}: {e}", file=sys.stderr)

        return results


def _strip_or_none(v: Optional[str]) -> Optional[str]:
    if v is None:
        return None
    v = v.strip()
    return v or None


def _fetch_token(
    *,
    http_client: httpx.Client,
    domain: Optional[str],
    client_id: Optional[str],
    client_secret: Optional[str],
    audience: Optional[str],
    organization_id: Optional[str],
) -> tuple[str, int]:
    if not domain:
        raise ValueError("domain is required when TURBINE_API_TOKEN is not set")
    if not client_id or not client_secret:
        raise ValueError(
            "client_id and client_secret are required when TURBINE_API_TOKEN is not set"
        )
    if not audience:
        raise ValueError("audience is required when TURBINE_API_TOKEN is not set")

    domain = domain.rstrip("/")
    token_url = f"{domain}/oauth/token"

    payload: Dict[str, Any] = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret,
        "audience": audience,
    }

    if organization_id:
        payload["organization"] = organization_id

    r = http_client.post(token_url, json=payload)
    r.raise_for_status()
    data = r.json()

    token = data.get("access_token")
    expires_in = int(data.get("expires_in", 3600))

    if not token:
        raise RuntimeError(f"Token response missing access_token: {data}")

    return token if token.startswith("Bearer ") else f"Bearer {token}", expires_in
