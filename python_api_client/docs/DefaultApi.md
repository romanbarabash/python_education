# client.DefaultApi

All URIs are relative to *http://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_task**](DefaultApi.md#create_task) | **POST** /tasks | Creates a &#39;Task&#39; object.
[**list_tasks**](DefaultApi.md#list_tasks) | **GET** /tasks | Lists the tasks
[**update_task**](DefaultApi.md#update_task) | **PUT** /tasks/{id} | Updates the details for a task.
[**view_task**](DefaultApi.md#view_task) | **GET** /tasks/{id} | Gets the details for a task.


# **create_task**
> create_task(body)

Creates a 'Task' object.

Allows for creating a task. 

### Example
```python
from __future__ import print_function
import time
import client
from client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = client.DefaultApi()
body = client.Task() # Task | The task to create

try:
    # Creates a 'Task' object.
    api_instance.create_task(body)
except ApiException as e:
    print("Exception when calling DefaultApi->create_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Task**](Task.md)| The task to create | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_tasks**
> list[Task] list_tasks()

Lists the tasks

List tasks. 

### Example
```python
from __future__ import print_function
import time
import client
from client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = client.DefaultApi()

try:
    # Lists the tasks
    api_response = api_instance.list_tasks()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_tasks: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Task]**](Task.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_task**
> Task update_task(id, body)

Updates the details for a task.

Allows for updating a task. 

### Example
```python
from __future__ import print_function
import time
import client
from client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = client.DefaultApi()
id = 'id_example' # str | The id of the task
body = client.Task() # Task | The task to update

try:
    # Updates the details for a task.
    api_response = api_instance.update_task(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The id of the task | 
 **body** | [**Task**](Task.md)| The task to update | 

### Return type

[**Task**](Task.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **view_task**
> Task view_task(id)

Gets the details for a task.

The details view of a task. 

### Example
```python
from __future__ import print_function
import time
import client
from client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = client.DefaultApi()
id = 'id_example' # str | The id of the task

try:
    # Gets the details for a task.
    api_response = api_instance.view_task(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->view_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The id of the task | 

### Return type

[**Task**](Task.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

