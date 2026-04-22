"""Convenience helper for the common authenticated-client setup.

Shipped alongside the generated code. Users can either use this one-liner:

    from scrapix import create_client, ScrapeInput
    api = create_client("YOUR_API_KEY")
    result = api.scrape(ScrapeInput(url="https://example.com"))

…or drop down to the full `Configuration + ApiClient + APIServicesApi` dance
when they need custom transport options, retries, or context-manager lifecycle.
"""
from __future__ import annotations

from .api.api_services_api import APIServicesApi
from .api_client import ApiClient
from .configuration import Configuration

DEFAULT_HOST = "https://api-scrapix.promptcloud.com"

# Must match the `name` of the APIKeyHeader security scheme in the OpenAPI
# spec — openapi-generator-cli keys the api_key dict by the scheme name.
_SECURITY_SCHEME = "APIKeyHeader"


def create_client(api_key: str, host: str = DEFAULT_HOST) -> APIServicesApi:
    """Return a configured APIServicesApi ready to make authenticated calls."""
    cfg = Configuration(host=host, api_key={_SECURITY_SCHEME: api_key})
    return APIServicesApi(ApiClient(cfg))
