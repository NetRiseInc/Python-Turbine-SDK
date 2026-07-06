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
from typing import Any, Generic, Optional, TypeVar

from netrise_turbine_sdk_graphql import input_types as inputs

TNode = TypeVar("TNode")


class Paginator(Generic[TNode], Iterator[TNode]):
    """Lazy Relay-style cursor paginator.

    ``Paginator`` behaves like the historical ``iter_all_pages`` generator,
    while retaining useful pagination metadata as pages are fetched.
    """

    def __init__(
        self,
        fetch_page: Callable[["inputs.Cursor"], Any],
        *,
        page_size: int = 100,
        max_pages: Optional[int] = None,
        start_after: Optional[str] = None,
        max_items: Optional[int] = None,
        node_filter: Optional[Callable[[TNode], bool]] = None,
    ) -> None:
        self._fetch_page = fetch_page
        self._page_size = page_size
        self._max_pages = max_pages
        self._start_after = start_after
        self._max_items = max_items
        self._node_filter = node_filter
        self._after = start_after
        self._buffer: list[tuple[TNode, Optional[str]]] = []
        self._yielded_count = 0
        self._done = False
        self._total_count: Optional[int] = None
        self._last_cursor: Optional[str] = None
        self._pages_fetched = 0

    @property
    def total_count(self) -> Optional[int]:
        """The latest ``page_info.total_count`` observed from the server."""
        return self._total_count

    @property
    def last_cursor(self) -> Optional[str]:
        """Cursor of the last yielded item, suitable for ``start_after``."""
        return self._last_cursor

    @property
    def pages_fetched(self) -> int:
        """Number of server round-trips made by this paginator."""
        return self._pages_fetched

    def __iter__(self) -> "Paginator[TNode]":
        return self

    def __next__(self) -> TNode:
        while not self._buffer:
            if self._done:
                raise StopIteration
            self._fetch_next_page()

        node, cursor = self._buffer.pop(0)
        self._yielded_count += 1
        if cursor is not None:
            self._last_cursor = cursor
        if self._max_items is not None and self._yielded_count >= self._max_items:
            self._done = True
            self._buffer.clear()
        return node

    def first(self) -> Optional[TNode]:
        """Return the first available node without consuming this iterator."""
        if self._node_filter is None:
            connection = self._fetch_page(
                inputs.Cursor(first=1, after=self._start_after)
            )
            for node, _cursor in _iter_connection_nodes(connection, None):
                return node
            return None

        paginator: Paginator[TNode] = Paginator(
            self._fetch_page,
            page_size=1,
            max_pages=self._max_pages,
            start_after=self._start_after,
            max_items=1,
            node_filter=self._node_filter,
        )
        return next(paginator, None)

    def to_list(self, limit: Optional[int] = None) -> list[TNode]:
        """Materialize this paginator, optionally stopping after ``limit`` items."""
        items: list[TNode] = []
        for item in self:
            items.append(item)
            if limit is not None and len(items) >= limit:
                break
        return items

    def _fetch_next_page(self) -> None:
        if self._max_items is not None and self._yielded_count >= self._max_items:
            self._done = True
            return
        if self._max_pages is not None and self._pages_fetched >= self._max_pages:
            self._done = True
            return

        first = self._page_size
        if self._node_filter is None and self._max_items is not None:
            remaining = self._max_items - self._yielded_count
            if remaining <= 0:
                self._done = True
                return
            first = min(first, remaining)

        connection = self._fetch_page(inputs.Cursor(first=first, after=self._after))
        self._pages_fetched += 1

        if connection is None:
            self._done = True
            return

        page_info = getattr(connection, "page_info", None)
        if page_info is None:
            self._buffer.extend(_iter_connection_nodes(connection, self._node_filter))
            self._done = True
            return

        total_count = getattr(page_info, "total_count", None)
        if total_count is not None:
            self._total_count = total_count

        end_cursor = getattr(page_info, "end_cursor", None)
        page_nodes = _iter_connection_nodes(connection, self._node_filter)
        if page_nodes and page_nodes[-1][1] is None and end_cursor is not None:
            node, _cursor = page_nodes[-1]
            page_nodes[-1] = (node, end_cursor)
        self._buffer.extend(page_nodes)

        if end_cursor:
            self._after = end_cursor

        if not getattr(page_info, "has_next_page", False):
            self._done = True
            return
        if not end_cursor:
            # Server says there is more but gave us no cursor; nothing safe
            # to do but stop after yielding the buffered page.
            self._done = True


def _iter_connection_nodes(
    connection: Any,
    node_filter: Optional[Callable[[TNode], bool]],
) -> list[tuple[TNode, Optional[str]]]:
    nodes: list[tuple[TNode, Optional[str]]] = []
    edges = getattr(connection, "edges", None) or []
    for edge in edges:
        if edge is None:
            continue
        node = getattr(edge, "node", None)
        if node is None:
            continue
        if node_filter is not None and not node_filter(node):
            continue
        cursor = getattr(edge, "cursor", None) or None
        nodes.append((node, cursor))
    return nodes


def iter_all_pages(
    fetch_page: Callable[["inputs.Cursor"], Any],
    *,
    page_size: int = 100,
    max_pages: Optional[int] = None,
    start_after: Optional[str] = None,
    max_items: Optional[int] = None,
    node_filter: Optional[Callable[[TNode], bool]] = None,
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
        start_after: Optional cursor to resume after.
        max_items: Optional cap on yielded items.
        node_filter: Optional predicate applied before yielding each node.

    Yields:
        Each non-null node in the order returned by the server.
    """
    return Paginator(
        fetch_page,
        page_size=page_size,
        max_pages=max_pages,
        start_after=start_after,
        max_items=max_items,
        node_filter=node_filter,
    )
