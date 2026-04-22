# CrawlResult

Result of crawling URLs from a page. `/crawl`

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **string** | Unique identifier for the scraping task | [optional] [default to undefined]
**url** | **string** | The URL that was scraped | [default to undefined]
**status_code** | **number** | HTTP status code of the response | [default to undefined]
**status** | **boolean** | Whether the scraping was successful | [default to undefined]
**response_headers** | **{ [key: string]: string; }** | HTTP headers of the response | [default to undefined]
**credits_used** | **number** | Credits used for the scraping task | [optional] [default to 0.0]
**main_page** | [**ScrapeResult**](ScrapeResult.md) |  | [optional] [default to undefined]
**responses** | [**Array&lt;ScrapeResult&gt;**](ScrapeResult.md) | List of responses for each URL scraped | [default to undefined]

## Example

```typescript
import { CrawlResult } from '@promptcloud/scrapix';

const instance: CrawlResult = {
    id,
    url,
    status_code,
    status,
    response_headers,
    credits_used,
    main_page,
    responses,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
