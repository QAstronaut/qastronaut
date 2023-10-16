import requests
import json
import copy

def create_collection(api_key, collection_name):
    url = "https://api.getpostman.com/collections"

    headers = {
        "X-Api-Key": api_key,
        "Content-Type": "application/json"
    }

    data = {
        "collection": {
            "info": {
                "name": collection_name,
                "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
            },
            "item": []
        }
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        collection_data = response.json()
        collection_id = collection_data.get('collection', {}).get('uid')
        if collection_id:
            print(f"\nCollection '{collection_name}' created successfully with collection_id: {collection_id}")
            return collection_id
        else:
            print(f"\nCollection '{collection_name}' created, but collection_id not found in the response.")
    else:
        print(f"\nFailed to create collection '{collection_name}'. Status code: {response.status_code}")

    return None


def create_folder(collection_id, folder_name, api_key):

    url = f'https://api.getpostman.com/collections/{collection_id}/folders'
    
    headers = {
        'Content-Type': 'application/json',
        'X-API-Key': api_key
    }

    data = {
        'name': folder_name
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        folder_data = response.json()
        folder_id = folder_data.get('data', {}).get('id')
        if folder_id:
            print(f'\nFolder {folder_name} created successfully with folder_id: {folder_id}')
            return folder_id
        else:
            print(f'\nFolder {folder_name} created, but folder_id not found in the response.')
    else:
        print('\nError creating folder:')
        print(response.text)
    return None


def create_request(api_key, collection_id, folder_id, request_name, request_method, request_headers, request_body, request_url, test_script):
    
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

def create_test_empty(api_key, collection_id, folder_id, user_request_names, request_method, request_headers, request_body, request_url, test_script):
    # Esta função tem como objetivo testar a primeira key do request_body vazia.
    for key, value in request_body.items():
        if type(value) == str or type(value) == float or type(value) == int:
            user_request_names = user_request_names[0] + str(key)
            request_body[key] = ''
            response = create_request(api_key, collection_id, folder_id, user_request_names, request_method, request_headers, request_body, request_url, test_script)
            request_body[key] = value
            user_request_names = "Teste "
            print(f'{key} foi testada sem valor')
        else:
            user_request_names = user_request_names[0] + str(key)
            for dic_value in request_body[key]:
                dic_value = ''
            response = create_request(api_key, collection_id, folder_id, user_request_names, request_method, request_headers, request_body, request_url, test_script)
            request_body[key] = dic_value
            user_request_names = "Teste "
            print(f'{key} foi testado com dicionário vazio')
                
    if response.status_code == 200:
        request_data = response.json()
        request_id = request_data.get('data', {}).get('id')
        if request_id:
            print(f"Request '{user_request_names}' created successfully with request_id: {request_id}")
            return request_id
        else:
            print(f"Request '{user_request_names}' created, but request_id not found in the response.")
    else:
        print(f"Failed to create request '{user_request_names}'. Status code: {response.status_code}")

    return None
