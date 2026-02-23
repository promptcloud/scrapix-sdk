# Scrapix TypeScript SDK

Official TypeScript/JavaScript SDK for the Scrapix API by PromptCloud.

## Installation

```bash
npm install @promptcloud/scrapix
```

## Quick Start

```typescript
import { Configuration, APIServicesApi, ScrapeInput, OutputFormatEnum } from '@promptcloud/scrapix';

const config = new Configuration({
  basePath: 'https://api-scrapix.promptcloud.com',
  apiKey: process.env.SCRAPIX_API_KEY
});

const api = new APIServicesApi(config);

// Scrape a webpage
const result = await api.scrape({
  scrapeInput: {
    url: 'https://example.com',
    outputFormat: OutputFormatEnum.Markdown
  }
});

console.log(result.data);
```

## API Methods

| Method | Description |
|--------|-------------|
| `scrape(scrapeInput)` | Scrape content from a URL |
| `crawl(crawlInput)` | Crawl a website for URLs |
| `collect(collectInput)` | Collect URLs from a page |
| `extract(extractInput)` | AI-powered data extraction |
| `echo()` | Test API connectivity |

## Common Options

All input types support these options:

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `url` | string | *required* | Target URL |
| `timeout` | number | 40 | Request timeout (seconds) |
| `maxRetries` | number | 5 | Max retry attempts |
| `render` | boolean | false | Enable JS rendering |
| `premiumProxies` | boolean | false | Use premium proxies |
| `useCaptchaSolver` | boolean | false | Auto-solve CAPTCHAs |
| `useCache` | boolean | true | Use cached responses |

## Requirements

- Node.js >= 16.0.0

## Support

- Email: [sales@promptcloud.com](mailto:sales@promptcloud.com)
- Website: [https://scrapix.promptcloud.com](https://scrapix.promptcloud.com)

## License

Provided by [PromptCloud](https://www.promptcloud.com).
