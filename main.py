from functions.create_postman import create_collection, create_folder, create_request
from functions.fetch_data_postman import extract_curl_data, format_headers
from functions.welcome import welcome, names
import os

api_key = welcome()

# Aviso para colocar o comando curl em um arquivo txt
print("\nPlease put the curl command in a text file named 'curl.txt' and then press 'Enter'.")
    
    # Opção de S/n para confirmar se o usuário colocou o comando no arquivo
user_input = input("\nDid you place the curl command in 'curl.txt'? (S/n): ")
    
    # Verifica a resposta do usuário
if user_input.strip().lower() not in ["s", ""]:
    print("\nPlease put the curl command in 'curl.txt' and try again.")
    exit()
    
    # Lê o conteúdo do arquivo curl.txt

# Define o diretório onde o arquivo "curl.txt" está localizado
requests_dir = 'config/requests'
requests_name_arch = 'config/requests'

# Define o caminho completo para o arquivo "curl.txt"
curl_file_path = os.path.join(requests_dir, 'curl.txt')
name_file_path = os.path.join(requests_name_arch, 'user_requests')

try:
    with open(curl_file_path, "r") as file:
        curl_command = file.read()
except FileNotFoundError:
    print("\nThe 'curl.txt' file was not found in the 'config/requests' directory. Please create the file and place the curl command in it.")
    exit()

def get_user_request_names():
    user_request_names = []
    user_requests_file = 'user_requests'
    
    try:
        with open(name_file_path, "r") as file:
            lines = file.readlines()
            for line in lines:
                parts = line.strip().split(',')
                if len(parts) >= 4:
                    user_request_name = '-'.join(parts) 
                    user_request_names.append(user_request_name)
    except FileNotFoundError:
        print("\nThe 'user_requests.txt' file was not found. Please create the file and add request names.")
        exit()
    
    return user_request_names

collection_name, folder_name = names()

new_collection = create_collection(api_key, collection_name)
collection_id = new_collection['collection']['id']

new_folder = create_folder(api_key, collection_id, folder_name, collection_name)
folder_id = new_folder['collection']['id']


request_method, request_url, request_body, headers_dict = extract_curl_data(curl_command)

print(f"\nRequest Method: {request_method}")
print(f"Request URL: {request_url}")
print(f"Request Body: {request_body}")
print(f"Request Headers: {headers_dict}")

test_script = "console.log()"

print("\n----------------------------------------------------------------------\n")

request_headers = format_headers(headers_dict)

user_request_names = get_user_request_names()

for user_request_name in user_request_names:
    new_request = create_request(api_key, collection_name, collection_id, folder_name, folder_id, request_method, request_headers, request_body, request_url, test_script, user_request_name)
    
    response_json = new_request  # Armazene a resposta em uma variável
    
    # Verifique o código de status da resposta
    if 'error' not in response_json:
        print(f"Request '{user_request_name}' created successfully!")
    else:
        print(f"Error creating request '{user_request_name}': {response_json['error']['message']}")
    
    # Resto do código permanece o mesmo

