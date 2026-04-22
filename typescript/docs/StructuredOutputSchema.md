# StructuredOutputSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**format** | [**StructuredOutputFormat**](StructuredOutputFormat.md) | The format of the structured output schema | [optional] [default to undefined]
**schema** | **{ [key: string]: any; }** |  | [optional] [default to undefined]
**query** | **string** | A user query on what to extract from the structured output | [default to undefined]

## Example

```typescript
import { StructuredOutputSchema } from '@promptcloud/scrapix';

const instance: StructuredOutputSchema = {
    format,
    schema,
    query,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
