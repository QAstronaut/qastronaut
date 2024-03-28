from functions.create_postman import create_collection, create_folder, create_test_empty, create_test_null, create_test_nonexistent, create_test_invalid, create_test_lenght
from functions.fetch_data_postman import extract_curl_data
from functions.welcome import welcome, names, get_user_request_names,lost_api_key
import os
import argparse
import pyfiglet

text = "QAstronaut"
banner = pyfiglet.figlet_format(text)
print(banner)

parser = argparse.ArgumentParser(description='QAstronaut, Your Solution for Agile API Testing!')
parser.add_argument('--init', action='store_true', help='Perform initial setup')
args = parser.parse_args()

if args.init:
    api_key = welcome()
    print("\nPlease put the curl command in a text file named 'config/requests/curl.txt'.")
    exit()
else:
    api_key = lost_api_key()

# Aviso para colocar o comando curl em um arquivo txt
print("\nPlease put the curl command in a text file named 'config/requests/curl.txt' and then press 'Enter'.")
    
# Opção de S/n para confirmar se o usuário colocou o comando no arquivo
user_input = input("\nDid you place the curl command in 'curl.txt'? (Y/n): ")

# Lê o conteúdo do arquivo curl.txt    
with open('config/requests/curl.txt', 'r') as file:
        validate_curl = file.read()

if validate_curl == "Paste your cURL here":
    print("\nPut a valid curl command in 'config/requests/curl.txt' and try again.")
    exit() 

    # Verifica a resposta do usuário
if user_input.strip().lower() not in ["y", ""]:
    print("\nPlease put the curl command in 'config/requests/curl.txt' and try again.")
    exit()
    

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


request_method, request_url, request_body, request_headers = extract_curl_data(curl_command)

collection_name, folder_name = names()

collection_id = create_collection(api_key, collection_name)

folder_id = create_folder(collection_id, folder_name, api_key)

print(f"\nRequest Method: {request_method}")
print(f"Request URL: {request_url}")
print(f"Request Body: {request_body}")
print(f"Request Headers: {request_headers}")

print('\n----------------------------------------------------------------------------------------------------------------------------\n')

user_request_names = get_user_request_names()

if request_body is None:

    # teste de get

    # realizei esse import por não ter um create_test_empty_get por enquanto
    from functions.create_postman import create_request

    # essa variável foi coloca dentro de cada create_test, como a função não foi criada ainda ela fica por aqui
    with open('config/tests/params/null', 'r') as file:
        test_script = file.read()

    new_request_test = create_request(api_key, collection_id, folder_id, user_request_names, request_method, request_headers, request_body, request_url, test_script)
    print("Create request GET sucess")

    # fim teste de get

else:

    new_request_empty = create_test_empty(api_key, collection_id, folder_id, user_request_names, request_method, request_headers, request_body, request_url)
    print('----------------------------------------------------------------------------------------------------------------------------')
    new_request_null = create_test_null(api_key, collection_id, folder_id, user_request_names, request_method, request_headers, request_body, request_url)
    print('----------------------------------------------------------------------------------------------------------------------------')
    new_request_noneexistent = create_test_nonexistent(api_key, collection_id, folder_id, user_request_names, request_method, request_headers, request_body, request_url)
    print('----------------------------------------------------------------------------------------------------------------------------')
    new_request_invalid = create_test_invalid(api_key, collection_id, folder_id, user_request_names, request_method, request_headers, request_body, request_url)
    print('----------------------------------------------------------------------------------------------------------------------------')
    new_request_lenght = create_test_lenght(api_key, collection_id, folder_id, user_request_names, request_method, request_headers, request_body, request_url)
    print('---------------------------------------------------End----------------------------------------------------------------------')