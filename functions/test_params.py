import requests
import json

ct_counter = 1

def read_curl_file(file_path):
    with open(file_path, 'r') as file:
        curl_command = file.read()
    url_start = curl_command.find('"') + 1
    url_end = curl_command.find('"', url_start)
    url = curl_command[url_start:url_end]
    return url

def read_test_script(test_type):
    file_path = f'config/tests/params/{test_type}'
    try:
        with open(file_path, 'r') as file:
            script_content = file.read()
            return script_content
    except FileNotFoundError:
        return "console.log('Error: Test script not found.')"

def parse_query_params(url):
    if '?' in url:
        params = url.split('?')[1]
        param_list = params.split('&')
        parsed_params = {}
        for param in param_list:
            key, value = param.split('=')
            parsed_params[key] = value
        return parsed_params
    else:
        return {}

def create_request(api_key, collection_id, folder_id, request_name, request_method, request_headers, request_url, test_script):
    url = f'https://api.getpostman.com/collections/{collection_id}/requests?folder={folder_id}'
    headers = {
        'Content-Type': 'application/json',
        'X-API-Key': api_key
    }
    data = {
        "name": request_name,
        "url": request_url,
        "method": request_method,
        "headers": request_headers,
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
    return response



def edit_and_send_requests(api_key, collection_id, folder_id, user_request_names, file_path, request_method):
    original_url = read_curl_file(file_path)
    base_url = original_url.split('?')[0]
    parsed_params = parse_query_params(original_url)

    if not parsed_params:
        print("No test scenarios can be created due to the lack of parameters.")
        request_name = "Request without params"
        request_url = base_url
        test_type = "No Parameters"
        test_script = read_test_script('empty')
        create_request(api_key, collection_id, folder_id, request_name, request_method, request_headers, request_url, test_script)
        return
    
    for key, original_value in parsed_params.items():
        global ct_counter
        for test_type in ['empty', 'null', 'invalid', 'nonexistent', 'length']:
            ct_counter += 1
            test_script = read_test_script(test_type)
            if test_type == 'nonexistent':
                temp_params = parsed_params.copy()
                temp_params.pop(key)
                edited_query_string = "&".join(f"{k}={v}" for k, v in temp_params.items())
                edited_url = f"{base_url}?{edited_query_string}"
                test_value = "N/A"
            else:
                test_value = {'empty': '', 'null': 'null', 'invalid': 'teste' if original_value.isdigit() else '1', 'length': original_value + 'a' * 100}[test_type]
                parsed_params[key] = test_value
                edited_query_string = "&".join(f"{k}={v}" for k, v in parsed_params.items())
                edited_url = f"{base_url}?{edited_query_string}"

            request_name = f"CT{str(ct_counter).zfill(3)} {str(key)} {test_type} {user_request_names[0]}"
            create_request(api_key, collection_id, folder_id, request_name, request_method, request_headers, edited_url, test_script)
            print(f'{key} was tested {test_type}')
            parsed_params[key] = original_value
