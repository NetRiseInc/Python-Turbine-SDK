"""Generic Relay-style cursor paginator.

The Turbine GraphQL API exposes ~21 cursor-paginated operations. They all
share the same response shape:

    {
      edges: [{cursor, node}, ...] | null,
      pageInfo: {
        endCursor: str | null,
        hasNextPage: bool,
        hasPreviousPage: bool,
        startCursor: str | null,
        totalCount: int | null,
      }
    }

``iter_all_pages`` walks that shape, transparently advancing ``after`` on
each iteration until the server reports ``hasNextPage=False``. Callers
provide a closure that builds the per-page request.

Operations that currently use ``Cursor`` (the flexible variant with
``first: Optional[int]``) are all covered here. A handful of
operations in the schema use ``CursorV3`` (``first: Int!``); those are
not yet wired into a ``TurbineClient.iter_*`` method but could be added
with a parallel helper if needed.
"""

from __future__ import annotations

from collections.abc import Callable, Iterator
from typing import Any, Optional, TypeVar

from netrise_turbine_sdk_graphql import input_types as inputs

TNode = TypeVar("TNode")


def iter_all_pages(
    fetch_page: Callable[["inputs.Cursor"], Any],
    *,
    page_size: int = 100,
    max_pages: Optional[int] = None,
) -> Iterator[TNode]:
    """Iterate through every node of a Relay cursor connection.

    Args:
        fetch_page: Callable that takes an ``inputs.Cursor`` and returns the
            connection object (anything with ``edges`` and ``page_info``
            attributes, or ``None`` if the query returned no data).
        page_size: Requests per page. The server may cap this lower; we
            honor whatever the page_info tells us on the way back.
        max_pages: Hard cap on the number of server round-trips. ``None``
            means no limit; iteration ends when ``hasNextPage`` is false.

    Yields:
        Each non-null node in the order returned by the server.
    """
    after: Optional[str] = None
    pages_fetched = 0

    while True:
        if max_pages is not None and pages_fetched >= max_pages:
            return

        cursor = inputs.Cursor(first=page_size, after=after)
        connection = fetch_page(cursor)
        pages_fetched += 1

        if connection is None:
            return

        edges = getattr(connection, "edges", None) or []
        for edge in edges:
            if edge is None:
                continue
            node = getattr(edge, "node", None)
            if node is not None:
                yield node

        page_info = getattr(connection, "page_info", None)
        if page_info is None:
            return
        if not getattr(page_info, "has_next_page", False):
            return

        next_cursor = getattr(page_info, "end_cursor", None)
        if not next_cursor:
            # Server says there is more but gave us no cursor; nothing safe
            # to do but stop.
            return
        after = next_cursor
