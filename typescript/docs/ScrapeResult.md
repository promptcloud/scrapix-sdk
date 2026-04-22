# ScrapeResult

Result of a single URL scrape. `/scrape`

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **string** | Unique identifier for the scraping task | [optional] [default to undefined]
**url** | **string** | The URL that was scraped | [default to undefined]
**status_code** | **number** | HTTP status code of the response | [default to undefined]
**status** | **boolean** | Whether the scraping was successful | [default to undefined]
**response_headers** | **{ [key: string]: string; }** | HTTP headers of the response | [default to undefined]
**credits_used** | **number** | Credits used for the scraping task | [optional] [default to 0.0]
**data** | [**DataSerialized**](DataSerialized.md) | Content of the response | [default to undefined]
**structured_output** | [**StructuredOutput**](StructuredOutput.md) |  | [optional] [default to undefined]
**summarized_data** | **{ [key: string]: any; }** |  | [optional] [default to undefined]

## Example

```typescript
import { ScrapeResult } from '@promptcloud/scrapix';

const instance: ScrapeResult = {
    id,
    url,
    status_code,
    status,
    response_headers,
    credits_used,
    data,
    structured_output,
    summarized_data,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
