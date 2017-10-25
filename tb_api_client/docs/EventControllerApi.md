# swagger_client.EventControllerApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_events_using_get**](EventControllerApi.md#get_events_using_get) | **GET** /api/events/{entityType}/{entityId}/{eventType} | getEvents
[**get_events_using_get1**](EventControllerApi.md#get_events_using_get1) | **GET** /api/events/{entityType}/{entityId} | getEvents


# **get_events_using_get**
> TimePageDataEvent get_events_using_get(entity_type, entity_id, event_type, tenant_id, limit, start_time=start_time, end_time=end_time, asc_order=asc_order, offset=offset)

getEvents

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: X-Authorization
configuration = swagger_client.Configuration()
configuration.api_key['X-Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.EventControllerApi(swagger_client.ApiClient(configuration))
entity_type = 'entity_type_example' # str | entityType
entity_id = 'entity_id_example' # str | entityId
event_type = 'event_type_example' # str | eventType
tenant_id = 'tenant_id_example' # str | tenantId
limit = 56 # int | limit
start_time = 789 # int | startTime (optional)
end_time = 789 # int | endTime (optional)
asc_order = false # bool | ascOrder (optional) (default to false)
offset = 'offset_example' # str | offset (optional)

try: 
    # getEvents
    api_response = api_instance.get_events_using_get(entity_type, entity_id, event_type, tenant_id, limit, start_time=start_time, end_time=end_time, asc_order=asc_order, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventControllerApi->get_events_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**| entityType | 
 **entity_id** | **str**| entityId | 
 **event_type** | **str**| eventType | 
 **tenant_id** | **str**| tenantId | 
 **limit** | **int**| limit | 
 **start_time** | **int**| startTime | [optional] 
 **end_time** | **int**| endTime | [optional] 
 **asc_order** | **bool**| ascOrder | [optional] [default to false]
 **offset** | **str**| offset | [optional] 

### Return type

[**TimePageDataEvent**](TimePageDataEvent.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_events_using_get1**
> TimePageDataEvent get_events_using_get1(entity_type, entity_id, tenant_id, limit, start_time=start_time, end_time=end_time, asc_order=asc_order, offset=offset)

getEvents

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: X-Authorization
configuration = swagger_client.Configuration()
configuration.api_key['X-Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.EventControllerApi(swagger_client.ApiClient(configuration))
entity_type = 'entity_type_example' # str | entityType
entity_id = 'entity_id_example' # str | entityId
tenant_id = 'tenant_id_example' # str | tenantId
limit = 56 # int | limit
start_time = 789 # int | startTime (optional)
end_time = 789 # int | endTime (optional)
asc_order = false # bool | ascOrder (optional) (default to false)
offset = 'offset_example' # str | offset (optional)

try: 
    # getEvents
    api_response = api_instance.get_events_using_get1(entity_type, entity_id, tenant_id, limit, start_time=start_time, end_time=end_time, asc_order=asc_order, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventControllerApi->get_events_using_get1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**| entityType | 
 **entity_id** | **str**| entityId | 
 **tenant_id** | **str**| tenantId | 
 **limit** | **int**| limit | 
 **start_time** | **int**| startTime | [optional] 
 **end_time** | **int**| endTime | [optional] 
 **asc_order** | **bool**| ascOrder | [optional] [default to false]
 **offset** | **str**| offset | [optional] 

### Return type

[**TimePageDataEvent**](TimePageDataEvent.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

