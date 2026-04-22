# CollectResult

Result of collecting URLs from a page. `/collect`

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **string** | Unique identifier for the scraping task | [optional] [default to undefined]
**url** | **string** | The URL that was scraped | [default to undefined]
**status_code** | **number** | HTTP status code of the response | [default to undefined]
**status** | **boolean** | Whether the scraping was successful | [default to undefined]
**response_headers** | **{ [key: string]: string; }** | HTTP headers of the response | [default to undefined]
**credits_used** | **number** | Credits used for the scraping task | [optional] [default to 0.0]
**links** | [**StructuredOutput**](StructuredOutput.md) | links extracted from the page | [optional] [default to undefined]
**main_page** | [**ScrapeResult**](ScrapeResult.md) |  | [optional] [default to undefined]

## Example

```typescript
import { CollectResult } from '@promptcloud/scrapix';

const instance: CollectResult = {
    id,
    url,
    status_code,
    status,
    response_headers,
    credits_used,
    links,
    main_page,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
