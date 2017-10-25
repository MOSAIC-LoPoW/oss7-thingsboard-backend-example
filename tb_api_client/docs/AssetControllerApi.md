# swagger_client.AssetControllerApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_asset_to_customer_using_post**](AssetControllerApi.md#assign_asset_to_customer_using_post) | **POST** /api/customer/{customerId}/asset/{assetId} | assignAssetToCustomer
[**assign_asset_to_public_customer_using_post**](AssetControllerApi.md#assign_asset_to_public_customer_using_post) | **POST** /api/customer/public/asset/{assetId} | assignAssetToPublicCustomer
[**delete_asset_using_delete**](AssetControllerApi.md#delete_asset_using_delete) | **DELETE** /api/asset/{assetId} | deleteAsset
[**find_by_query_using_post**](AssetControllerApi.md#find_by_query_using_post) | **POST** /api/assets | findByQuery
[**get_asset_by_id_using_get**](AssetControllerApi.md#get_asset_by_id_using_get) | **GET** /api/asset/{assetId} | getAssetById
[**get_asset_types_using_get**](AssetControllerApi.md#get_asset_types_using_get) | **GET** /api/asset/types | getAssetTypes
[**get_assets_by_ids_using_get**](AssetControllerApi.md#get_assets_by_ids_using_get) | **GET** /api/assets | getAssetsByIds
[**get_customer_assets_using_get**](AssetControllerApi.md#get_customer_assets_using_get) | **GET** /api/customer/{customerId}/assets | getCustomerAssets
[**get_tenant_assets_using_get**](AssetControllerApi.md#get_tenant_assets_using_get) | **GET** /api/tenant/assets | getTenantAssets
[**save_asset_using_post**](AssetControllerApi.md#save_asset_using_post) | **POST** /api/asset | saveAsset
[**unassign_asset_from_customer_using_delete**](AssetControllerApi.md#unassign_asset_from_customer_using_delete) | **DELETE** /api/customer/asset/{assetId} | unassignAssetFromCustomer


# **assign_asset_to_customer_using_post**
> Asset assign_asset_to_customer_using_post(customer_id, asset_id)

assignAssetToCustomer

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
api_instance = swagger_client.AssetControllerApi(swagger_client.ApiClient(configuration))
customer_id = 'customer_id_example' # str | customerId
asset_id = 'asset_id_example' # str | assetId

try: 
    # assignAssetToCustomer
    api_response = api_instance.assign_asset_to_customer_using_post(customer_id, asset_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetControllerApi->assign_asset_to_customer_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| customerId | 
 **asset_id** | **str**| assetId | 

### Return type

[**Asset**](Asset.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assign_asset_to_public_customer_using_post**
> Asset assign_asset_to_public_customer_using_post(asset_id)

assignAssetToPublicCustomer

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
api_instance = swagger_client.AssetControllerApi(swagger_client.ApiClient(configuration))
asset_id = 'asset_id_example' # str | assetId

try: 
    # assignAssetToPublicCustomer
    api_response = api_instance.assign_asset_to_public_customer_using_post(asset_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetControllerApi->assign_asset_to_public_customer_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**| assetId | 

### Return type

[**Asset**](Asset.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_asset_using_delete**
> delete_asset_using_delete(asset_id)

deleteAsset

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
api_instance = swagger_client.AssetControllerApi(swagger_client.ApiClient(configuration))
asset_id = 'asset_id_example' # str | assetId

try: 
    # deleteAsset
    api_instance.delete_asset_using_delete(asset_id)
except ApiException as e:
    print("Exception when calling AssetControllerApi->delete_asset_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**| assetId | 

### Return type

void (empty response body)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_by_query_using_post**
> list[Asset] find_by_query_using_post(query)

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
api_instance = swagger_client.AssetControllerApi(swagger_client.ApiClient(configuration))
query = swagger_client.AssetSearchQuery() # AssetSearchQuery | query

try: 
    # findByQuery
    api_response = api_instance.find_by_query_using_post(query)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetControllerApi->find_by_query_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | [**AssetSearchQuery**](AssetSearchQuery.md)| query | 

### Return type

[**list[Asset]**](Asset.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_by_id_using_get**
> Asset get_asset_by_id_using_get(asset_id)

getAssetById

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
api_instance = swagger_client.AssetControllerApi(swagger_client.ApiClient(configuration))
asset_id = 'asset_id_example' # str | assetId

try: 
    # getAssetById
    api_response = api_instance.get_asset_by_id_using_get(asset_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetControllerApi->get_asset_by_id_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**| assetId | 

### Return type

[**Asset**](Asset.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_types_using_get**
> list[EntitySubtype] get_asset_types_using_get()

getAssetTypes

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
api_instance = swagger_client.AssetControllerApi(swagger_client.ApiClient(configuration))

try: 
    # getAssetTypes
    api_response = api_instance.get_asset_types_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetControllerApi->get_asset_types_using_get: %s\n" % e)
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

# **get_assets_by_ids_using_get**
> list[Asset] get_assets_by_ids_using_get(asset_ids)

getAssetsByIds

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
api_instance = swagger_client.AssetControllerApi(swagger_client.ApiClient(configuration))
asset_ids = 'asset_ids_example' # str | assetIds

try: 
    # getAssetsByIds
    api_response = api_instance.get_assets_by_ids_using_get(asset_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetControllerApi->get_assets_by_ids_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_ids** | **str**| assetIds | 

### Return type

[**list[Asset]**](Asset.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_assets_using_get**
> TextPageDataAsset get_customer_assets_using_get(customer_id, limit, type=type, text_search=text_search, id_offset=id_offset, text_offset=text_offset)

getCustomerAssets

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
api_instance = swagger_client.AssetControllerApi(swagger_client.ApiClient(configuration))
customer_id = 'customer_id_example' # str | customerId
limit = 'limit_example' # str | limit
type = 'type_example' # str | type (optional)
text_search = 'text_search_example' # str | textSearch (optional)
id_offset = 'id_offset_example' # str | idOffset (optional)
text_offset = 'text_offset_example' # str | textOffset (optional)

try: 
    # getCustomerAssets
    api_response = api_instance.get_customer_assets_using_get(customer_id, limit, type=type, text_search=text_search, id_offset=id_offset, text_offset=text_offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetControllerApi->get_customer_assets_using_get: %s\n" % e)
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

[**TextPageDataAsset**](TextPageDataAsset.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tenant_assets_using_get**
> TextPageDataAsset get_tenant_assets_using_get(limit, type=type, text_search=text_search, id_offset=id_offset, text_offset=text_offset)

getTenantAssets

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
api_instance = swagger_client.AssetControllerApi(swagger_client.ApiClient(configuration))
limit = 'limit_example' # str | limit
type = 'type_example' # str | type (optional)
text_search = 'text_search_example' # str | textSearch (optional)
id_offset = 'id_offset_example' # str | idOffset (optional)
text_offset = 'text_offset_example' # str | textOffset (optional)

try: 
    # getTenantAssets
    api_response = api_instance.get_tenant_assets_using_get(limit, type=type, text_search=text_search, id_offset=id_offset, text_offset=text_offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetControllerApi->get_tenant_assets_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **str**| limit | 
 **type** | **str**| type | [optional] 
 **text_search** | **str**| textSearch | [optional] 
 **id_offset** | **str**| idOffset | [optional] 
 **text_offset** | **str**| textOffset | [optional] 

### Return type

[**TextPageDataAsset**](TextPageDataAsset.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_asset_using_post**
> Asset save_asset_using_post(asset)

saveAsset

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
api_instance = swagger_client.AssetControllerApi(swagger_client.ApiClient(configuration))
asset = swagger_client.Asset() # Asset | asset

try: 
    # saveAsset
    api_response = api_instance.save_asset_using_post(asset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetControllerApi->save_asset_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | [**Asset**](Asset.md)| asset | 

### Return type

[**Asset**](Asset.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unassign_asset_from_customer_using_delete**
> Asset unassign_asset_from_customer_using_delete(asset_id)

unassignAssetFromCustomer

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
api_instance = swagger_client.AssetControllerApi(swagger_client.ApiClient(configuration))
asset_id = 'asset_id_example' # str | assetId

try: 
    # unassignAssetFromCustomer
    api_response = api_instance.unassign_asset_from_customer_using_delete(asset_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetControllerApi->unassign_asset_from_customer_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**| assetId | 

### Return type

[**Asset**](Asset.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

