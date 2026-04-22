# ExtractResult

Result of extracting structured data or summarization from a page. `/extract`

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **string** | Unique identifier for the scraping task | [optional] [default to undefined]
**url** | **string** | The URL that was scraped | [default to undefined]
**status_code** | **number** | HTTP status code of the response | [default to undefined]
**status** | **boolean** | Whether the scraping was successful | [default to undefined]
**response_headers** | **{ [key: string]: string; }** | HTTP headers of the response | [default to undefined]
**credits_used** | **number** | Credits used for the scraping task | [optional] [default to 0.0]
**query** | **string** | Query for Structured output / Summarize / Instruct | [default to undefined]
**result** | **string** | Result of the query | [default to undefined]
**final_html_page** | **string** |  | [optional] [default to undefined]
**cost** | **number** | Cost incurred for the extraction | [optional] [default to 0.0]
**agent_type** | **string** | Type of extraction agent used | [default to undefined]
**tokens_used** | **number** |  | [optional] [default to undefined]
**structured_output** | [**StructuredOutput**](StructuredOutput.md) |  | [optional] [default to undefined]

## Example

```typescript
import { ExtractResult } from '@promptcloud/scrapix';

const instance: ExtractResult = {
    id,
    url,
    status_code,
    status,
    response_headers,
    credits_used,
    query,
    result,
    final_html_page,
    cost,
    agent_type,
    tokens_used,
    structured_output,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
