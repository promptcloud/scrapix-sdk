# Scrapix — TypeScript / JavaScript SDK

[![npm version](https://img.shields.io/npm/v/@promptcloud/scrapix.svg)](https://www.npmjs.com/package/@promptcloud/scrapix)
[![npm downloads](https://img.shields.io/npm/dm/@promptcloud/scrapix.svg)](https://www.npmjs.com/package/@promptcloud/scrapix)
[![types](https://img.shields.io/npm/types/@promptcloud/scrapix.svg)](https://www.npmjs.com/package/@promptcloud/scrapix)
[![license](https://img.shields.io/npm/l/@promptcloud/scrapix.svg)](https://www.npmjs.com/package/@promptcloud/scrapix)

Official TypeScript/JavaScript client for [**Scrapix**](https://scrapix.promptcloud.com) — an AI-powered web scraping and data extraction API. Fetch pages, collect URLs, crawl sites, and extract structured data from a single function call, with JS rendering, proxy rotation, captcha solving, and LLM-backed extraction handled server-side.

Works in Node.js (18+) and any bundler targeting modern browsers. First-class TypeScript types ship with the package.

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
npm install @promptcloud/scrapix
# or
yarn add @promptcloud/scrapix
# or
pnpm add @promptcloud/scrapix
```

Requires Node.js 18 or newer. Works in browsers via any modern bundler (Vite, webpack, esbuild, Rollup).

## Authentication

All requests require an API key. Get one at [scrapix.promptcloud.com](https://scrapix.promptcloud.com) and either pass it explicitly or load it from an environment variable:

```ts
import { createClient } from "@promptcloud/scrapix";

const api = createClient(process.env.SCRAPIX_API_KEY!);
```

## Quick start

```ts
import { createClient } from "@promptcloud/scrapix";

const api = createClient("YOUR_API_KEY");

const { data: result } = await api.scrape({ url: "https://example.com" });
console.log(result.data?.data);   // page content
console.log(result.status_code);  // upstream HTTP status
console.log(result.credits_used); // credits consumed
```

Every method returns an axios-style response — the parsed API body is on `.data`. `createClient(apiKey)` targets `https://api-scrapix.promptcloud.com` by default; pass a second argument to override.

---

## Endpoints

### `scrape` — single page

Fetch one URL and return its content in the requested format.

```ts
const { data: result } = await api.scrape({
  url: "https://example.com",
  output_format: "markdown",   // "html" | "text" | "markdown" | "docx" | "pdf" | "base64"
  render: true,                // execute JS before capturing
});

console.log(result.data?.format); // "markdown"
console.log(result.data?.data);   // rendered markdown
```

### `collect` — URLs from a page

Extract outgoing links from a page. Useful as a first step before crawling.

```ts
const { data: result } = await api.collect({
  url: "https://example.com",
  urls_limit: 100,
  include_paths: "^/blog/",           // regex — keep only matching paths
  exclude_paths: "/tag/|/author/",
  include_sitemap_urls: true,         // also harvest from sitemap.xml
});

// result.links.data is a serialized string in result.links.format ("json" by default)
console.log(result.links?.data);
```

### `crawl` — collect + scrape

Collect URLs from a starting page and scrape each one in a single call.

```ts
const { data: result } = await api.crawl({
  url: "https://books.toscrape.com/",
  urls_limit: 10,                // 1–25
  output_format: "markdown",
});

for (const page of result.responses ?? []) {
  console.log(page.url, "->", page.data?.data?.length ?? 0, "chars");
}
```

### `extract` — structured data & summaries

Run an LLM over a page to answer a natural-language query or extract structured data.

```ts
// Free-form answer
const { data: answer } = await api.extract({
  url: "https://example.com",
  query: "What is this website about? Answer in one sentence.",
});
console.log(answer.result);

// Structured extraction — provide a JSON Schema
const { data: books } = await api.extract({
  url: "https://books.toscrape.com/",
  query: "Extract the first 5 books on this page.",
  structured_schema: {
    query: "Extract the first 5 books.",
    format: "json",
    schema: {
      type: "object",
      properties: {
        books: {
          type: "array",
          items: {
            type: "object",
            properties: {
              title: { type: "string" },
              price: { type: "string" },
            },
          },
        },
      },
    },
  },
});
console.log(books.structured_output?.data); // serialized string
```

---

## Common input options

Every endpoint accepts these fields in addition to its endpoint-specific ones:

| Field                | Type      | Default | Description                                                             |
|----------------------|-----------|---------|-------------------------------------------------------------------------|
| `url`                | `string`  | —       | Target URL (required).                                                  |
| `timeout`            | `number`  | `40`    | Request timeout in seconds (10–1000).                                   |
| `max_retries`        | `number`  | `5`     | Max retries before the request fails.                                   |
| `render`             | `boolean` | `false` | Execute JavaScript before capturing the page.                           |
| `premium_proxies`    | `boolean` | `false` | Route through premium residential/mobile proxies.                       |
| `auto_proxy`         | `boolean` | `false` | Escalate automatically: normal proxies → premium → render fallback.     |
| `use_captcha_solver` | `boolean` | `false` | Solve captchas when encountered.                                        |
| `use_cache`          | `boolean` | `true`  | Serve from the fresh-crawl cache when available.                        |

## Output formats

| Format                 | Where it applies                          | Notes                                  |
|------------------------|-------------------------------------------|----------------------------------------|
| `html`                 | `scrape`, `crawl`                         | Default.                               |
| `text`                 | `scrape`, `crawl`                         | Plain-text extraction.                 |
| `markdown`             | `scrape`, `crawl`                         | HTML → Markdown conversion.            |
| `docx` / `pdf`         | `scrape`, `crawl`                         | Binary content, base64-encoded.        |
| `base64`               | `scrape`, `crawl`                         | Raw HTML as base64.                    |
| `json` (default)       | `collect`, `extract.structured_output`    | Other structured formats also allowed. |
| `xml` / `yaml` / `toml`| `collect`, `extract.structured_output`    |                                        |

## Error handling

Every method uses axios under the hood, so HTTP errors surface as rejected promises with `AxiosError`:

```ts
import { AxiosError } from "axios";

try {
  const { data } = await api.scrape({ url: "https://example.com" });
} catch (err) {
  if (err instanceof AxiosError) {
    console.error("status:", err.response?.status);
    console.error("body:  ", err.response?.data);
  } else {
    throw err;
  }
}
```

Non-HTTP failures (network, DNS, timeout) surface as plain `Error`s from axios.

## Custom host / advanced configuration

`createClient` wraps the common "Configuration + APIServicesApi" setup. For a custom axios instance (interceptors, per-request timeouts, proxy agents, retry middleware), construct things manually:

```ts
import axios from "axios";
import { APIServicesApi, Configuration } from "@promptcloud/scrapix";

const http = axios.create({ timeout: 60_000 });
http.interceptors.request.use((config) => {
  console.log("→", config.method?.toUpperCase(), config.url);
  return config;
});

const api = new APIServicesApi(
  new Configuration({
    apiKey: "YOUR_API_KEY",
    basePath: "https://api-scrapix.promptcloud.com",
  }),
  undefined,
  http,
);

const { data } = await api.scrape({ url: "https://example.com" });
```

## Links

- **Home:** https://scrapix.promptcloud.com
- **API reference:** https://docs-scrapix.promptcloud.com/api-reference/scrapix-api
- **Docs:** https://docs-scrapix.promptcloud.com
- **Source:** https://github.com/promptcloud/scrapix-sdk/tree/main/typescript
- **Issues:** https://github.com/promptcloud/scrapix-sdk/issues
- **Changelog:** https://github.com/promptcloud/scrapix-sdk/releases

## License

Released under the terms of the [LICENSE](./LICENSE) file shipped with this package.
