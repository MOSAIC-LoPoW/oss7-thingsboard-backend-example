# swagger_client.RuleControllerApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_rule_by_id_using_post**](RuleControllerApi.md#activate_rule_by_id_using_post) | **POST** /api/rule/{ruleId}/activate | activateRuleById
[**delete_rule_using_delete**](RuleControllerApi.md#delete_rule_using_delete) | **DELETE** /api/rule/{ruleId} | deleteRule
[**get_rule_by_id_using_get**](RuleControllerApi.md#get_rule_by_id_using_get) | **GET** /api/rule/{ruleId} | getRuleById
[**get_rules_by_plugin_token_using_get**](RuleControllerApi.md#get_rules_by_plugin_token_using_get) | **GET** /api/rule/token/{pluginToken} | getRulesByPluginToken
[**get_rules_using_get**](RuleControllerApi.md#get_rules_using_get) | **GET** /api/rules | getRules
[**get_system_rules_using_get**](RuleControllerApi.md#get_system_rules_using_get) | **GET** /api/rule/system | getSystemRules
[**get_tenant_rules_using_get**](RuleControllerApi.md#get_tenant_rules_using_get) | **GET** /api/rule/tenant/{tenantId} | getTenantRules
[**get_tenant_rules_using_get1**](RuleControllerApi.md#get_tenant_rules_using_get1) | **GET** /api/rule | getTenantRules
[**save_rule_using_post**](RuleControllerApi.md#save_rule_using_post) | **POST** /api/rule | saveRule
[**suspend_rule_by_id_using_post**](RuleControllerApi.md#suspend_rule_by_id_using_post) | **POST** /api/rule/{ruleId}/suspend | suspendRuleById


# **activate_rule_by_id_using_post**
> activate_rule_by_id_using_post(rule_id)

activateRuleById

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
api_instance = swagger_client.RuleControllerApi(swagger_client.ApiClient(configuration))
rule_id = 'rule_id_example' # str | ruleId

try: 
    # activateRuleById
    api_instance.activate_rule_by_id_using_post(rule_id)
except ApiException as e:
    print("Exception when calling RuleControllerApi->activate_rule_by_id_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**| ruleId | 

### Return type

void (empty response body)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_rule_using_delete**
> delete_rule_using_delete(rule_id)

deleteRule

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
api_instance = swagger_client.RuleControllerApi(swagger_client.ApiClient(configuration))
rule_id = 'rule_id_example' # str | ruleId

try: 
    # deleteRule
    api_instance.delete_rule_using_delete(rule_id)
except ApiException as e:
    print("Exception when calling RuleControllerApi->delete_rule_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**| ruleId | 

### Return type

void (empty response body)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rule_by_id_using_get**
> RuleMetaData get_rule_by_id_using_get(rule_id)

getRuleById

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
api_instance = swagger_client.RuleControllerApi(swagger_client.ApiClient(configuration))
rule_id = 'rule_id_example' # str | ruleId

try: 
    # getRuleById
    api_response = api_instance.get_rule_by_id_using_get(rule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RuleControllerApi->get_rule_by_id_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**| ruleId | 

### Return type

[**RuleMetaData**](RuleMetaData.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rules_by_plugin_token_using_get**
> list[RuleMetaData] get_rules_by_plugin_token_using_get(plugin_token)

getRulesByPluginToken

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
api_instance = swagger_client.RuleControllerApi(swagger_client.ApiClient(configuration))
plugin_token = 'plugin_token_example' # str | pluginToken

try: 
    # getRulesByPluginToken
    api_response = api_instance.get_rules_by_plugin_token_using_get(plugin_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RuleControllerApi->get_rules_by_plugin_token_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plugin_token** | **str**| pluginToken | 

### Return type

[**list[RuleMetaData]**](RuleMetaData.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rules_using_get**
> list[RuleMetaData] get_rules_using_get()

getRules

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
api_instance = swagger_client.RuleControllerApi(swagger_client.ApiClient(configuration))

try: 
    # getRules
    api_response = api_instance.get_rules_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RuleControllerApi->get_rules_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[RuleMetaData]**](RuleMetaData.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_rules_using_get**
> TextPageDataRuleMetaData get_system_rules_using_get(limit, text_search=text_search, id_offset=id_offset, text_offset=text_offset)

getSystemRules

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
api_instance = swagger_client.RuleControllerApi(swagger_client.ApiClient(configuration))
limit = 'limit_example' # str | limit
text_search = 'text_search_example' # str | textSearch (optional)
id_offset = 'id_offset_example' # str | idOffset (optional)
text_offset = 'text_offset_example' # str | textOffset (optional)

try: 
    # getSystemRules
    api_response = api_instance.get_system_rules_using_get(limit, text_search=text_search, id_offset=id_offset, text_offset=text_offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RuleControllerApi->get_system_rules_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **str**| limit | 
 **text_search** | **str**| textSearch | [optional] 
 **id_offset** | **str**| idOffset | [optional] 
 **text_offset** | **str**| textOffset | [optional] 

### Return type

[**TextPageDataRuleMetaData**](TextPageDataRuleMetaData.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tenant_rules_using_get**
> TextPageDataRuleMetaData get_tenant_rules_using_get(tenant_id, limit, text_search=text_search, id_offset=id_offset, text_offset=text_offset)

getTenantRules

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
api_instance = swagger_client.RuleControllerApi(swagger_client.ApiClient(configuration))
tenant_id = 'tenant_id_example' # str | tenantId
limit = 'limit_example' # str | limit
text_search = 'text_search_example' # str | textSearch (optional)
id_offset = 'id_offset_example' # str | idOffset (optional)
text_offset = 'text_offset_example' # str | textOffset (optional)

try: 
    # getTenantRules
    api_response = api_instance.get_tenant_rules_using_get(tenant_id, limit, text_search=text_search, id_offset=id_offset, text_offset=text_offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RuleControllerApi->get_tenant_rules_using_get: %s\n" % e)
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

[**TextPageDataRuleMetaData**](TextPageDataRuleMetaData.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tenant_rules_using_get1**
> TextPageDataRuleMetaData get_tenant_rules_using_get1(limit, text_search=text_search, id_offset=id_offset, text_offset=text_offset)

getTenantRules

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
api_instance = swagger_client.RuleControllerApi(swagger_client.ApiClient(configuration))
limit = 'limit_example' # str | limit
text_search = 'text_search_example' # str | textSearch (optional)
id_offset = 'id_offset_example' # str | idOffset (optional)
text_offset = 'text_offset_example' # str | textOffset (optional)

try: 
    # getTenantRules
    api_response = api_instance.get_tenant_rules_using_get1(limit, text_search=text_search, id_offset=id_offset, text_offset=text_offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RuleControllerApi->get_tenant_rules_using_get1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **str**| limit | 
 **text_search** | **str**| textSearch | [optional] 
 **id_offset** | **str**| idOffset | [optional] 
 **text_offset** | **str**| textOffset | [optional] 

### Return type

[**TextPageDataRuleMetaData**](TextPageDataRuleMetaData.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_rule_using_post**
> RuleMetaData save_rule_using_post(source)

saveRule

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
api_instance = swagger_client.RuleControllerApi(swagger_client.ApiClient(configuration))
source = swagger_client.RuleMetaData() # RuleMetaData | source

try: 
    # saveRule
    api_response = api_instance.save_rule_using_post(source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RuleControllerApi->save_rule_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | [**RuleMetaData**](RuleMetaData.md)| source | 

### Return type

[**RuleMetaData**](RuleMetaData.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **suspend_rule_by_id_using_post**
> suspend_rule_by_id_using_post(rule_id)

suspendRuleById

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
api_instance = swagger_client.RuleControllerApi(swagger_client.ApiClient(configuration))
rule_id = 'rule_id_example' # str | ruleId

try: 
    # suspendRuleById
    api_instance.suspend_rule_by_id_using_post(rule_id)
except ApiException as e:
    print("Exception when calling RuleControllerApi->suspend_rule_by_id_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**| ruleId | 

### Return type

void (empty response body)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

