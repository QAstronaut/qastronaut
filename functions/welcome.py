import os
import json

# Define a variável name_file_path
requests_name_arch = 'config/requests_names'
name_file_path = os.path.join(requests_name_arch, 'user_requests')

def welcome():

    message_initial = (
        """\nWelcome to your test suite automator!\n\n
        Before we dive into the hard work, I'll need some information.\n
        *** No information provided will be stored outside your machine ***\n"""
    )

    # Define o diretório de configuração
    config_dir = 'config'
    requests_dir = 'config/requests'
    test_dir = 'config/tests'
    request_name_dir ='config/request_name'
    test_body_dir = 'config/tests/body'
    test_params_dir = 'config/tests/params'

    # Define o diretório de solicitações dentro do diretório de configuração
    requests_dir = os.path.join(config_dir, 'requests')
    test_dir = os.path.join(config_dir, 'tests')
    request_name_dir = os.path.join(config_dir, 'requests_names')
    test_body_dir = os.path.join(test_dir, 'body')
    test_params_dir = os.path.join(test_dir, 'params')
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

    if not os.path.exists(test_params_dir):
        os.makedirs(test_params_dir)

    default_test()

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


def default_test():
    # Define o caminho completo do arquivo
    file_path_nonexistent = os.path.join("config", "tests", "body", "nonexistent")
    file_path_empty = os.path.join("config", "tests", "body", "empty")
    file_path_size = os.path.join("config", "tests", "body", "size")
    file_path_invalid = os.path.join("config", "tests", "body", "invalid")


    
    test_nonexistent = '''var resbody = JSON.parse(responseBody)

var statusCode = 400
var messageError = ""
var messageJsonPath = "resbody.message"

pm.test("Status code is " + statusCode, function () {pm.response.to.have.status(statusCode);});

pm.test("Validate error message", function () {pm.expect(messageJsonPath).to.be.contains(messageError);}); '''

    test_empty = '''var resbody = JSON.parse(responseBody)

var statusCode = 400
var messageError = ""
var messageJsonPath = "resbody.message"

pm.test("Status code is " + statusCode, function () {pm.response.to.have.status(statusCode);});

pm.test("Validate error message", function () {pm.expect(messageJsonPath).to.be.contains(messageError);}); '''

    test_size = '''var resbody = JSON.parse(responseBody)

var statusCode = 400
var messageError = ""
var messageJsonPath = "resbody.message"

pm.test("Status code is " + statusCode, function () {pm.response.to.have.status(statusCode);});

pm.test("Validate error message", function () {pm.expect(messageJsonPath).to.be.contains(messageError);}); '''

    test_invalid = '''var resbody = JSON.parse(responseBody)

var statusCode = 400
var messageError = ""
var messageJsonPath = "resbody.message"

pm.test("Status code is " + statusCode, function () {pm.response.to.have.status(statusCode);});

pm.test("Validate error message", function () {pm.expect(messageJsonPath).to.be.contains(messageError);}); '''

    # Cria o arquivo e escreve o conteúdo nele
    with open(file_path_nonexistent, "w") as file:
        file.write(test_nonexistent)
    
    with open(file_path_empty, "w") as file:
        file.write(test_empty)

    with open(file_path_size, "w") as file:
        file.write(test_size)

    with open(file_path_invalid, "w") as file:
        file.write(test_invalid)

# Adicione a função get_user_request_names() 

def get_user_request_names():
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