"""GraphQL client exceptions with user-facing messages.

Hand-edit ``turbine/python-sdk/codegen/exceptions.py``. ariadne-codegen
copies that file here on every generate.
"""

from __future__ import annotations

import json
from typing import Any, Optional, Union

import httpx

# Distinguishes the two InvalidResponseError raise sites in BaseClient.get_data.
REASON_NOT_JSON = "not_json"
REASON_MISSING_DATA_AND_ERRORS = "missing_data_and_errors"

_BODY_SNIPPET_LIMIT = 200
_REQUEST_ID_HEADER = "x-request-id"
_RETRY_AFTER_HEADER = "retry-after"


def _request_of(response: httpx.Response) -> Optional[httpx.Request]:
    """Return the request attached to *response*, or None.

    ``httpx.Response.request`` raises ``RuntimeError`` when the response was
    constructed without a request (tests, some transport failures). Never
    inspect request headers — ``Authorization`` must not leak into messages.
    """
    try:
        return response.request
    except RuntimeError:
        return None


def operation_name_from_response(response: httpx.Response) -> Optional[str]:
    """Best-effort GraphQL ``operationName`` from a JSON request body.

    Multipart uploads have no JSON body; returns None rather than guessing.
    Called only on error paths.
    """
    request = _request_of(response)
    if request is None:
        return None
    content = request.content
    if not content:
        return None
    try:
        payload = json.loads(content)
    except (json.JSONDecodeError, UnicodeDecodeError, TypeError, ValueError):
        return None
    if not isinstance(payload, dict):
        return None
    name = payload.get("operationName")
    if isinstance(name, str) and name:
        return name
    return None


def _endpoint_from_response(response: httpx.Response) -> Optional[str]:
    request = _request_of(response)
    if request is None:
        return None
    url = getattr(request, "url", None)
    if url is None:
        return None
    return str(url) or None


def _header(response: httpx.Response, name: str) -> Optional[str]:
    try:
        value = response.headers.get(name)
    except Exception:
        return None
    if not value:
        return None
    text = str(value).strip()
    return text or None


def _body_snippet(
    response: httpx.Response, limit: int = _BODY_SNIPPET_LIMIT
) -> Optional[str]:
    try:
        text = response.text
    except Exception:
        return None
    if not text:
        return None
    collapsed = " ".join(text.split())
    if len(collapsed) > limit:
        return collapsed[:limit] + "…"
    return collapsed


def _where_clause(endpoint: Optional[str]) -> str:
    return f" at {endpoint}" if endpoint else ""


def _request_id_suffix(request_id: Optional[str]) -> str:
    return f" Request id: {request_id}." if request_id else ""


class GraphQLClientError(Exception):
    """Base exception."""


class GraphQLClientHttpError(GraphQLClientError):
    def __init__(self, status_code: int, response: httpx.Response) -> None:
        self.status_code = status_code
        self.response = response

    def __str__(self) -> str:
        operation = operation_name_from_response(self.response)
        endpoint = _endpoint_from_response(self.response)
        request_id = _header(self.response, _REQUEST_ID_HEADER)
        retry_after = _header(self.response, _RETRY_AFTER_HEADER)
        subject = operation or "GraphQL request"
        where = _where_clause(endpoint)
        status = self.status_code

        if status == 401:
            core = (
                f"{subject} was rejected (HTTP 401){where}. "
                "Credentials were not accepted. Set TURBINE_API_TOKEN, or set "
                "client_id, client_secret, audience, and domain."
            )
        elif status == 403:
            core = (
                f"{subject} was forbidden (HTTP 403){where}. "
                "You are authenticated, but this operation is not permitted "
                "for this organization."
            )
        elif status == 404:
            core = (
                f"{subject} got HTTP 404{where}. "
                "The endpoint URL is likely wrong. Check the `endpoint` setting "
                "(e.g. https://apollo.turbine.netrise.io/graphql/v3)."
            )
        elif status == 429:
            retry_bit = (
                f" Retry after {retry_after}." if retry_after else " Wait and retry."
            )
            core = (
                f"{subject} was rate limited (HTTP 429){where} after the "
                f"client's retries.{retry_bit}"
            )
        elif 500 <= status <= 599:
            core = (
                f"{subject} failed with HTTP {status}{where} after the client's "
                "retries. This is a server-side issue; the request was not "
                "processed. Please try again in a moment."
            )
        else:
            core = f"{subject} failed with HTTP {status}{where}."

        return core + _request_id_suffix(request_id)


class GraphQLClientInvalidResponseError(GraphQLClientError):
    def __init__(
        self,
        response: httpx.Response,
        reason: Optional[str] = None,
    ) -> None:
        self.response = response
        self.reason = reason

    def __str__(self) -> str:
        operation = operation_name_from_response(self.response)
        endpoint = _endpoint_from_response(self.response)
        request_id = _header(self.response, _REQUEST_ID_HEADER)
        content_type = _header(self.response, "content-type")
        snippet = _body_snippet(self.response)
        subject = operation or "GraphQL request"
        where = _where_clause(endpoint)
        try:
            status = self.response.status_code
            status_bit = f" (HTTP {status})"
        except Exception:
            status_bit = ""

        if self.reason == REASON_NOT_JSON:
            core = f"{subject} returned a non-JSON body{status_bit}{where}."
            if content_type:
                core += f" Content-Type was {content_type}."
            core += (
                " This is often an HTML login or proxy page instead of the "
                "GraphQL API."
            )
        elif self.reason == REASON_MISSING_DATA_AND_ERRORS:
            core = (
                f"{subject} returned JSON without `data` or `errors`"
                f"{status_bit}{where}."
            )
        else:
            core = (
                f"{subject} returned a response that is not a GraphQL result"
                f"{status_bit}{where}."
            )

        if snippet:
            core += f" Body starts with: {snippet}"
        return core + _request_id_suffix(request_id)


class GraphQLClientGraphQLError(GraphQLClientError):
    def __init__(
        self,
        message: str,
        locations: Optional[list[dict[str, int]]] = None,
        path: Optional[list[str]] = None,
        extensions: Optional[dict[str, object]] = None,
        original: Optional[dict[str, object]] = None,
    ):
        self.message = message
        self.locations = locations
        self.path = path
        self.extensions = extensions
        self.original = original

    def __str__(self) -> str:
        text = self.message or "GraphQL error"
        extras: list[str] = []
        if self.path:
            extras.append("at " + ".".join(str(part) for part in self.path))
        if isinstance(self.extensions, dict):
            code = self.extensions.get("code")
            if code is not None and str(code):
                extras.append(f"code={code}")
        if extras:
            return f"{text} ({'; '.join(extras)})"
        return text

    @classmethod
    def from_dict(cls, error: dict[str, Any]) -> GraphQLClientGraphQLError:
        return cls(
            message=error["message"],
            locations=error.get("locations"),
            path=error.get("path"),
            extensions=error.get("extensions"),
            original=error,
        )


class GraphQLClientGraphQLMultiError(GraphQLClientError):
    def __init__(
        self,
        errors: list[GraphQLClientGraphQLError],
        data: Optional[dict[str, Any]] = None,
        operation_name: Optional[str] = None,
    ):
        self.errors = errors
        self.data = data
        self.operation_name = operation_name

    def __str__(self) -> str:
        subject = self.operation_name or "GraphQL request"
        count = len(self.errors)
        noun = "error" if count == 1 else "errors"
        header = f"{subject} failed with {count} GraphQL {noun}"
        if not self.errors:
            return header + "."
        lines = [header + ":"]
        for index, error in enumerate(self.errors, start=1):
            lines.append(f"  {index}. {error}")
        return "\n".join(lines)

    @classmethod
    def from_errors_dicts(
        cls,
        errors_dicts: list[dict[str, Any]],
        data: Optional[dict[str, Any]] = None,
        operation_name: Optional[str] = None,
    ) -> GraphQLClientGraphQLMultiError:
        return cls(
            errors=[GraphQLClientGraphQLError.from_dict(e) for e in errors_dicts],
            data=data,
            operation_name=operation_name,
        )


class GraphQLClientInvalidMessageFormat(GraphQLClientError):  # noqa: N818
    """Websocket-only; unused while ``async_client = false``. Left as-is."""

    def __init__(self, message: Union[str, bytes]) -> None:
        self.message = message

    def __str__(self) -> str:
        return "Invalid message format."
