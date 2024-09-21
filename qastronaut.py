from functions.create_postman import create_collection, create_folder
from functions.test_body import create_test_empty, create_test_null, create_test_nonexistent, create_test_invalid, create_test_lenght
from functions.test_params import edit_and_send_requests
from functions.fetch_data_postman import extract_curl_data
from functions.welcome import welcome, names, get_user_request_names
from functions.api_key_manager import lost_api_key, load_api_key
import os
import argparse

parser = argparse.ArgumentParser(description='QAstronaut, Your Solution for Agile API Testing!')
parser.add_argument('--init', action='store_true', help='Perform initial setup')
args = parser.parse_args()

if args.init:
    
    message_initial = welcome()
    api_key = load_api_key()
    print(f"\nPlease put the curl command in a text file named 'config/requests/curl.txt'.")
    
    exit()
    

else:
    api_key = lost_api_key()

print(f"\nPlease put the curl command in a text file named 'config/requests/curl.txt' and then press 'Enter'.")
    
user_input = input(f"\nDid you place the curl command in 'curl.txt'? (Y/n): ")
   
with open('config/requests/curl.txt', 'r') as file:
    validate_curl = file.read()

if validate_curl == "Paste your cURL here":

    print(f"\nPut a valid curl command in 'config/requests/curl.txt' and try again.")
    exit() 


if user_input.strip().lower() not in ["y", ""]:
    print(f"\nPlease put the curl command in 'config/requests/curl.txt' and try again.")
    exit()

curl_file_path = os.path.join('config/requests', 'curl.txt')
requests_name_arch = 'config/requests'
name_file_path = os.path.join(requests_name_arch, 'user_requests')

try:
    with open(curl_file_path, "r") as file:
        curl_command = file.read()
except FileNotFoundError:
    print(f"\nThe 'curl.txt' file was not found in the 'config/requests' directory. Please create the file and place the curl command in it.")
    exit()

request_method, request_url, request_body, request_headers = extract_curl_data(curl_command)

collection_name, folder_name = names()

print(f"\nRequest Method: {request_method}")
print(f"Request URL: {request_url}")
print(f"Request Body: {request_body}")
print(f"Request Headers: {request_headers}")

runner = input("\nCan I run? (Y/n): ")

if runner.strip().lower() not in ["y", ""]:
    exit()

collection_id = create_collection(api_key, collection_name)

folder_id = create_folder(collection_id, folder_name, api_key)

print('\n-------------------------------\n')
user_request_names = get_user_request_names()

if request_body is None:
    edit_and_send_requests(api_key, collection_id, folder_id, curl_file_path, request_method, request_headers, request_url)
    print('-------------------------------')
    print("\nEnd")
else:
    new_request_empty = create_test_empty(api_key, collection_id, folder_id, user_request_names, request_method, request_headers, request_body, request_url)
    print('-------------------------------')
    new_request_null = create_test_null(api_key, collection_id, folder_id, user_request_names, request_method, request_headers, request_body, request_url)
    print('-------------------------------')
    new_request_nonexistent = create_test_nonexistent(api_key, collection_id, folder_id, user_request_names, request_method, request_headers, request_body, request_url)
    print('-------------------------------')
    new_request_invalid = create_test_invalid(api_key, collection_id, folder_id, user_request_names, request_method, request_headers, request_body, request_url)
    print('-------------------------------')
    new_request_length = create_test_lenght(api_key, collection_id, folder_id, user_request_names, request_method, request_headers, request_body, request_url)
    print('-------------------------------')
    print("\nEnd")
