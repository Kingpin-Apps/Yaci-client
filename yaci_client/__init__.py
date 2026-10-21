"""A client library for accessing Yaci Store API"""

from .client import AuthenticatedClient, Client

__version__ = "1.0.1"
__app_name__ = "yaci_client"
__all__ = (
    "AuthenticatedClient",
    "Client",
)
