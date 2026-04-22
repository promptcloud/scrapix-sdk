# ExtractInput

Input schema for extracting structured data or summarization from a page. `/extract`

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **string** | Unique identifier for the scraping task | [optional] [default to undefined]
**url** | **string** | Input URL | [default to undefined]
**timeout** | **number** | Timeout in seconds for the request | [optional] [default to 40]
**max_retries** | **number** | Max retries before failing | [optional] [default to 5]
**max_cost** | **number** |  | [optional] [default to undefined]
**render** | **boolean** | Render the Page | [optional] [default to false]
**premium_proxies** | **boolean** | Use premium proxy | [optional] [default to false]
**auto_proxy** | **boolean** | Use auto proxy: normal proxies (2 attempts) → premium proxies → render fallback | [optional] [default to false]
**use_captcha_solver** | **boolean** | Use captcha solvers to avoid blocking | [optional] [default to false]
**use_cache** | **boolean** | If enabled will serve from fresh crawl | [optional] [default to true]
**output_format** | [**StructuredOutputFormat**](StructuredOutputFormat.md) | The format of the output | [optional] [default to undefined]
**structured_schema** | [**StructuredOutputSchema**](StructuredOutputSchema.md) |  | [optional] [default to undefined]
**summarize_schema** | [**SummarizeSchema**](SummarizeSchema.md) |  | [optional] [default to undefined]
**query** | **string** | Query for Structured output / Summarize / Instruct | [default to undefined]

## Example

```typescript
import { ExtractInput } from '@promptcloud/scrapix';

const instance: ExtractInput = {
    id,
    url,
    timeout,
    max_retries,
    max_cost,
    render,
    premium_proxies,
    auto_proxy,
    use_captcha_solver,
    use_cache,
    output_format,
    structured_schema,
    summarize_schema,
    query,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
