import requests
import json
import copy
import simplejson as json
from decimal import Decimal

ct_counter = 1

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
    global ct_counter
    for key, value in request_body.items():
        if type(value) != dict:
            request_name = f"CT{str(ct_counter).zfill(3)} {user_request_names[0]} {str(key)} Vazio"
            ct_counter += 1
            request_body[key] = '' if type(value) != list else []
            response = create_request(api_key, collection_id, folder_id, request_name, request_method, request_headers, request_body, request_url, test_script)
            request_body[key] = value
            print(f'{key} foi testada sem Valor')
        else:
            if type(value) == dict:
                request_name = f"CT{str(ct_counter).zfill(3)} {user_request_names[0]} {str(key)} Vazio"
                ct_counter += 1
                request_body[key] = {}
                response = create_request(api_key, collection_id, folder_id, request_name, request_method, request_headers, request_body, request_url, test_script)
                request_body[key] = value
                print(f'{key} foi testada sem Valor')
                for dict_key, dict_value in value.items():
                    request_name = f"CT{str(ct_counter).zfill(3)} {user_request_names[0]} {str(key)} Vazio"
                    ct_counter += 1
                    request_body[key][dict_key] = ""
                    response = create_request(api_key, collection_id, folder_id, request_name, request_method, request_headers, request_body, request_url, test_script)
                    request_body[key][dict_key] = dict_value
                    print(f'{key} foi testada sem Valor')


    if response.status_code == 200:
        request_data = response.json()
        request_id = request_data.get('data', {}).get('id')
        if request_id:
            # print(f"Request '{user_request_names}' created successfully with request_id: {request_id}")
            pass
            return request_id
        else:
            pass
            # print(f"Request '{user_request_names}' created, but request_id not found in the response.")
    else:
        print(f"Failed to create request '{user_request_names}'. Status code: {response.status_code}")

    return None

def create_test_null(api_key, collection_id, folder_id, user_request_names, request_method, request_headers, request_body, request_url, test_script):
    # Esta função tem como objetivo testar a primeira key do request_body vazia.
    global ct_counter
    for key, value in request_body.items():
        if type(value) != dict:
            request_name = f"CT{str(ct_counter).zfill(3)} {user_request_names[0]} {str(key)} Nulo"
            ct_counter += 1
            request_body[key] = None if type(value) != list else None
            response = create_request(api_key, collection_id, folder_id, request_name, request_method, request_headers, request_body, request_url, test_script)
            request_body[key] = value
            print(f'{key} foi testada Nulo')
        else:
            request_name = f"CT{str(ct_counter).zfill(3)} {user_request_names[0]} {str(key)} Nulo"
            ct_counter += 1
            request_body[key] = None
            response = create_request(api_key, collection_id, folder_id, request_name, request_method, request_headers, request_body, request_url, test_script)
            request_body[key] = value
            print(f'{key} foi testada Nulo')
            for dict_key, dict_value in value.items():
                request_name = f"CT{str(ct_counter).zfill(3)} {user_request_names[0]} {key}/{str(dict_key)} Nulo"
                ct_counter += 1
                request_body[key][dict_key] = None
                response = create_request(api_key, collection_id, folder_id, request_name, request_method, request_headers, request_body, request_url, test_script)
                request_body[key][dict_key] = dict_value
                print(f'{key} foi testada Nulo')

    if response.status_code == 200:
        request_data = response.json()
        request_id = request_data.get('data', {}).get('id')
        if request_id:
            # print(f"Request '{user_request_names}' created successfully with request_id: {request_id}")
            pass
            return request_id
        else:
            pass
            # print(f"Request '{user_request_names}' created, but request_id not found in the response.")
    else:
        print(f"Failed to create request '{user_request_names}'. Status code: {response.status_code}")

    return None

def create_test_nonexistent(api_key, collection_id, folder_id, user_request_names, request_method, request_headers, request_body, request_url, test_script):
    # Esta função tem como objetivo testar a primeira key do request_body vazia.
    global ct_counter
    FIX_BODY = copy.deepcopy(request_body)
    for key, value in request_body.items():
        if type(value) != dict:
            request_name = f"CT{str(ct_counter).zfill(3)} {user_request_names[0]} {str(key)} Inexistente"
            ct_counter += 1
            del FIX_BODY[key]
            response = create_request(api_key, collection_id, folder_id, request_name, request_method, request_headers, FIX_BODY, request_url, test_script)
            FIX_BODY = copy.deepcopy(request_body)
            print(f'{key} foi testada Inexistente')
        else:
            if type(value) == dict:
                request_name = f"CT{str(ct_counter).zfill(3)} {user_request_names[0]} {str(key)} Inexistente"
                ct_counter += 1
                del FIX_BODY[key]
                response = create_request(api_key, collection_id, folder_id, request_name, request_method, request_headers, FIX_BODY, request_url, test_script)
                FIX_BODY = copy.deepcopy(request_body)
                print(f'{key} foi testada Inexistente')
                for dict_key, dict_value in value.items():
                    request_name = f"CT{str(ct_counter).zfill(3)} {user_request_names[0]} {key}/{str(dict_key)} Inexistente"
                    ct_counter += 1
                    del FIX_BODY[key][dict_key]
                    response = create_request(api_key, collection_id, folder_id, request_name, request_method, request_headers, FIX_BODY, request_url, test_script)
                    FIX_BODY = copy.deepcopy(request_body)
                    print(f'{key} foi testada Inexistente')

    if response.status_code == 200:
        request_data = response.json()
        request_id = request_data.get('data', {}).get('id')
        if request_id:
            # print(f"Request '{user_request_names}' created successfully with request_id: {request_id}")
            pass
            return request_id
        else:
            pass
            # print(f"Request '{user_request_names}' created, but request_id not found in the response.")
    else:
        print(f"Failed to create request '{user_request_names}'. Status code: {response.status_code}")

    return None

def create_test_invalid(api_key, collection_id, folder_id, user_request_names, request_method, request_headers, request_body, request_url, test_script):
    # Esta função tem como objetivo testar a primeira key do request_body vazia.
    global ct_counter
    types_values = {str: 1, int: 'Teste', float: 'Teste', dict: ['Teste'], list: 1.2}
    for key, value in request_body.items():
        if type(value) != dict and type(value) != list:
            request_name = f"CT{str(ct_counter).zfill(3)} {user_request_names[0]} {str(key)} Inválido"
            ct_counter += 1
            request_body[key] = types_values[type(value)]
            response = create_request(api_key, collection_id, folder_id, request_name, request_method, request_headers, request_body, request_url, test_script)
            request_body[key] = value
            print(f'{key} foi testada Inválido')
        else:
            if type(value) != list:
                for dict_key, dict_value in value.items():
                    request_name = f"CT{str(ct_counter).zfill(3)} {user_request_names[0]} {key}/{str(dict_key)} Inválido"
                    ct_counter += 1
                    request_body[key][dict_key] = types_values[type(value)]
                    response = create_request(api_key, collection_id, folder_id, request_name, request_method, request_headers, request_body, request_url, test_script)
                    request_body[key][dict_key] = dict_value
                    print(f'{key} foi testada Inválido')

    if response.status_code == 200:
        request_data = response.json()
        request_id = request_data.get('data', {}).get('id')
        if request_id:
            # print(f"Request '{user_request_names}' created successfully with request_id: {request_id}")
            pass
            return request_id
        else:
            pass
            # print(f"Request '{user_request_names}' created, but request_id not found in the response.")
    else:
        print(f"Failed to create request '{user_request_names}'. Status code: {response.status_code}")

    return None


def create_test_lenght(api_key, collection_id, folder_id, user_request_names, request_method, request_headers, request_body, request_url, test_script):
    # Esta função tem como objetivo testar a primeira key do request_body vazia.
    global ct_counter
    for key, value in request_body.items():
        if type(value) != dict and type(value) != list:
            request_name = f"CT{str(ct_counter).zfill(3)} {user_request_names[0]} {str(key)} Tamanho" 
            ct_counter += 1
            if type(value) == str:
                request_body[key] = (str(value).rstrip() + ' ') * 100
            else:
                if type(value) == int:
                    request_body[key] = str(value)* 100
                    request_body[key] = int(request_body[key])
                else:
                    request_body[key] = (str(value).split('.')[0]*100) + '.' + str(value).split('.')[1]
                    decimal_value = Decimal(request_body[key])
                    request_body[key] = decimal_value
            response = create_request(api_key, collection_id, folder_id, request_name, request_method, request_headers, request_body, request_url, test_script)
            request_body[key] = value
            print(f'{key} foi testada sem Tamanho')
        else:
            if type(value) == dict:
                for dict_key, dict_value in value.items():
                    if type(dict_value) != dict:
                        if type(dict_value) == str:
                            request_name = f"CT{str(ct_counter).zfill(3)} {user_request_names[0]} {str(key)} Tamanho" 
                            ct_counter += 1
                            request_body[key][dict_key] = (str(dict_value).rstrip() + ' ') * 100
                        else:
                            if type(value) == int:
                                request_body[key][dict_key] = str(dict_value)* 100
                                request_body[key][dict_key] = int(request_body[key][dict_key])
                            else:
                                request_body[key][dict_key] = (str(value).split('.')[0]*100) + '.' + str(value).split('.')[1]
                                decimal_value = Decimal(request_body[key][dict_key])
                                request_body[key][dict_key] = decimal_value
                        response = create_request(api_key, collection_id, folder_id, request_name, request_method, request_headers, request_body, request_url, test_script)
                        request_body[key][dict_key] = dict_value
                        print(f'{key} foi testada sem Tamanho')
            elif type(value) == list:
                pass
    if response.status_code == 200:
        request_data = response.json()
        request_id = request_data.get('data', {}).get('id')
        if request_id:
            # print(f"Request '{user_request_names}' created successfully with request_id: {request_id}")
            pass
            return request_id
        else:
            pass
            # print(f"Request '{user_request_names}' created, but request_id not found in the response.")
    else:
        print(f"Failed to create request '{user_request_names}'. Status code: {response.status_code}")

    return None