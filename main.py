from functions.create_postman import create_collection, create_folder, create_request
from functions.fetch_data_postman import fetch_request_data, extract_curl_data
from functions.welcome import welcome

api_key, collection_name, folder_name = welcome()

new_collection = create_collection(api_key, collection_name)
#print("\nNew Collection created!")
collection_id = new_collection['collection']['id']

new_folder = create_folder(api_key, collection_id, folder_name, collection_name)
#print("New Folder created!\n")
folder_id = new_folder['collection']['id']

print("----------------------------------------------------------------------\n")

# Aviso para colocar o comando curl em um arquivo txt
print("Please put the curl command in a text file named 'curl.txt' and then press 'Enter'.")
    
    # Opção de S/n para confirmar se o usuário colocou o comando no arquivo
user_input = input("\nDid you place the curl command in 'curl.txt'? (S/n): ")
    
    # Verifica a resposta do usuário
if user_input.strip().lower() not in ["s", ""]:
    print("\nPlease put the curl command in 'curl.txt' and try again.")
    exit()
    
    # Lê o conteúdo do arquivo curl.txt
try:
    with open("curl.txt", "r") as file:
        curl_command = file.read()
except FileNotFoundError:
    print("\nThe 'curl.txt' file was not found. Please create the file and place the curl command in it.")
    exit()

request_method, request_url, request_body, request_headers = extract_curl_data(curl_command)

print(f"\nRequest Method: {request_method}")
print(f"Request URL: {request_url}")
print(f"Request Body: {request_body}")
print(f"Request Headers: {request_headers}")

request_name = 'Teste'
test_script = "console.log()"

print("\n----------------------------------------------------------------------\n")

new_request = create_request(api_key, collection_name, collection_id, folder_name, folder_id, request_name, request_method, request_body, request_url, request_headers, test_script)
#print("\nNew Request created!\n")