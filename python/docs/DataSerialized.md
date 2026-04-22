# DataSerialized


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**format** | [**OutputFormat**](OutputFormat.md) |  | 
**data** | **str** |  | 

## Example

```python
from scrapix.models.data_serialized import DataSerialized

# TODO update the JSON string below
json = "{}"
# create an instance of DataSerialized from a JSON string
data_serialized_instance = DataSerialized.from_json(json)
# print the JSON string representation of the object
print(DataSerialized.to_json())

# convert the object into a dict
data_serialized_dict = data_serialized_instance.to_dict()
# create an instance of DataSerialized from a dict
data_serialized_from_dict = DataSerialized.from_dict(data_serialized_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


