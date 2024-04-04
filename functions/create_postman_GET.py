import requests
import json
test_script = 'console.log()'

def read_curl_file(file_path):
    with open(file_path, 'r') as file:
        curl_command = file.read()
    url_start = curl_command.find('"') + 1
    url_end = curl_command.find('"', url_start)
    url = curl_command[url_start:url_end]
    return url

def parse_query_params(url):
    params = url.split('?')[1]
    param_list = params.split('&')
    parsed_params = {}
    for param in param_list:
        key, value = param.split('=')
        parsed_params[key] = value
    return parsed_params

def create_get_lenght(parsed_params):
    edited_params = []
    for key, value in parsed_params.items():
        edited_value = value + 'a'*100
        edited_params.append(f"{key}={edited_value}")
    return "&".join(edited_params)

def create_test_empty(parsed_params):
    edited_params = []
    for key, value in parsed_params.items():
        value = ''
        edited_params.append(f"{key}={value}")
    return "&".join(edited_params)

def create_test_null(parsed_params):
    edited_params = []
    for key, value in parsed_params.items():
        value = None
        edited_params.append(f"{key}={value}")
    return "&".join(edited_params)

def create_test_invalid(parsed_params):
    edited_params = []
    for key, value in parsed_params.items():
        value = '!@#$%'
        edited_params.append(f"{key}={value}")
    return "&".join(edited_params)

def create_test_nonexistent(parsed_params):
    edited_params = []
    return "&".join(edited_params)

def create_request(api_key, collection_id, folder_id, request_name, request_method, request_headers, request_body, request_url, test_script):
    
    url = f'https://api.getpostman.com/collections/{collection_id}/requests?folder={folder_id}'

    headers = {
        'Content-Type': 'application/json',
        'X-API-Key': api_key
    }
    if request_body is None:
                data = {
            "name": request_name,
            "url": request_url,
            "method": request_method,
            "headers": request_headers,
            "dataMode": "none",
            "events": [
                {
                    "listen": "test",
                    "script": {
                        "id": "a8608e1a-ce4b-4129-8c89-930d26ae0f6a",
                        "exec": [test_script],
                        "type": "text/javascript"
                    }
                }
            ]
        }
    else:
        data = {
            "name": request_name,
            "url": request_url,
            "method": request_method,
            "headers": request_headers,
            "dataMode": "raw",
            "rawModeData": json.dumps(request_body, indent=2),
            "dataOptions": {
                "raw": {
                    "language": "json"
                }
            },
            "events": [
                {
                    "listen": "test",
                    "script": {
                        "id": "a8608e1a-ce4b-4129-8c89-930d26ae0f6a",
                        "exec": [test_script],
                        "type": "text/javascript"
                    }
                }
            ]
        }
    
    response = requests.post(url, headers=headers, json=data)
    print(response)
    return response

def edit_and_send_requests(api_key, collection_id, folder_id, file_path, request_method, request_headers, test_script):
    original_url = read_curl_file(file_path)
    parsed_params = parse_query_params(original_url)
    base_url = original_url.split('?')[0]

    edit_functions = {
        "length_test": create_get_lenght,
        "empty_test": create_test_empty,
        "null_test": create_test_null,
        "invalid_test": create_test_invalid,
        "nonexistent_test": create_test_nonexistent,
    }

    for test_name, edit_func in edit_functions.items():
        edited_query_string = edit_func(parsed_params)
        edited_url = f"{base_url}?{edited_query_string}"
        request_name = f"Edited GET Request - {test_name}"
        create_request(api_key, collection_id, folder_id, request_name, request_method, request_headers, None, edited_url, test_script)