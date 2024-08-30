from functions.create_postman import create_request
import json
import copy
from decimal import Decimal

ct_counter = 1

# Main function to handle different types of test cases.
def create_test(api_key, collection_id, folder_id, user_request_names, request_method, request_headers, request_body, request_url, test_type):

    test_script_path = f'config/tests/body/{test_type}'
    with open(test_script_path, 'r') as file:
        test_script = file.read()

    global ct_counter  # Ensure ct_counter is treated as a global variable

    # Function to handle the creation of a single request for testing.
    def handle_request(request_body, key, subkey=None, subvalue=None):
        global ct_counter  # Reference the global ct_counter
        if subkey is None:
            request_name = f"CT{str(ct_counter).zfill(3)} {str(key)} {test_type.capitalize()} {user_request_names[0]}"
        else:
            request_name = f"CT{str(ct_counter).zfill(3)} {key}/{str(subkey)} {test_type.capitalize()} {user_request_names[0]}"

        ct_counter += 1
        response = create_request(api_key, collection_id, folder_id, request_name, request_method, request_headers, request_body, request_url, test_script)

        if response.status_code == 200:
            request_data = response.json()
            request_id = request_data.get('data', {}).get('id')
            if request_id:
                return request_id
        else:
            print(f"Failed to create request '{user_request_names}'. Status code: {response.status_code}")
        return None

    # Function to modify and test a key in the request_body based on the test type.
    def test_key(request_body, key, value):
        original_value = copy.deepcopy(value)

        if test_type == 'empty':
            request_body[key] = '' if not isinstance(value, list) else []
        elif test_type == 'null':
            request_body[key] = None
        elif test_type == 'nonexistent':
            del request_body[key]
        elif test_type == 'invalid':
            types_values = {str: 1, int: 'Teste', float: 'Teste', dict: 1, list: 1.2}
            request_body[key] = types_values.get(type(value), value)
        elif test_type == 'lenght':
            if isinstance(value, str):
                last_char = value[-1] if value else 'a'  # get last character or default to 'a'
                request_body[key] = value + (last_char * 99)
            elif isinstance(value, int):
                last_digit = str(value)[-1]  # get last digit
                request_body[key] = int(str(value) + (last_digit * 99))
            elif isinstance(value, float):
                value_str = str(value)
                last_digit = value_str.split('.')[1][-1]  # get last digit after the decimal point
                request_body[key] = Decimal(value_str + (last_digit * 99))

        request_id = handle_request(request_body, key)
        request_body[key] = original_value
        print(f'{key} was tested {test_type.capitalize()}')
        return request_id

    # Create a list of keys to avoid changing the dictionary while iterating
    keys = list(request_body.keys())
    for key in keys:
        value = request_body[key]
        if isinstance(value, dict):
            subkeys = list(value.keys())
            for subkey in subkeys:
                test_key(request_body[key], subkey, value[subkey])
        else:
            test_key(request_body, key, value)

    return None

# Function to create a test case where the key's value is empty.
def create_test_empty(api_key, collection_id, folder_id, user_request_names, request_method, request_headers, request_body, request_url):
    return create_test(api_key, collection_id, folder_id, user_request_names, request_method, request_headers, request_body, request_url, 'empty')

# Function to create a test case where the key's value is null.
def create_test_null(api_key, collection_id, folder_id, user_request_names, request_method, request_headers, request_body, request_url):
    return create_test(api_key, collection_id, folder_id, user_request_names, request_method, request_headers, request_body, request_url, 'null')

# Function to create a test case where the key does not exist in the request body.
def create_test_nonexistent(api_key, collection_id, folder_id, user_request_names, request_method, request_headers, request_body, request_url):
    return create_test(api_key, collection_id, folder_id, user_request_names, request_method, request_headers, request_body, request_url, 'nonexistent')

# Function to create a test case where the key's value is invalid (wrong data type).
def create_test_invalid(api_key, collection_id, folder_id, user_request_names, request_method, request_headers, request_body, request_url):
    return create_test(api_key, collection_id, folder_id, user_request_names, request_method, request_headers, request_body, request_url, 'invalid')

# Function to create a test case where the key's value is overly long.
def create_test_lenght(api_key, collection_id, folder_id, user_request_names, request_method, request_headers, request_body, request_url):
    return create_test(api_key, collection_id, folder_id, user_request_names, request_method, request_headers, request_body, request_url, 'lenght')
