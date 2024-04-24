import requests
import json

def read_curl_file(file_path):
    with open(file_path, 'r') as file:
        curl_command = file.read()
    url_start = curl_command.find('"') + 1
    url_end = curl_command.find('"', url_start)
    url = curl_command[url_start:url_end]
    return url

def read_test_script(test_type):
    file_path = f'config/tests/body/{test_type}'
    with open(file_path, 'r') as file:
        return file.read()

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

def create_request(api_key, collection_id, folder_id, request_name, request_method, request_headers, request_body, request_url, test_script, test_type, key, value):
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
    response = requests.post(url, headers=headers, json=data)
    print(f'{key} was tested {test_type}')
    return response


def edit_and_send_requests(api_key, collection_id, folder_id, file_path, request_method, request_headers, test_script):
    original_url = read_curl_file(file_path)
    base_url = original_url.split('?')[0]
    parsed_params = parse_query_params(original_url)

    if not parsed_params:
        print("No test scenarios can be created due to the lack of parameters.")
        request_name = "Request sem parâmetros"
        request_url = base_url
        test_type = "No Parameters"
        test_script = read_test_script('empty')  # Assume 'empty' script for the scenario without parameters
        create_request(api_key, collection_id, folder_id, request_name, request_method, request_headers, None, request_url, test_script, test_type, "None", "None")
        return
    
    previous_key = None

    original_value = parsed_params[key]

    for key in parsed_params.keys():
        if previous_key is not None and key != previous_key:
            print("-------------------------------")
            print("")
        previous_key = key

        original_value = parsed_params[key]
        
        # Empty test
        test_value = ''
        parsed_params[key] = test_value
        edited_query_string = "&".join(f"{k}={v}" for k, v in parsed_params.items())
        edited_url = f"{base_url}?{edited_query_string}"
        request_name = f"Edited GET Request - {key} Empty"
        create_request(api_key, collection_id, folder_id, request_name, request_method, request_headers, None, edited_url, test_script, "Empty", key, test_value)
        parsed_params[key] = original_value
        
        # Null test
        test_value = 'null'
        parsed_params[key] = test_value
        edited_query_string = "&".join(f"{k}={v}" for k, v in parsed_params.items())
        edited_url = f"{base_url}?{edited_query_string}"
        request_name = f"Edited GET Request - {key} Null"
        create_request(api_key, collection_id, folder_id, request_name, request_method, request_headers, None, edited_url, test_script, "Null", key, test_value)
        parsed_params[key] = original_value
        
        # Invalid test
        test_value = 'teste' if original_value.isdigit() else '1'
        parsed_params[key] = test_value
        edited_query_string = "&".join(f"{k}={v}" for k, v in parsed_params.items())
        edited_url = f"{base_url}?{edited_query_string}"
        request_name = f"Edited GET Request - {key} Invalid"
        create_request(api_key, collection_id, folder_id, request_name, request_method, request_headers, None, edited_url, test_script, "Invalid", key, test_value)
        parsed_params[key] = original_value
        
        # Nonexistent test
        temp_params = parsed_params.copy()
        temp_params.pop(key)
        edited_query_string = "&".join(f"{k}={v}" for k, v in temp_params.items())
        edited_url = f"{base_url}?{edited_query_string}"
        request_name = f"Edited GET Request - {key} Nonexistent"
        create_request(api_key, collection_id, folder_id, request_name, request_method, request_headers, None, edited_url, test_script, "Nonexistent", key, "N/A")
        
        # Length test
        test_value = original_value + 'a' * 100
        parsed_params[key] = test_value
        edited_query_string = "&".join(f"{k}={v}" for k, v in parsed_params.items())
        edited_url = f"{base_url}?{edited_query_string}"
        request_name = f"Edited GET Request - {key} Length"
        create_request(api_key, collection_id, folder_id, request_name, request_method, request_headers, None, edited_url, test_script, "Length", key, test_value)
        parsed_params[key] = original_value
