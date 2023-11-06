from functions.create_postman import create_collection, create_folder, create_test_empty, create_test_null, create_test_nonexistent, create_test_invalid, create_test_lenght
from functions.fetch_data_postman import extract_curl_data
from functions.welcome import welcome, names, get_user_request_names,lost_api_key
import os
import argparse
import time


print(30 * '-' + 'QAstronaut' + 30 * '-')

parser = argparse.ArgumentParser(description='QAstronaut, Your Solution for Agile API Testing!')
parser.add_argument('--init', action='store_true', help='Perform initial setup')
args = parser.parse_args()

if args.init:
    api_key = welcome()
else:
    api_key = lost_api_key()

# Aviso para colocar o comando curl em um arquivo txt
print("\n\nPlease put the curl command in a text file named 'curl.txt' and then press 'Enter'.")
    
    # Opção de S/n para confirmar se o usuário colocou o comando no arquivo
user_input = input("\nDid you place the curl command in 'curl.txt'? (Y/n): ")
    
    # Verifica a resposta do usuário
if user_input.strip().lower() not in ["y", ""]:
    print("\nPlease put the curl command in 'curl.txt' and try again.")
    exit()
    
    # Lê o conteúdo do arquivo curl.txt

# Define o caminho completo para o arquivo "curl.txt"
curl_file_path = os.path.join('config/requests', 'curl.txt')
requests_name_arch = 'config/requests'
name_file_path = os.path.join(requests_name_arch, 'user_requests')

try:
    with open(curl_file_path, "r") as file:
        curl_command = file.read()
except FileNotFoundError:
    print("\nThe 'curl.txt' file was not found in the 'config/requests' directory. Please create the file and place the curl command in it.")
    exit()

collection_name, folder_name = names()

collection_id = create_collection(api_key, collection_name)

folder_id = create_folder(collection_id, folder_name, api_key)

request_method, request_url, request_body, request_headers = extract_curl_data(curl_command)

print(f"\nRequest Method: {request_method}")
print(f"Request URL: {request_url}")
print(f"Request Body: {request_body}")
print(f"Request Headers: {request_headers}")

test_script = "console.log()"

print("\n----------------------------------------------------------------------\n")

user_request_names = get_user_request_names()
new_request_empty = create_test_empty(api_key, collection_id, folder_id, user_request_names, request_method, request_headers, request_body, request_url, test_script)
print('----------------------------------------------------------------------------------------------------------------------------')
new_request_null = create_test_null(api_key, collection_id, folder_id, user_request_names, request_method, request_headers, request_body, request_url, test_script)
print('----------------------------------------------------------------------------------------------------------------------------')
new_request_noneexistent = create_test_nonexistent(api_key, collection_id, folder_id, user_request_names, request_method, request_headers, request_body, request_url, test_script)
print('----------------------------------------------------------------------------------------------------------------------------')
new_request_invalid = create_test_invalid(api_key, collection_id, folder_id, user_request_names, request_method, request_headers, request_body, request_url, test_script)
print('----------------------------------------------------------------------------------------------------------------------------')
new_request_lenght = create_test_lenght(api_key, collection_id, folder_id, user_request_names, request_method, request_headers, request_body, request_url, test_script)
print('--------------------------------------------End--------------------------------------------------------')
