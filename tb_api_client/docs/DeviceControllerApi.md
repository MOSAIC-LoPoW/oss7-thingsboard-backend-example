# swagger_client.DeviceControllerApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_device_to_customer_using_post**](DeviceControllerApi.md#assign_device_to_customer_using_post) | **POST** /api/customer/{customerId}/device/{deviceId} | assignDeviceToCustomer
[**assign_device_to_public_customer_using_post**](DeviceControllerApi.md#assign_device_to_public_customer_using_post) | **POST** /api/customer/public/device/{deviceId} | assignDeviceToPublicCustomer
[**delete_device_using_delete**](DeviceControllerApi.md#delete_device_using_delete) | **DELETE** /api/device/{deviceId} | deleteDevice
[**find_by_query_using_post1**](DeviceControllerApi.md#find_by_query_using_post1) | **POST** /api/devices | findByQuery
[**get_customer_devices_using_get**](DeviceControllerApi.md#get_customer_devices_using_get) | **GET** /api/customer/{customerId}/devices | getCustomerDevices
[**get_device_by_id_using_get**](DeviceControllerApi.md#get_device_by_id_using_get) | **GET** /api/device/{deviceId} | getDeviceById
[**get_device_credentials_by_device_id_using_get**](DeviceControllerApi.md#get_device_credentials_by_device_id_using_get) | **GET** /api/device/{deviceId}/credentials | getDeviceCredentialsByDeviceId
[**get_device_types_using_get**](DeviceControllerApi.md#get_device_types_using_get) | **GET** /api/device/types | getDeviceTypes
[**get_devices_by_ids_using_get**](DeviceControllerApi.md#get_devices_by_ids_using_get) | **GET** /api/devices | getDevicesByIds
[**get_tenant_device_using_get**](DeviceControllerApi.md#get_tenant_device_using_get) | **GET** /api/tenant/devices | getTenantDevice
[**save_device_credentials_using_post**](DeviceControllerApi.md#save_device_credentials_using_post) | **POST** /api/device/credentials | saveDeviceCredentials
[**save_device_using_post**](DeviceControllerApi.md#save_device_using_post) | **POST** /api/device | saveDevice
[**unassign_device_from_customer_using_delete**](DeviceControllerApi.md#unassign_device_from_customer_using_delete) | **DELETE** /api/customer/device/{deviceId} | unassignDeviceFromCustomer


# **assign_device_to_customer_using_post**
> Device assign_device_to_customer_using_post(customer_id, device_id)

assignDeviceToCustomer

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
api_instance = swagger_client.DeviceControllerApi(swagger_client.ApiClient(configuration))
customer_id = 'customer_id_example' # str | customerId
device_id = 'device_id_example' # str | deviceId

try: 
    # assignDeviceToCustomer
    api_response = api_instance.assign_device_to_customer_using_post(customer_id, device_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceControllerApi->assign_device_to_customer_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| customerId | 
 **device_id** | **str**| deviceId | 

### Return type

[**Device**](Device.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assign_device_to_public_customer_using_post**
> Device assign_device_to_public_customer_using_post(device_id)

assignDeviceToPublicCustomer

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
api_instance = swagger_client.DeviceControllerApi(swagger_client.ApiClient(configuration))
device_id = 'device_id_example' # str | deviceId

try: 
    # assignDeviceToPublicCustomer
    api_response = api_instance.assign_device_to_public_customer_using_post(device_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceControllerApi->assign_device_to_public_customer_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| deviceId | 

### Return type

[**Device**](Device.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_device_using_delete**
> delete_device_using_delete(device_id)

deleteDevice

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
api_instance = swagger_client.DeviceControllerApi(swagger_client.ApiClient(configuration))
device_id = 'device_id_example' # str | deviceId

try: 
    # deleteDevice
    api_instance.delete_device_using_delete(device_id)
except ApiException as e:
    print("Exception when calling DeviceControllerApi->delete_device_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| deviceId | 

### Return type

void (empty response body)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_by_query_using_post1**
> list[Device] find_by_query_using_post1(query)

findByQuery

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
api_instance = swagger_client.DeviceControllerApi(swagger_client.ApiClient(configuration))
query = swagger_client.DeviceSearchQuery() # DeviceSearchQuery | query

try: 
    # findByQuery
    api_response = api_instance.find_by_query_using_post1(query)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceControllerApi->find_by_query_using_post1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | [**DeviceSearchQuery**](DeviceSearchQuery.md)| query | 

### Return type

[**list[Device]**](Device.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_devices_using_get**
> TextPageDataDevice get_customer_devices_using_get(customer_id, limit, type=type, text_search=text_search, id_offset=id_offset, text_offset=text_offset)

getCustomerDevices

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
api_instance = swagger_client.DeviceControllerApi(swagger_client.ApiClient(configuration))
customer_id = 'customer_id_example' # str | customerId
limit = 'limit_example' # str | limit
type = 'type_example' # str | type (optional)
text_search = 'text_search_example' # str | textSearch (optional)
id_offset = 'id_offset_example' # str | idOffset (optional)
text_offset = 'text_offset_example' # str | textOffset (optional)

try: 
    # getCustomerDevices
    api_response = api_instance.get_customer_devices_using_get(customer_id, limit, type=type, text_search=text_search, id_offset=id_offset, text_offset=text_offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceControllerApi->get_customer_devices_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| customerId | 
 **limit** | **str**| limit | 
 **type** | **str**| type | [optional] 
 **text_search** | **str**| textSearch | [optional] 
 **id_offset** | **str**| idOffset | [optional] 
 **text_offset** | **str**| textOffset | [optional] 

### Return type

[**TextPageDataDevice**](TextPageDataDevice.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_by_id_using_get**
> Device get_device_by_id_using_get(device_id)

getDeviceById

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
api_instance = swagger_client.DeviceControllerApi(swagger_client.ApiClient(configuration))
device_id = 'device_id_example' # str | deviceId

try: 
    # getDeviceById
    api_response = api_instance.get_device_by_id_using_get(device_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceControllerApi->get_device_by_id_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| deviceId | 

### Return type

[**Device**](Device.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_credentials_by_device_id_using_get**
> DeviceCredentials get_device_credentials_by_device_id_using_get(device_id)

getDeviceCredentialsByDeviceId

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
api_instance = swagger_client.DeviceControllerApi(swagger_client.ApiClient(configuration))
device_id = 'device_id_example' # str | deviceId

try: 
    # getDeviceCredentialsByDeviceId
    api_response = api_instance.get_device_credentials_by_device_id_using_get(device_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceControllerApi->get_device_credentials_by_device_id_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| deviceId | 

### Return type

[**DeviceCredentials**](DeviceCredentials.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_types_using_get**
> list[EntitySubtype] get_device_types_using_get()

getDeviceTypes

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
api_instance = swagger_client.DeviceControllerApi(swagger_client.ApiClient(configuration))

try: 
    # getDeviceTypes
    api_response = api_instance.get_device_types_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceControllerApi->get_device_types_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[EntitySubtype]**](EntitySubtype.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_devices_by_ids_using_get**
> list[Device] get_devices_by_ids_using_get(device_ids)

getDevicesByIds

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
api_instance = swagger_client.DeviceControllerApi(swagger_client.ApiClient(configuration))
device_ids = 'device_ids_example' # str | deviceIds

try: 
    # getDevicesByIds
    api_response = api_instance.get_devices_by_ids_using_get(device_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceControllerApi->get_devices_by_ids_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_ids** | **str**| deviceIds | 

### Return type

[**list[Device]**](Device.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tenant_device_using_get**
> Device get_tenant_device_using_get(device_name)

getTenantDevice

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
api_instance = swagger_client.DeviceControllerApi(swagger_client.ApiClient(configuration))
device_name = 'device_name_example' # str | deviceName

try: 
    # getTenantDevice
    api_response = api_instance.get_tenant_device_using_get(device_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceControllerApi->get_tenant_device_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_name** | **str**| deviceName | 

### Return type

[**Device**](Device.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_device_credentials_using_post**
> DeviceCredentials save_device_credentials_using_post(device_credentials)

saveDeviceCredentials

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
api_instance = swagger_client.DeviceControllerApi(swagger_client.ApiClient(configuration))
device_credentials = swagger_client.DeviceCredentials() # DeviceCredentials | deviceCredentials

try: 
    # saveDeviceCredentials
    api_response = api_instance.save_device_credentials_using_post(device_credentials)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceControllerApi->save_device_credentials_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_credentials** | [**DeviceCredentials**](DeviceCredentials.md)| deviceCredentials | 

### Return type

[**DeviceCredentials**](DeviceCredentials.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_device_using_post**
> Device save_device_using_post(device)

saveDevice

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
api_instance = swagger_client.DeviceControllerApi(swagger_client.ApiClient(configuration))
device = swagger_client.Device() # Device | device

try: 
    # saveDevice
    api_response = api_instance.save_device_using_post(device)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceControllerApi->save_device_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device** | [**Device**](Device.md)| device | 

### Return type

[**Device**](Device.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unassign_device_from_customer_using_delete**
> Device unassign_device_from_customer_using_delete(device_id)

unassignDeviceFromCustomer

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
api_instance = swagger_client.DeviceControllerApi(swagger_client.ApiClient(configuration))
device_id = 'device_id_example' # str | deviceId

try: 
    # unassignDeviceFromCustomer
    api_response = api_instance.unassign_device_from_customer_using_delete(device_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceControllerApi->unassign_device_from_customer_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| deviceId | 

### Return type

[**Device**](Device.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

