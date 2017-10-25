# swagger_client.PluginControllerApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_plugin_by_id_using_post**](PluginControllerApi.md#activate_plugin_by_id_using_post) | **POST** /api/plugin/{pluginId}/activate | activatePluginById
[**delete_plugin_using_delete**](PluginControllerApi.md#delete_plugin_using_delete) | **DELETE** /api/plugin/{pluginId} | deletePlugin
[**get_plugin_by_id_using_get**](PluginControllerApi.md#get_plugin_by_id_using_get) | **GET** /api/plugin/{pluginId} | getPluginById
[**get_plugin_by_token_using_get**](PluginControllerApi.md#get_plugin_by_token_using_get) | **GET** /api/plugin/token/{pluginToken} | getPluginByToken
[**get_plugins_using_get**](PluginControllerApi.md#get_plugins_using_get) | **GET** /api/plugins | getPlugins
[**get_system_plugins_using_get**](PluginControllerApi.md#get_system_plugins_using_get) | **GET** /api/plugin/system | getSystemPlugins
[**get_tenant_plugins_using_get**](PluginControllerApi.md#get_tenant_plugins_using_get) | **GET** /api/plugin/tenant/{tenantId} | getTenantPlugins
[**get_tenant_plugins_using_get1**](PluginControllerApi.md#get_tenant_plugins_using_get1) | **GET** /api/plugin | getTenantPlugins
[**save_plugin_using_post**](PluginControllerApi.md#save_plugin_using_post) | **POST** /api/plugin | savePlugin
[**suspend_plugin_by_id_using_post**](PluginControllerApi.md#suspend_plugin_by_id_using_post) | **POST** /api/plugin/{pluginId}/suspend | suspendPluginById


# **activate_plugin_by_id_using_post**
> activate_plugin_by_id_using_post(plugin_id)

activatePluginById

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
api_instance = swagger_client.PluginControllerApi(swagger_client.ApiClient(configuration))
plugin_id = 'plugin_id_example' # str | pluginId

try: 
    # activatePluginById
    api_instance.activate_plugin_by_id_using_post(plugin_id)
except ApiException as e:
    print("Exception when calling PluginControllerApi->activate_plugin_by_id_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plugin_id** | **str**| pluginId | 

### Return type

void (empty response body)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_plugin_using_delete**
> delete_plugin_using_delete(plugin_id)

deletePlugin

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
api_instance = swagger_client.PluginControllerApi(swagger_client.ApiClient(configuration))
plugin_id = 'plugin_id_example' # str | pluginId

try: 
    # deletePlugin
    api_instance.delete_plugin_using_delete(plugin_id)
except ApiException as e:
    print("Exception when calling PluginControllerApi->delete_plugin_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plugin_id** | **str**| pluginId | 

### Return type

void (empty response body)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_plugin_by_id_using_get**
> PluginMetaData get_plugin_by_id_using_get(plugin_id)

getPluginById

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
api_instance = swagger_client.PluginControllerApi(swagger_client.ApiClient(configuration))
plugin_id = 'plugin_id_example' # str | pluginId

try: 
    # getPluginById
    api_response = api_instance.get_plugin_by_id_using_get(plugin_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PluginControllerApi->get_plugin_by_id_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plugin_id** | **str**| pluginId | 

### Return type

[**PluginMetaData**](PluginMetaData.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_plugin_by_token_using_get**
> PluginMetaData get_plugin_by_token_using_get(plugin_token)

getPluginByToken

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
api_instance = swagger_client.PluginControllerApi(swagger_client.ApiClient(configuration))
plugin_token = 'plugin_token_example' # str | pluginToken

try: 
    # getPluginByToken
    api_response = api_instance.get_plugin_by_token_using_get(plugin_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PluginControllerApi->get_plugin_by_token_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plugin_token** | **str**| pluginToken | 

### Return type

[**PluginMetaData**](PluginMetaData.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_plugins_using_get**
> list[PluginMetaData] get_plugins_using_get()

getPlugins

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
api_instance = swagger_client.PluginControllerApi(swagger_client.ApiClient(configuration))

try: 
    # getPlugins
    api_response = api_instance.get_plugins_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PluginControllerApi->get_plugins_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[PluginMetaData]**](PluginMetaData.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_plugins_using_get**
> TextPageDataPluginMetaData get_system_plugins_using_get(limit, text_search=text_search, id_offset=id_offset, text_offset=text_offset)

getSystemPlugins

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
api_instance = swagger_client.PluginControllerApi(swagger_client.ApiClient(configuration))
limit = 'limit_example' # str | limit
text_search = 'text_search_example' # str | textSearch (optional)
id_offset = 'id_offset_example' # str | idOffset (optional)
text_offset = 'text_offset_example' # str | textOffset (optional)

try: 
    # getSystemPlugins
    api_response = api_instance.get_system_plugins_using_get(limit, text_search=text_search, id_offset=id_offset, text_offset=text_offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PluginControllerApi->get_system_plugins_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **str**| limit | 
 **text_search** | **str**| textSearch | [optional] 
 **id_offset** | **str**| idOffset | [optional] 
 **text_offset** | **str**| textOffset | [optional] 

### Return type

[**TextPageDataPluginMetaData**](TextPageDataPluginMetaData.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tenant_plugins_using_get**
> TextPageDataPluginMetaData get_tenant_plugins_using_get(tenant_id, limit, text_search=text_search, id_offset=id_offset, text_offset=text_offset)

getTenantPlugins

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
api_instance = swagger_client.PluginControllerApi(swagger_client.ApiClient(configuration))
tenant_id = 'tenant_id_example' # str | tenantId
limit = 'limit_example' # str | limit
text_search = 'text_search_example' # str | textSearch (optional)
id_offset = 'id_offset_example' # str | idOffset (optional)
text_offset = 'text_offset_example' # str | textOffset (optional)

try: 
    # getTenantPlugins
    api_response = api_instance.get_tenant_plugins_using_get(tenant_id, limit, text_search=text_search, id_offset=id_offset, text_offset=text_offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PluginControllerApi->get_tenant_plugins_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| tenantId | 
 **limit** | **str**| limit | 
 **text_search** | **str**| textSearch | [optional] 
 **id_offset** | **str**| idOffset | [optional] 
 **text_offset** | **str**| textOffset | [optional] 

### Return type

[**TextPageDataPluginMetaData**](TextPageDataPluginMetaData.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tenant_plugins_using_get1**
> TextPageDataPluginMetaData get_tenant_plugins_using_get1(limit, text_search=text_search, id_offset=id_offset, text_offset=text_offset)

getTenantPlugins

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
api_instance = swagger_client.PluginControllerApi(swagger_client.ApiClient(configuration))
limit = 'limit_example' # str | limit
text_search = 'text_search_example' # str | textSearch (optional)
id_offset = 'id_offset_example' # str | idOffset (optional)
text_offset = 'text_offset_example' # str | textOffset (optional)

try: 
    # getTenantPlugins
    api_response = api_instance.get_tenant_plugins_using_get1(limit, text_search=text_search, id_offset=id_offset, text_offset=text_offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PluginControllerApi->get_tenant_plugins_using_get1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **str**| limit | 
 **text_search** | **str**| textSearch | [optional] 
 **id_offset** | **str**| idOffset | [optional] 
 **text_offset** | **str**| textOffset | [optional] 

### Return type

[**TextPageDataPluginMetaData**](TextPageDataPluginMetaData.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_plugin_using_post**
> PluginMetaData save_plugin_using_post(source)

savePlugin

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
api_instance = swagger_client.PluginControllerApi(swagger_client.ApiClient(configuration))
source = swagger_client.PluginMetaData() # PluginMetaData | source

try: 
    # savePlugin
    api_response = api_instance.save_plugin_using_post(source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PluginControllerApi->save_plugin_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | [**PluginMetaData**](PluginMetaData.md)| source | 

### Return type

[**PluginMetaData**](PluginMetaData.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **suspend_plugin_by_id_using_post**
> suspend_plugin_by_id_using_post(plugin_id)

suspendPluginById

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
api_instance = swagger_client.PluginControllerApi(swagger_client.ApiClient(configuration))
plugin_id = 'plugin_id_example' # str | pluginId

try: 
    # suspendPluginById
    api_instance.suspend_plugin_by_id_using_post(plugin_id)
except ApiException as e:
    print("Exception when calling PluginControllerApi->suspend_plugin_by_id_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plugin_id** | **str**| pluginId | 

### Return type

void (empty response body)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

