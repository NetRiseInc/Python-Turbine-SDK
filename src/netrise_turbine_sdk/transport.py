"""HTTP transport stack for `TurbineClient`.

Layered transports (outer -> inner):

    RateLimitTransport -> ConcurrencyTransport -> RetryTransport -> HTTPTransport

Retries sit closest to the wire so that rate-limit and concurrency budgets are
not spent on retry attempts. Each layer is a no-op when its config is absent,
so the simplest configuration collapses to a plain ``httpx.HTTPTransport``.

The ``httpx_retries`` and ``pyrate_limiter`` imports are lazy: they are only
pulled in when the corresponding feature is enabled, so the SDK can be
imported even if those packages are missing at runtime (they are declared as
hard deps in ``pyproject.toml`` but keeping the imports lazy also makes the
hot path fractionally cheaper when the features are off).
"""

from __future__ import annotations

import threading
from collections.abc import Iterable
from typing import Any, Optional

import httpx


class _ConcurrencyTransport(httpx.BaseTransport):
    """Serialize HTTP requests through a bounded semaphore.

    Any caller (thread) that tries to send a request while ``max_in_flight``
    requests are already inflight will block on ``__enter__`` until a slot
    frees up.
    """

    def __init__(
        self,
        wrapped: httpx.BaseTransport,
        semaphore: threading.BoundedSemaphore,
    ) -> None:
        self._wrapped = wrapped
        self._semaphore = semaphore

    def handle_request(self, request: httpx.Request) -> httpx.Response:
        with self._semaphore:
            return self._wrapped.handle_request(request)

    def close(self) -> None:
        self._wrapped.close()


class _RateLimitTransport(httpx.BaseTransport):
    """Acquire a permit from the rate limiter, then delegate to the inner transport.

    ``limiter.try_acquire`` blocks by default until a permit is available,
    which gives us a smooth fixed-rate egress across the whole client.
    """

    _KEY = "turbine-sdk"

    def __init__(self, wrapped: httpx.BaseTransport, limiter: Any) -> None:
        self._wrapped = wrapped
        self._limiter = limiter

    def handle_request(self, request: httpx.Request) -> httpx.Response:
        self._limiter.try_acquire(self._KEY)
        return self._wrapped.handle_request(request)

    def close(self) -> None:
        self._wrapped.close()


def _build_transport_stack(
    *,
    max_retries: int,
    backoff_factor: float,
    retry_statuses: Iterable[int],
    max_in_flight: Optional[int],
    rate_limit_per_second: Optional[float],
    rate_limit_per_minute: Optional[float],
) -> httpx.BaseTransport:
    """Compose the transport stack per the module docstring.

    Factored out of ``_build_http_client`` so tests can inspect the
    individual layers without constructing a full ``httpx.Client``.
    """
    transport: httpx.BaseTransport = httpx.HTTPTransport()

    if max_retries > 0:
        from httpx_retries import Retry, RetryTransport

        retry = Retry(
            total=max_retries,
            backoff_factor=backoff_factor,
            status_forcelist=list(retry_statuses),
            # GraphQL is POST-only; httpx_retries excludes POST from
            # allowed_methods by default, so enable every method we
            # might use explicitly. Retrying POST is safe for the
            # status codes we care about (429 / 5xx): the server either
            # never processed the request or explicitly asked us to
            # back off.
            allowed_methods=[
                "POST",
                "GET",
                "HEAD",
                "PUT",
                "DELETE",
                "OPTIONS",
                "TRACE",
            ],
        )
        transport = RetryTransport(transport=transport, retry=retry)

    if max_in_flight is not None and max_in_flight > 0:
        transport = _ConcurrencyTransport(
            transport, threading.BoundedSemaphore(max_in_flight)
        )

    if rate_limit_per_second or rate_limit_per_minute:
        from pyrate_limiter import Duration, Limiter, Rate

        rates: list[Rate] = []
        if rate_limit_per_second:
            rates.append(Rate(max(1, int(rate_limit_per_second)), Duration.SECOND))
        if rate_limit_per_minute:
            rates.append(Rate(max(1, int(rate_limit_per_minute)), Duration.MINUTE))
        # pyrate_limiter requires intervals sorted ascending (smallest first).
        rates.sort(key=lambda r: r.interval)
        limiter = Limiter(rates)
        transport = _RateLimitTransport(transport, limiter)

    return transport


def _build_http_client(
    *,
    timeout: float,
    headers: Optional[dict[str, str]],
    max_retries: int,
    backoff_factor: float,
    retry_statuses: Iterable[int],
    max_in_flight: Optional[int],
    rate_limit_per_second: Optional[float],
    rate_limit_per_minute: Optional[float],
) -> httpx.Client:
    """Build an ``httpx.Client`` wired with the configured transport stack."""
    transport = _build_transport_stack(
        max_retries=max_retries,
        backoff_factor=backoff_factor,
        retry_statuses=retry_statuses,
        max_in_flight=max_in_flight,
        rate_limit_per_second=rate_limit_per_second,
        rate_limit_per_minute=rate_limit_per_minute,
    )
    return httpx.Client(timeout=timeout, headers=headers, transport=transport)
