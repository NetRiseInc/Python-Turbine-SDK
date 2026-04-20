"""Turbine Python SDK.

This package provides a stable, handwritten wrapper client (`TurbineClient`) over
the generated GraphQL client code.
"""

from .client import TurbineClient, TurbineClientConfig
from .pagination import iter_all_pages

__all__ = ["TurbineClient", "TurbineClientConfig", "iter_all_pages"]
