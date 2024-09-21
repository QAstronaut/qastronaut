from functions.create_postman import create_request
import json
import copy
import simplejson as json
from decimal import Decimal

ct_counter = 1

def create_test_empty(api_key, collection_id, folder_id, user_request_names, request_method, request_headers, request_body, request_url):

    with open('config/tests/body/empty', 'r') as file:
        test_script = file.read()

    global ct_counter
    for key, value in request_body.items():
        if type(value) != dict:
            request_name = f"CT{str(ct_counter).zfill(3)} {str(key)} Empty {user_request_names[0]}"
            ct_counter += 1
            request_body[key] = '' if type(value) != list else []
            response = create_request(api_key, collection_id, folder_id, request_name, request_method, request_headers, request_body, request_url, test_script)
            request_body[key] = value
            print(f'{key} was tested Empty')
        else:
            if type(value) == dict:
                request_name = f"CT{str(ct_counter).zfill(3)} {str(key)} Empty {user_request_names[0]}"
                ct_counter += 1
                request_body[key] = {}
                response = create_request(api_key, collection_id, folder_id, request_name, request_method, request_headers, request_body, request_url, test_script)
                request_body[key] = value
                print(f'{key} was tested Empty')
                for dict_key, dict_value in value.items():
                    request_name = f"CT{str(ct_counter).zfill(3)} {key}/{str(dict_key)} Empty {user_request_names[0]}"
                    ct_counter += 1
                    request_body[key][dict_key] = ""
                    response = create_request(api_key, collection_id, folder_id, request_name, request_method, request_headers, request_body, request_url, test_script)
                    request_body[key][dict_key] = dict_value
                    print(f'{key} was tested Empty')

    if response.status_code == 200:
        request_data = response.json()
        request_id = request_data.get('data', {}).get('id')
        if request_id:
            return request_id
    else:
        print(f"Failed to create request '{user_request_names}'. Status code: {response.status_code}")

    return None

def create_test_null(api_key, collection_id, folder_id, user_request_names, request_method, request_headers, request_body, request_url):

    with open('config/tests/body/null', 'r') as file:
        test_script = file.read()

    global ct_counter
    for key, value in request_body.items():
        if type(value) != dict:
            request_name = f"CT{str(ct_counter).zfill(3)} {str(key)} Null {user_request_names[0]}"
            ct_counter += 1
            request_body[key] = None if type(value) != list else None
            response = create_request(api_key, collection_id, folder_id, request_name, request_method, request_headers, request_body, request_url, test_script)
            request_body[key] = value
            print(f'{key} was tested Null')
        else: 
            request_name = f"CT{str(ct_counter).zfill(3)} {str(key)} Null {user_request_names[0]}"
            ct_counter += 1
            request_body[key] = None
            response = create_request(api_key, collection_id, folder_id, request_name, request_method, request_headers, request_body, request_url, test_script)
            request_body[key] = value
            print(f'{key} was tested Null')
            for dict_key, dict_value in value.items():
                request_name = f"CT{str(ct_counter).zfill(3)} {key}/{str(dict_key)} Null {user_request_names[0]}"
                ct_counter += 1
                request_body[key][dict_key] = None
                response = create_request(api_key, collection_id, folder_id, request_name, request_method, request_headers, request_body, request_url, test_script)
                request_body[key][dict_key] = dict_value
                print(f'{key} was tested Null')

    if response.status_code == 200:
        request_data = response.json()
        request_id = request_data.get('data', {}).get('id')
        if request_id:
            return request_id
    else:
        print(f"Failed to create request '{user_request_names}'. Status code: {response.status_code}")

    return None

def create_test_nonexistent(api_key, collection_id, folder_id, user_request_names, request_method, request_headers, request_body, request_url):

    with open('config/tests/body/nonexistent', 'r') as file:
        test_script = file.read()

    global ct_counter
    FIX_BODY = copy.deepcopy(request_body)
    for key, value in request_body.items():
        if type(value) != dict:
            request_name = f"CT{str(ct_counter).zfill(3)} {str(key)} Nonexistent {user_request_names[0]}"
            ct_counter += 1
            del FIX_BODY[key]
            response = create_request(api_key, collection_id, folder_id, request_name, request_method, request_headers, FIX_BODY, request_url, test_script)
            FIX_BODY = copy.deepcopy(request_body)
            print(f'{key} was tested Nonexistent')
        else:
            if type(value) == dict:
                request_name = f"CT{str(ct_counter).zfill(3)} {str(key)} Nonexistent {user_request_names[0]}"
                ct_counter += 1
                del FIX_BODY[key]
                response = create_request(api_key, collection_id, folder_id, request_name, request_method, request_headers, FIX_BODY, request_url, test_script)
                FIX_BODY = copy.deepcopy(request_body)
                print(f'{key} was tested Nonexistent')
                for dict_key, dict_value in value.items():
                    request_name = f"CT{str(ct_counter).zfill(3)} {key}/{str(dict_key)} Nonexistent {user_request_names[0]}"
                    ct_counter += 1
                    del FIX_BODY[key][dict_key]
                    response = create_request(api_key, collection_id, folder_id, request_name, request_method, request_headers, FIX_BODY, request_url, test_script)
                    FIX_BODY = copy.deepcopy(request_body)
                    print(f'{key} was tested Nonexistent')

    if response.status_code == 200:
        request_data = response.json()
        request_id = request_data.get('data', {}).get('id')
        if request_id:
            return request_id
    else:
        print(f"Failed to create request '{user_request_names}'. Status code: {response.status_code}")

    return None

def create_test_invalid(api_key, collection_id, folder_id, user_request_names, request_method, request_headers, request_body, request_url):

    with open('config/tests/body/invalid', 'r') as file:
        test_script = file.read()
    
    global ct_counter
    types_values = {str: 1, int: 'Teste', float: 'Teste', dict: 1, list: 1.2}
    for key, value in request_body.items():
        if type(value) != dict and type(value) != list:
            request_name = f"CT{str(ct_counter).zfill(3)} {str(key)} Invalid {user_request_names[0]}"
            ct_counter += 1
            request_body[key] = types_values[type(value)]
            response = create_request(api_key, collection_id, folder_id, request_name, request_method, request_headers, request_body, request_url, test_script)
            request_body[key] = value
            print(f'{key} was tested Invalid')
        else:
            if type(value) != list:
                for dict_key, dict_value in value.items():
                    request_name = f"CT{str(ct_counter).zfill(3)} {key}/{str(dict_key)} Invalid {user_request_names[0]}"
                    ct_counter += 1
                    request_body[key][dict_key] = types_values[type(value)]
                    response = create_request(api_key, collection_id, folder_id, request_name, request_method, request_headers, request_body, request_url, test_script)
                    request_body[key][dict_key] = dict_value
                    print(f'{key} was tested Invalid')

    if response.status_code == 200:
        request_data = response.json()
        request_id = request_data.get('data', {}).get('id')
        if request_id:
            return request_id
    else:
        print(f"Failed to create request '{user_request_names}'. Status code: {response.status_code}")

    return None


def create_test_lenght(api_key, collection_id, folder_id, user_request_names, request_method, request_headers, request_body, request_url):

    with open('config/tests/body/lenght', 'r') as file:
        test_script = file.read()
    
    global ct_counter
    for key, value in request_body.items():
        if type(value) != dict and type(value) != list:
            request_name = f"CT{str(ct_counter).zfill(3)} {str(key)} Lenght {user_request_names[0]}" 
            ct_counter += 1
            if type(value) == str:
                request_body[key] = (str(value).rstrip() + ' ') * 100
            elif type(value) == int:
                request_body[key] = int(str(value) * 100)
            elif type(value) == float:
                request_body[key] = Decimal((str(value).split('.')[0] * 100) + '.' + str(value).split('.')[1])
            response = create_request(api_key, collection_id, folder_id, request_name, request_method, request_headers, request_body, request_url, test_script)
            request_body[key] = value
            print(f'{key} was tested lenght')
        elif type(value) == dict:
            for dict_key, dict_value in value.items():
                if type(dict_value) == str:
                    request_name = f"CT{str(ct_counter).zfill(3)} {key}/{str(dict_key)} Lenght {user_request_names[0]}" 
                    ct_counter += 1
                    request_body[key][dict_key] = (str(dict_value).rstrip() + ' ') * 100
                elif type(dict_value) == int:
                    request_body[key][dict_key] = int(str(dict_value) * 100)
                elif type(dict_value) == float:
                    request_body[key][dict_key] = Decimal((str(dict_value).split('.')[0] * 100) + '.' + str(dict_value).split('.')[1])
                response = create_request(api_key, collection_id, folder_id, request_name, request_method, request_headers, request_body, request_url, test_script)
                request_body[key][dict_key] = dict_value
                print(f'{key} was tested lenght')
        elif type(value) == list:
            if value:  # Verifica se a lista não está vazia
                request_name = f"CT{str(ct_counter).zfill(3)} {key} Lenght {user_request_names[0]}"
                ct_counter += 1
                request_body[key] = value + [value[-1]] * (100 - len(value))  # Repete o último elemento até atingir o comprimento desejado
                response = create_request(api_key, collection_id, folder_id, request_name, request_method, request_headers, request_body, request_url, test_script)
                request_body[key] = value  # Restaura o valor original
                print(f'{key} was tested lenght')

    if response.status_code == 200:
        request_data = response.json()
        request_id = request_data.get('data', {}).get('id')
        if request_id:
            return request_id
    else:
        print(f"Failed to create request '{user_request_names}'. Status code: {response.status_code}")

    return None