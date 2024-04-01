from functions.create_postman import create_collection, create_folder, create_test_empty, create_test_null, create_test_nonexistent, create_test_invalid
from functions.create_postman_GET import edit_and_create_get_requests  # Assegure-se de que o caminho está correto
from functions.fetch_data_postman import extract_curl_data
from functions.welcome import welcome, names, get_user_request_names, lost_api_key
import os
import argparse
import pyfiglet

green_color = "\033[1;32m"
blue_color = "\033[1;34m"
reset_color = "\033[0m"

text = "QAstronaut"
banner = pyfiglet.figlet_format(text)

print(f"{blue_color}{banner}{reset_color}")

parser = argparse.ArgumentParser(description='QAstronaut, Your Solution for Agile API Testing!')
parser.add_argument('--init', action='store_true', help='Perform initial setup')
args = parser.parse_args()

if args.init:
    api_key = welcome()
    print(f"\nPlease put the curl command in a text file named '{blue_color}config/requests/curl.txt{reset_color}'.")
    exit()
else:
    api_key = lost_api_key()

print(f"\nPlease put the curl command in a text file named '{blue_color}config/requests/curl.txt{reset_color}' and then press '{blue_color}Enter{reset_color}'.")

user_input = input(f"\nDid you place the curl command in '{blue_color}curl.txt{reset_color}'? (Y/n): ")

with open('config/requests/curl.txt', 'r') as file:
    validate_curl = file.read()

if validate_curl == "Paste your cURL here":
    print(f"\nPut a valid curl command in '{blue_color}config/requests/curl.txt{reset_color}' and try again.")
    exit()

if user_input.strip().lower() not in ["y", ""]:
    print(f"\nPlease put the curl command in '{blue_color}config/requests/curl.txt{reset_color}' and try again.")
    exit()

curl_file_path = os.path.join('config/requests', 'curl.txt')
requests_name_arch = 'config/requests'
name_file_path = os.path.join(requests_name_arch, 'user_requests')

try:
    with open(curl_file_path, "r") as file:
        curl_command = file.read()
except FileNotFoundError:
    print(f"\nThe '{blue_color}curl.txt{reset_color}' file was not found in the '{blue_color}config/requests{reset_color}' directory. Please create the file and place the curl command in it.")
    exit()

request_method, request_url, request_body, request_headers = extract_curl_data(curl_command)

collection_name, folder_name = names()

collection_id = create_collection(api_key, collection_name)

folder_id = create_folder(collection_id, folder_name, api_key)

print(f"\nRequest Method: {green_color}{request_method}{reset_color}")
print(f"Request URL: {green_color}{request_url}{reset_color}")
print(f"Request Body: {green_color}{request_body if request_body else 'None'}{reset_color}")
print(f"Request Headers: {green_color}{request_headers}{reset_color}")

runner = input("\nCan I run? (Y/n): ")

if runner.strip().lower() not in ["y", ""]:
    exit()

print('\n----------------------------------------------------------------------------------------------------------------------------\n')

user_request_names = get_user_request_names()

if request_method == "GET":
    edit_and_create_get_requests(api_key, collection_id, folder_id, curl_file_path, request_method, request_headers, "console.log('Test passed')")  # Exemplo de script de teste
    print("Create request GET success")
else:
    new_request_empty = create_test_empty(api_key, collection_id, folder_id, user_request_names, request_method, request_headers, request_body, request_url)
    print('----------------------------------------------------------------------------------------------------------------------------')
    new_request_null = create_test_null(api_key, collection_id, folder_id, user_request_names, request_method, request_headers, request_body, request_url)
    print('----------------------------------------------------------------------------------------------------------------------------')
    new_request_nonexistent = create_test_nonexistent(api_key, collection_id, folder_id, user_request_names, request_method, request_headers, request_body, request_url)
    print('----------------------------------------------------------------------------------------------------------------------------')
    new_request_invalid = create_test_invalid(api_key, collection_id, folder_id, user_request_names, request_method, request_headers, request_body, request_url)
    print('----------------------------------------------------------------------------------------------------------------------------')
    # new_request_length = create_test_length(api_key, collection_id, folder_id, user_request_names, request_method, request_headers, request_body, request)
