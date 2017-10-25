# swagger_client.AlarmControllerApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ack_alarm_using_post**](AlarmControllerApi.md#ack_alarm_using_post) | **POST** /api/alarm/{alarmId}/ack | ackAlarm
[**clear_alarm_using_post**](AlarmControllerApi.md#clear_alarm_using_post) | **POST** /api/alarm/{alarmId}/clear | clearAlarm
[**get_alarm_by_id_using_get**](AlarmControllerApi.md#get_alarm_by_id_using_get) | **GET** /api/alarm/{alarmId} | getAlarmById
[**get_alarm_info_by_id_using_get**](AlarmControllerApi.md#get_alarm_info_by_id_using_get) | **GET** /api/alarm/info/{alarmId} | getAlarmInfoById
[**get_alarms_using_get**](AlarmControllerApi.md#get_alarms_using_get) | **GET** /api/alarm/{entityType}/{entityId} | getAlarms
[**get_highest_alarm_severity_using_get**](AlarmControllerApi.md#get_highest_alarm_severity_using_get) | **GET** /api/alarm/highestSeverity/{entityType}/{entityId} | getHighestAlarmSeverity
[**save_alarm_using_post**](AlarmControllerApi.md#save_alarm_using_post) | **POST** /api/alarm | saveAlarm


# **ack_alarm_using_post**
> ack_alarm_using_post(alarm_id)

ackAlarm

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
api_instance = swagger_client.AlarmControllerApi(swagger_client.ApiClient(configuration))
alarm_id = 'alarm_id_example' # str | alarmId

try: 
    # ackAlarm
    api_instance.ack_alarm_using_post(alarm_id)
except ApiException as e:
    print("Exception when calling AlarmControllerApi->ack_alarm_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alarm_id** | **str**| alarmId | 

### Return type

void (empty response body)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clear_alarm_using_post**
> clear_alarm_using_post(alarm_id)

clearAlarm

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
api_instance = swagger_client.AlarmControllerApi(swagger_client.ApiClient(configuration))
alarm_id = 'alarm_id_example' # str | alarmId

try: 
    # clearAlarm
    api_instance.clear_alarm_using_post(alarm_id)
except ApiException as e:
    print("Exception when calling AlarmControllerApi->clear_alarm_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alarm_id** | **str**| alarmId | 

### Return type

void (empty response body)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alarm_by_id_using_get**
> Alarm get_alarm_by_id_using_get(alarm_id)

getAlarmById

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
api_instance = swagger_client.AlarmControllerApi(swagger_client.ApiClient(configuration))
alarm_id = 'alarm_id_example' # str | alarmId

try: 
    # getAlarmById
    api_response = api_instance.get_alarm_by_id_using_get(alarm_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlarmControllerApi->get_alarm_by_id_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alarm_id** | **str**| alarmId | 

### Return type

[**Alarm**](Alarm.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alarm_info_by_id_using_get**
> AlarmInfo get_alarm_info_by_id_using_get(alarm_id)

getAlarmInfoById

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
api_instance = swagger_client.AlarmControllerApi(swagger_client.ApiClient(configuration))
alarm_id = 'alarm_id_example' # str | alarmId

try: 
    # getAlarmInfoById
    api_response = api_instance.get_alarm_info_by_id_using_get(alarm_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlarmControllerApi->get_alarm_info_by_id_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alarm_id** | **str**| alarmId | 

### Return type

[**AlarmInfo**](AlarmInfo.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alarms_using_get**
> TimePageDataAlarmInfo get_alarms_using_get(entity_type, entity_id, limit, search_status=search_status, status=status, start_time=start_time, end_time=end_time, asc_order=asc_order, offset=offset, fetch_originator=fetch_originator)

getAlarms

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
api_instance = swagger_client.AlarmControllerApi(swagger_client.ApiClient(configuration))
entity_type = 'entity_type_example' # str | entityType
entity_id = 'entity_id_example' # str | entityId
limit = 56 # int | limit
search_status = 'search_status_example' # str | searchStatus (optional)
status = 'status_example' # str | status (optional)
start_time = 789 # int | startTime (optional)
end_time = 789 # int | endTime (optional)
asc_order = false # bool | ascOrder (optional) (default to false)
offset = 'offset_example' # str | offset (optional)
fetch_originator = true # bool | fetchOriginator (optional)

try: 
    # getAlarms
    api_response = api_instance.get_alarms_using_get(entity_type, entity_id, limit, search_status=search_status, status=status, start_time=start_time, end_time=end_time, asc_order=asc_order, offset=offset, fetch_originator=fetch_originator)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlarmControllerApi->get_alarms_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**| entityType | 
 **entity_id** | **str**| entityId | 
 **limit** | **int**| limit | 
 **search_status** | **str**| searchStatus | [optional] 
 **status** | **str**| status | [optional] 
 **start_time** | **int**| startTime | [optional] 
 **end_time** | **int**| endTime | [optional] 
 **asc_order** | **bool**| ascOrder | [optional] [default to false]
 **offset** | **str**| offset | [optional] 
 **fetch_originator** | **bool**| fetchOriginator | [optional] 

### Return type

[**TimePageDataAlarmInfo**](TimePageDataAlarmInfo.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_highest_alarm_severity_using_get**
> str get_highest_alarm_severity_using_get(entity_type, entity_id, search_status=search_status, status=status)

getHighestAlarmSeverity

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
api_instance = swagger_client.AlarmControllerApi(swagger_client.ApiClient(configuration))
entity_type = 'entity_type_example' # str | entityType
entity_id = 'entity_id_example' # str | entityId
search_status = 'search_status_example' # str | searchStatus (optional)
status = 'status_example' # str | status (optional)

try: 
    # getHighestAlarmSeverity
    api_response = api_instance.get_highest_alarm_severity_using_get(entity_type, entity_id, search_status=search_status, status=status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlarmControllerApi->get_highest_alarm_severity_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**| entityType | 
 **entity_id** | **str**| entityId | 
 **search_status** | **str**| searchStatus | [optional] 
 **status** | **str**| status | [optional] 

### Return type

**str**

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_alarm_using_post**
> Alarm save_alarm_using_post(alarm)

saveAlarm

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
api_instance = swagger_client.AlarmControllerApi(swagger_client.ApiClient(configuration))
alarm = swagger_client.Alarm() # Alarm | alarm

try: 
    # saveAlarm
    api_response = api_instance.save_alarm_using_post(alarm)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlarmControllerApi->save_alarm_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alarm** | [**Alarm**](Alarm.md)| alarm | 

### Return type

[**Alarm**](Alarm.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

