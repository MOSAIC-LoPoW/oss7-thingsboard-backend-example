# swagger_client.ComponentDescriptorControllerApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_component_descriptor_by_clazz_using_get**](ComponentDescriptorControllerApi.md#get_component_descriptor_by_clazz_using_get) | **GET** /api/component/{componentDescriptorClazz} | getComponentDescriptorByClazz
[**get_component_descriptors_by_type_using_get**](ComponentDescriptorControllerApi.md#get_component_descriptors_by_type_using_get) | **GET** /api/components/{componentType} | getComponentDescriptorsByType
[**get_plugin_actions_by_plugin_clazz_using_get**](ComponentDescriptorControllerApi.md#get_plugin_actions_by_plugin_clazz_using_get) | **GET** /api/components/actions/{pluginClazz} | getPluginActionsByPluginClazz


# **get_component_descriptor_by_clazz_using_get**
> ComponentDescriptor get_component_descriptor_by_clazz_using_get(component_descriptor_clazz)

getComponentDescriptorByClazz

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
api_instance = swagger_client.ComponentDescriptorControllerApi(swagger_client.ApiClient(configuration))
component_descriptor_clazz = 'component_descriptor_clazz_example' # str | componentDescriptorClazz

try: 
    # getComponentDescriptorByClazz
    api_response = api_instance.get_component_descriptor_by_clazz_using_get(component_descriptor_clazz)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComponentDescriptorControllerApi->get_component_descriptor_by_clazz_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **component_descriptor_clazz** | **str**| componentDescriptorClazz | 

### Return type

[**ComponentDescriptor**](ComponentDescriptor.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_component_descriptors_by_type_using_get**
> list[ComponentDescriptor] get_component_descriptors_by_type_using_get(component_type)

getComponentDescriptorsByType

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
api_instance = swagger_client.ComponentDescriptorControllerApi(swagger_client.ApiClient(configuration))
component_type = 'component_type_example' # str | componentType

try: 
    # getComponentDescriptorsByType
    api_response = api_instance.get_component_descriptors_by_type_using_get(component_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComponentDescriptorControllerApi->get_component_descriptors_by_type_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **component_type** | **str**| componentType | 

### Return type

[**list[ComponentDescriptor]**](ComponentDescriptor.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_plugin_actions_by_plugin_clazz_using_get**
> list[ComponentDescriptor] get_plugin_actions_by_plugin_clazz_using_get(plugin_clazz)

getPluginActionsByPluginClazz

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
api_instance = swagger_client.ComponentDescriptorControllerApi(swagger_client.ApiClient(configuration))
plugin_clazz = 'plugin_clazz_example' # str | pluginClazz

try: 
    # getPluginActionsByPluginClazz
    api_response = api_instance.get_plugin_actions_by_plugin_clazz_using_get(plugin_clazz)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComponentDescriptorControllerApi->get_plugin_actions_by_plugin_clazz_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plugin_clazz** | **str**| pluginClazz | 

### Return type

[**list[ComponentDescriptor]**](ComponentDescriptor.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

