# swagger_client.WidgetsBundleControllerApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_widgets_bundle_using_delete**](WidgetsBundleControllerApi.md#delete_widgets_bundle_using_delete) | **DELETE** /api/widgetsBundle/{widgetsBundleId} | deleteWidgetsBundle
[**get_widgets_bundle_by_id_using_get**](WidgetsBundleControllerApi.md#get_widgets_bundle_by_id_using_get) | **GET** /api/widgetsBundle/{widgetsBundleId} | getWidgetsBundleById
[**get_widgets_bundles_using_get**](WidgetsBundleControllerApi.md#get_widgets_bundles_using_get) | **GET** /api/widgetsBundles | getWidgetsBundles
[**save_widgets_bundle_using_post**](WidgetsBundleControllerApi.md#save_widgets_bundle_using_post) | **POST** /api/widgetsBundle | saveWidgetsBundle


# **delete_widgets_bundle_using_delete**
> delete_widgets_bundle_using_delete(widgets_bundle_id)

deleteWidgetsBundle

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
api_instance = swagger_client.WidgetsBundleControllerApi(swagger_client.ApiClient(configuration))
widgets_bundle_id = 'widgets_bundle_id_example' # str | widgetsBundleId

try: 
    # deleteWidgetsBundle
    api_instance.delete_widgets_bundle_using_delete(widgets_bundle_id)
except ApiException as e:
    print("Exception when calling WidgetsBundleControllerApi->delete_widgets_bundle_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **widgets_bundle_id** | **str**| widgetsBundleId | 

### Return type

void (empty response body)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_widgets_bundle_by_id_using_get**
> WidgetsBundle get_widgets_bundle_by_id_using_get(widgets_bundle_id)

getWidgetsBundleById

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
api_instance = swagger_client.WidgetsBundleControllerApi(swagger_client.ApiClient(configuration))
widgets_bundle_id = 'widgets_bundle_id_example' # str | widgetsBundleId

try: 
    # getWidgetsBundleById
    api_response = api_instance.get_widgets_bundle_by_id_using_get(widgets_bundle_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WidgetsBundleControllerApi->get_widgets_bundle_by_id_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **widgets_bundle_id** | **str**| widgetsBundleId | 

### Return type

[**WidgetsBundle**](WidgetsBundle.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_widgets_bundles_using_get**
> TextPageDataWidgetsBundle get_widgets_bundles_using_get(limit, text_search=text_search, id_offset=id_offset, text_offset=text_offset)

getWidgetsBundles

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
api_instance = swagger_client.WidgetsBundleControllerApi(swagger_client.ApiClient(configuration))
limit = 'limit_example' # str | limit
text_search = 'text_search_example' # str | textSearch (optional)
id_offset = 'id_offset_example' # str | idOffset (optional)
text_offset = 'text_offset_example' # str | textOffset (optional)

try: 
    # getWidgetsBundles
    api_response = api_instance.get_widgets_bundles_using_get(limit, text_search=text_search, id_offset=id_offset, text_offset=text_offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WidgetsBundleControllerApi->get_widgets_bundles_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **str**| limit | 
 **text_search** | **str**| textSearch | [optional] 
 **id_offset** | **str**| idOffset | [optional] 
 **text_offset** | **str**| textOffset | [optional] 

### Return type

[**TextPageDataWidgetsBundle**](TextPageDataWidgetsBundle.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_widgets_bundle_using_post**
> WidgetsBundle save_widgets_bundle_using_post(widgets_bundle)

saveWidgetsBundle

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
api_instance = swagger_client.WidgetsBundleControllerApi(swagger_client.ApiClient(configuration))
widgets_bundle = swagger_client.WidgetsBundle() # WidgetsBundle | widgetsBundle

try: 
    # saveWidgetsBundle
    api_response = api_instance.save_widgets_bundle_using_post(widgets_bundle)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WidgetsBundleControllerApi->save_widgets_bundle_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **widgets_bundle** | [**WidgetsBundle**](WidgetsBundle.md)| widgetsBundle | 

### Return type

[**WidgetsBundle**](WidgetsBundle.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

