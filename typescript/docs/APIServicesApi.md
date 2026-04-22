# APIServicesApi

All URIs are relative to *https://api-scrapix.promptcloud.com*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**collect**](#collect) | **POST** /v1/collect | Collect Endpoint|
|[**crawl**](#crawl) | **POST** /v1/crawl | Crawl Endpoint|
|[**echo**](#echo) | **POST** /v1/echo | Echo|
|[**extract**](#extract) | **POST** /v1/extract | Extract Endpoint|
|[**scrape**](#scrape) | **POST** /v1/scrape | Scrape Endpoint|

# **collect**
> CollectResult collect(collectInput)


### Example

```typescript
import {
    APIServicesApi,
    Configuration,
    CollectInput
} from '@promptcloud/scrapix';

const configuration = new Configuration();
const apiInstance = new APIServicesApi(configuration);

let collectInput: CollectInput; //

const { status, data } = await apiInstance.collect(
    collectInput
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **collectInput** | **CollectInput**|  | |


### Return type

**CollectResult**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful Response |  -  |
|**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crawl**
> CrawlResult crawl(crawlInput)


### Example

```typescript
import {
    APIServicesApi,
    Configuration,
    CrawlInput
} from '@promptcloud/scrapix';

const configuration = new Configuration();
const apiInstance = new APIServicesApi(configuration);

let crawlInput: CrawlInput; //

const { status, data } = await apiInstance.crawl(
    crawlInput
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **crawlInput** | **CrawlInput**|  | |


### Return type

**CrawlResult**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful Response |  -  |
|**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **echo**
> any echo()


### Example

```typescript
import {
    APIServicesApi,
    Configuration
} from '@promptcloud/scrapix';

const configuration = new Configuration();
const apiInstance = new APIServicesApi(configuration);

const { status, data } = await apiInstance.echo();
```

### Parameters
This endpoint does not have any parameters.


### Return type

**any**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extract**
> ExtractResult extract(extractInput)


### Example

```typescript
import {
    APIServicesApi,
    Configuration,
    ExtractInput
} from '@promptcloud/scrapix';

const configuration = new Configuration();
const apiInstance = new APIServicesApi(configuration);

let extractInput: ExtractInput; //

const { status, data } = await apiInstance.extract(
    extractInput
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **extractInput** | **ExtractInput**|  | |


### Return type

**ExtractResult**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful Response |  -  |
|**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scrape**
> ScrapeResult scrape(scrapeInput)


### Example

```typescript
import {
    APIServicesApi,
    Configuration,
    ScrapeInput
} from '@promptcloud/scrapix';

const configuration = new Configuration();
const apiInstance = new APIServicesApi(configuration);

let scrapeInput: ScrapeInput; //

const { status, data } = await apiInstance.scrape(
    scrapeInput
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **scrapeInput** | **ScrapeInput**|  | |


### Return type

**ScrapeResult**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful Response |  -  |
|**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

