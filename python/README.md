# Scrapix — Python SDK

[![PyPI version](https://img.shields.io/pypi/v/scrapix.svg)](https://pypi.org/project/scrapix/)
[![Python versions](https://img.shields.io/pypi/pyversions/scrapix.svg)](https://pypi.org/project/scrapix/)
[![License](https://img.shields.io/pypi/l/scrapix.svg)](https://pypi.org/project/scrapix/)
[![Downloads](https://static.pepy.tech/badge/scrapix/month)](https://pepy.tech/project/scrapix)

Official Python client for [**Scrapix**](https://scrapix.promptcloud.com) — an AI-powered web scraping and data extraction API. Fetch pages, collect URLs, crawl sites, and extract structured data from a single function call, with JS rendering, proxy rotation, captcha solving, and LLM-backed extraction handled server-side.

---

## Table of contents

- [Installation](#installation)
- [Authentication](#authentication)
- [Quick start](#quick-start)
- [Endpoints](#endpoints)
  - [`scrape` — single page](#scrape--single-page)
  - [`collect` — URLs from a page](#collect--urls-from-a-page)
  - [`crawl` — collect + scrape](#crawl--collect--scrape)
  - [`extract` — structured data & summaries](#extract--structured-data--summaries)
- [Common input options](#common-input-options)
- [Output formats](#output-formats)
- [Error handling](#error-handling)
- [Custom host / advanced configuration](#custom-host--advanced-configuration)
- [Links](#links)
- [License](#license)

---

## Installation

```bash
pip install scrapix
```

Requires Python 3.9 or newer.

## Authentication

All requests require an API key. Get one at [scrapix.promptcloud.com](https://scrapix.promptcloud.com) and either pass it explicitly or load it from an environment variable:

```python
import os
from scrapix import create_client

api = create_client(os.environ["SCRAPIX_API_KEY"])
```

## Quick start

```python
from scrapix import create_client, ScrapeInput

api = create_client("YOUR_API_KEY")

result = api.scrape(ScrapeInput(url="https://example.com"))
print(result.data.data)        # page content (HTML by default)
print(result.status_code)      # upstream HTTP status
print(result.credits_used)     # credits consumed by this call
```

`create_client(api_key)` targets `https://api-scrapix.promptcloud.com` by default. Override with `create_client(api_key, host="https://your-host")`.

---

## Endpoints

### `scrape` — single page

Fetch one URL and return its content in the requested format.

```python
from scrapix import create_client, ScrapeInput

api = create_client("YOUR_API_KEY")

result = api.scrape(ScrapeInput(
    url="https://example.com",
    output_format="markdown",   # html | text | markdown | docx | pdf | base64
    render=True,                # execute JS before returning
))

print(result.data.format)       # "markdown"
print(result.data.data)         # rendered markdown
```

### `collect` — URLs from a page

Extract outgoing links from a page. Useful as a first step before crawling.

```python
from scrapix import create_client, CollectInput

result = api.collect(CollectInput(
    url="https://example.com",
    urls_limit=100,
    include_paths=r"^/blog/",       # regex filter — keep only matching paths
    exclude_paths=r"/tag/|/author/",
    include_sitemap_urls=True,      # also harvest URLs from sitemap.xml
))

# result.links.data is a serialized string in result.links.format ("json" by default)
print(result.links.data)
```

### `crawl` — collect + scrape

Collect URLs from a starting page and scrape each one in a single call.

```python
from scrapix import create_client, CrawlInput

result = api.crawl(CrawlInput(
    url="https://books.toscrape.com/",
    urls_limit=10,                  # 1–25
    output_format="markdown",
    include_sitemap_urls=False,
))

for page in result.responses:
    print(page.url, "->", len(page.data.data), "chars")
```

### `extract` — structured data & summaries

Run an LLM over a page to answer a natural-language query or extract structured data.

```python
from scrapix import create_client, ExtractInput

# Free-form answer
result = api.extract(ExtractInput(
    url="https://example.com",
    query="What is this website about? Answer in one sentence.",
))
print(result.result)

# Structured extraction — provide a JSON Schema
from scrapix import StructuredOutputSchema

result = api.extract(ExtractInput(
    url="https://books.toscrape.com/",
    query="Extract the first 5 books on this page.",
    structured_schema=StructuredOutputSchema(
        query="Extract the first 5 books.",
        schema={
            "type": "object",
            "properties": {
                "books": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "title": {"type": "string"},
                            "price": {"type": "string"},
                        },
                    },
                }
            },
        },
    ),
))
print(result.structured_output.data)   # serialized in result.structured_output.format
```

---

## Common input options

Every input model accepts the following fields in addition to its endpoint-specific ones:

| Field                | Type    | Default | Description                                                             |
|----------------------|---------|---------|-------------------------------------------------------------------------|
| `url`                | `str`   | —       | Target URL (required).                                                  |
| `timeout`            | `int`   | `40`    | Request timeout in seconds (10–1000).                                   |
| `max_retries`        | `int`   | `5`     | Max retries before the request fails.                                   |
| `render`             | `bool`  | `False` | Execute JavaScript before capturing the page.                           |
| `premium_proxies`    | `bool`  | `False` | Route through premium residential/mobile proxies.                       |
| `auto_proxy`         | `bool`  | `False` | Escalate automatically: normal proxies → premium → render fallback.     |
| `use_captcha_solver` | `bool`  | `False` | Solve captchas when encountered.                                        |
| `use_cache`          | `bool`  | `True`  | Serve from the fresh-crawl cache when available.                        |

## Output formats

| Format             | Where it applies                          | Notes                                  |
|--------------------|-------------------------------------------|----------------------------------------|
| `html`             | `scrape`, `crawl`                         | Default.                               |
| `text`             | `scrape`, `crawl`                         | Plain-text extraction.                 |
| `markdown`         | `scrape`, `crawl`                         | HTML → Markdown conversion.            |
| `docx` / `pdf`     | `scrape`, `crawl`                         | Binary content, base64-encoded.        |
| `base64`           | `scrape`, `crawl`                         | Raw HTML as base64.                    |
| `json` (default)   | `collect`, `extract.structured_output`    | Other structured formats also allowed. |
| `xml`/`yaml`/`toml`| `collect`, `extract.structured_output`    |                                        |

## Error handling

API errors raise `scrapix.ApiException` (and its subclasses `BadRequestException`, `UnauthorizedException`, `NotFoundException`, `ServiceException`, …):

```python
from scrapix import create_client, ScrapeInput
from scrapix.exceptions import ApiException

try:
    result = api.scrape(ScrapeInput(url="https://example.com"))
except ApiException as e:
    print(f"HTTP {e.status}: {e.reason}")
    print(e.body)          # raw error body
    print(e.headers)       # response headers
```

Non-HTTP failures (network, timeout) raise the underlying `urllib3` exception.

## Custom host / advanced configuration

`create_client` wraps the common "Configuration + ApiClient + APIServicesApi" setup. When you need interceptors, per-request timeouts, or connection pooling, drop down to the raw client:

```python
import scrapix

config = scrapix.Configuration(
    host="https://api-scrapix.promptcloud.com",
    api_key={"APIKeyHeader": "YOUR_API_KEY"},
)
config.retries = 3

with scrapix.ApiClient(config) as client:
    api = scrapix.APIServicesApi(client)
    result = api.scrape(
        scrapix.ScrapeInput(url="https://example.com"),
        _request_timeout=60,
    )
```

Every endpoint method accepts per-call overrides via `_request_timeout`, `_headers`, and `_host_index`. See the [API reference](https://docs-scrapix.promptcloud.com/api-reference/scrapix-api) for the full list.

## Links

- **Home:** https://scrapix.promptcloud.com
- **API reference:** https://docs-scrapix.promptcloud.com/api-reference/scrapix-api
- **Docs:** https://docs-scrapix.promptcloud.com
- **Source:** https://github.com/promptcloud/scrapix-sdk/tree/main/python
- **Issues:** https://github.com/promptcloud/scrapix-sdk/issues
- **Changelog:** https://github.com/promptcloud/scrapix-sdk/releases

## License

Released under the terms of the [LICENSE](./LICENSE) file shipped with this package.
