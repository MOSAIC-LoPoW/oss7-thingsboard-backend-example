# swagger_client.PluginApiControllerApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**process_request_using_delete**](PluginApiControllerApi.md#process_request_using_delete) | **DELETE** /api/plugins/{pluginToken}/** | processRequest
[**process_request_using_get**](PluginApiControllerApi.md#process_request_using_get) | **GET** /api/plugins/{pluginToken}/** | processRequest
[**process_request_using_head**](PluginApiControllerApi.md#process_request_using_head) | **HEAD** /api/plugins/{pluginToken}/** | processRequest
[**process_request_using_options**](PluginApiControllerApi.md#process_request_using_options) | **OPTIONS** /api/plugins/{pluginToken}/** | processRequest
[**process_request_using_patch**](PluginApiControllerApi.md#process_request_using_patch) | **PATCH** /api/plugins/{pluginToken}/** | processRequest
[**process_request_using_post**](PluginApiControllerApi.md#process_request_using_post) | **POST** /api/plugins/{pluginToken}/** | processRequest
[**process_request_using_put**](PluginApiControllerApi.md#process_request_using_put) | **PUT** /api/plugins/{pluginToken}/** | processRequest


# **process_request_using_delete**
> DeferredResultResponseEntity process_request_using_delete(plugin_token)

processRequest

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
api_instance = swagger_client.PluginApiControllerApi(swagger_client.ApiClient(configuration))
plugin_token = 'plugin_token_example' # str | pluginToken

try: 
    # processRequest
    api_response = api_instance.process_request_using_delete(plugin_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PluginApiControllerApi->process_request_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plugin_token** | **str**| pluginToken | 

### Return type

[**DeferredResultResponseEntity**](DeferredResultResponseEntity.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **process_request_using_get**
> DeferredResultResponseEntity process_request_using_get(plugin_token)

processRequest

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
api_instance = swagger_client.PluginApiControllerApi(swagger_client.ApiClient(configuration))
plugin_token = 'plugin_token_example' # str | pluginToken

try: 
    # processRequest
    api_response = api_instance.process_request_using_get(plugin_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PluginApiControllerApi->process_request_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plugin_token** | **str**| pluginToken | 

### Return type

[**DeferredResultResponseEntity**](DeferredResultResponseEntity.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **process_request_using_head**
> DeferredResultResponseEntity process_request_using_head(plugin_token)

processRequest

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
api_instance = swagger_client.PluginApiControllerApi(swagger_client.ApiClient(configuration))
plugin_token = 'plugin_token_example' # str | pluginToken

try: 
    # processRequest
    api_response = api_instance.process_request_using_head(plugin_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PluginApiControllerApi->process_request_using_head: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plugin_token** | **str**| pluginToken | 

### Return type

[**DeferredResultResponseEntity**](DeferredResultResponseEntity.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **process_request_using_options**
> DeferredResultResponseEntity process_request_using_options(plugin_token)

processRequest

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
api_instance = swagger_client.PluginApiControllerApi(swagger_client.ApiClient(configuration))
plugin_token = 'plugin_token_example' # str | pluginToken

try: 
    # processRequest
    api_response = api_instance.process_request_using_options(plugin_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PluginApiControllerApi->process_request_using_options: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plugin_token** | **str**| pluginToken | 

### Return type

[**DeferredResultResponseEntity**](DeferredResultResponseEntity.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **process_request_using_patch**
> DeferredResultResponseEntity process_request_using_patch(plugin_token)

processRequest

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
api_instance = swagger_client.PluginApiControllerApi(swagger_client.ApiClient(configuration))
plugin_token = 'plugin_token_example' # str | pluginToken

try: 
    # processRequest
    api_response = api_instance.process_request_using_patch(plugin_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PluginApiControllerApi->process_request_using_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plugin_token** | **str**| pluginToken | 

### Return type

[**DeferredResultResponseEntity**](DeferredResultResponseEntity.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **process_request_using_post**
> DeferredResultResponseEntity process_request_using_post(plugin_token)

processRequest

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
api_instance = swagger_client.PluginApiControllerApi(swagger_client.ApiClient(configuration))
plugin_token = 'plugin_token_example' # str | pluginToken

try: 
    # processRequest
    api_response = api_instance.process_request_using_post(plugin_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PluginApiControllerApi->process_request_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plugin_token** | **str**| pluginToken | 

### Return type

[**DeferredResultResponseEntity**](DeferredResultResponseEntity.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **process_request_using_put**
> DeferredResultResponseEntity process_request_using_put(plugin_token)

processRequest

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
api_instance = swagger_client.PluginApiControllerApi(swagger_client.ApiClient(configuration))
plugin_token = 'plugin_token_example' # str | pluginToken

try: 
    # processRequest
    api_response = api_instance.process_request_using_put(plugin_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PluginApiControllerApi->process_request_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plugin_token** | **str**| pluginToken | 

### Return type

[**DeferredResultResponseEntity**](DeferredResultResponseEntity.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

