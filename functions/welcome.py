import os
import json

def welcome():

    message_initial = (
        """\nWelcome to your test suite automator!\n\n
        Before we dive into the hard work, I'll need some information.\n
        *** No information provided will be stored outside your machine ***\n"""
    )

    # Define o diretório de configuração
    config_dir = 'config'
    requests_dir = 'config/requests'
    user_curl_path = 'config/requests/curl.txt'
    test_dir = 'config/tests'
    request_name_dir ='config/request_names'
    user_request_path = 'config/request_name/user_requests.txt'
    test_body_dir = 'config/tests/body'
    

    # Define o diretório de solicitações dentro do diretório de configuração
    requests_dir = os.path.join(config_dir, 'requests')
    test_dir = os.path.join(config_dir, 'tests')
    request_name_dir = os.path.join(config_dir, 'requests_names')
    test_body_dir = os.path.join(test_dir, 'body')
    test_body_dir = os.path.join(test_dir, 'params')
    
    user_request_path = os.path.join(request_name_dir, 'user_requests.txt')
    user_curl_path = os.path.join(requests_dir, 'curl.txt')

    # Verifica se o diretório de configuração existe; se não existir, cria
    if not os.path.exists(config_dir):
        os.makedirs(config_dir)

    # Verifica se o diretório de solicitações existe; se não existir, cria
    if not os.path.exists(requests_dir):
        os.makedirs(requests_dir)

    if not os.path.exists(test_dir):
        os.makedirs(test_dir)

    if not os.path.exists(request_name_dir):
        os.makedirs(request_name_dir)

    if not os.path.exists(test_body_dir):
        os.makedirs(test_body_dir)
        
    with open(user_request_path, 'w') as file:
        file.write("QAstronaut")
    
    with open(user_curl_path, 'w') as file:
        file.write("Paste your cURL here")



    default_test_body()
    default_test_get()

    # Define o caminho completo para o arquivo api_key.json
    api_key_file = os.path.join(config_dir, 'api_key.json')

    # Check if the api_key.json file exists
    try:
        with open(api_key_file, 'r') as config_file:
            config = json.load(config_file)

        api_key = config.get('api_key', '')

    except FileNotFoundError:
        
        message_initial = (
        """Welcome to your test suite automator!\n\n
        Before we dive into the hard work, I'll need some information.\n
        *** No information provided will be stored outside your machine ***\n"""
    )
        print('\n\n' + message_initial)

        api_key = input("What's your API key? ").strip()

        config = {
            'api_key': api_key
        }

        with open(api_key_file, 'w') as config_file:
            json.dump(config, config_file, indent=4)

    return api_key

def names():

    collection_name = input("What will the name of the collection be? ")
    folder_name = input("What will the folder name be? ")

    return collection_name, folder_name


def default_test_body():
    # Define o caminho completo do arquivo
    file_path_nonexistent = os.path.join("config", "tests", "body", "nonexistent")
    file_path_empty = os.path.join("config", "tests", "body", "empty")
    file_path_null = os.path.join("config", "tests", "body", "null")
    file_path_size = os.path.join("config", "tests", "body", "size")
    file_path_invalid = os.path.join("config", "tests", "body", "invalid")
    
    test_generic = '''var resbody = JSON.parse(responseBody)

var statusCode = 400
var messageError = ""

pm.test("Status code is " + statusCode, function () {pm.response.to.have.status(statusCode);});

pm.test("Validate error message", function () {pm.expect(resbody.message).to.be.contains(messageError);}); '''

    # Cria o arquivo e escreve o conteúdo nele
    with open(file_path_nonexistent, "w") as file:
        file.write(test_generic)
    
    with open(file_path_empty, "w") as file:
        file.write(test_generic)

    with open(file_path_null, "w") as file:
        file.write(test_generic)

    with open(file_path_invalid, "w") as file:
        file.write(test_generic)
    
    with open(file_path_size, "w") as file:
        file.write(test_generic)

def default_test_get():
    # Define o caminho completo do arquivo
    file_path_nonexistent = os.path.join("config", "tests", "params", "nonexistent")
    file_path_empty = os.path.join("config", "tests", "params", "empty")
    file_path_null = os.path.join("config", "tests", "params", "null")
    file_path_size = os.path.join("config", "tests", "params", "size")
    file_path_invalid = os.path.join("config", "tests", "params", "invalid")
    
    test_generic = '''var resbody = JSON.parse(responseBody)

var statusCode = 400
var messageError = ""

pm.test("Status code is " + statusCode, function () {pm.response.to.have.status(statusCode);});

pm.test("Response Body is not empty", function () {pm.expect(resbody).to.be.not.empty;});

pm.test("Validate error message", function () {pm.expect(resbody.message).to.be.contains(messageError);}); '''

    # Cria o arquivo e escreve o conteúdo nele
    with open(file_path_nonexistent, "w") as file:
        file.write(test_generic)
    
    with open(file_path_empty, "w") as file:
        file.write(test_generic)

    with open(file_path_null, "w") as file:
        file.write(test_generic)

    with open(file_path_invalid, "w") as file:
        file.write(test_generic)
    
    with open(file_path_size, "w") as file:
        file.write(test_generic)


def get_user_request_names():

    requests_name_arch = 'config/requests_names'
    name_file_path = os.path.join(requests_name_arch, 'user_requests.txt')
    user_request_names = []

    try:
        with open(name_file_path, "r") as file:
            lines = file.readlines()
            for line in lines:
                parts = line.strip().split(',')
                if len(parts) >= 1:
                    user_request_name = ','.join(parts)
                    user_request_names.append(user_request_name)
    except FileNotFoundError:
        print("\nThe 'user_requests' file was not found. Please create the file and add request names.")
        exit()

    return user_request_names

def lost_api_key():

    config_dir = 'config'       
    api_key_file = os.path.join(config_dir, 'api_key.json')

    # Check if the api_key.json file exists
    try:
        with open(api_key_file, 'r') as config_file:
            config = json.load(config_file)
        api_key = config.get('api_key', '')

    except FileNotFoundError:
        
        print("\nThe file api_key.json was not found")
        api_key = input("\nWhat's your API key? ").strip()
        config = {
            'api_key': api_key
        }
        with open(api_key_file, 'w') as config_file:
            json.dump(config, config_file, indent=4)

    return api_key