# StructuredOutput

Structured output model for the response. This model is used to represent structured data extracted from the response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **string** | Structured data extracted from the response | [default to undefined]
**data_schema** | **{ [key: string]: any; }** |  | [optional] [default to undefined]
**format** | [**StructuredOutputFormat**](StructuredOutputFormat.md) | Format of the structured output | [optional] [default to undefined]
**cost** | **number** | Cost incurred for generating the structured output | [optional] [default to 0.0]

## Example

```typescript
import { StructuredOutput } from '@promptcloud/scrapix';

const instance: StructuredOutput = {
    data,
    data_schema,
    format,
    cost,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
