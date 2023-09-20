import os
import json

def welcome():
    message = (
        """Welcome to your test suite automator!\n\n
        Before we dive into the hard work, I'll need some information.\n
        *** No information provided will be stored outside your machine ***\n"""
    )
    print(30 * '-' + 'QAstronaut' + 30 * '-')
    print('\n\n' + message)

    # Define o diretório de configuração
    config_dir = 'config'
        # Define o diretório de solicitações dentro do diretório de configuração
    requests_dir = os.path.join(config_dir, 'requests')

    # Verifica se o diretório de configuração existe; se não existir, cria
    if not os.path.exists(config_dir):
        os.makedirs(config_dir)

    # Verifica se o diretório de solicitações existe; se não existir, cria
    if not os.path.exists(requests_dir):
        os.makedirs(requests_dir)

    # Define o caminho completo para o arquivo api_key.json
    api_key_file = os.path.join(config_dir, 'api_key.json')

    # Check if the api_key.json file exists
    try:
        with open(api_key_file, 'r') as config_file:
            config = json.load(config_file)

            api_key = config.get('api_key', '')
            collection_name = input("What will the name of the collection be? ")
            folder_name = input("What will the folder name be? ")

    except FileNotFoundError:
        api_key = input("What's your API key? ")
        collection_name = input("What will the name of the collection be? ")
        folder_name = input("What will the folder name be? ")

        config = {
            'api_key': api_key
        }

        with open(api_key_file, 'w') as config_file:
            json.dump(config, config_file, indent=4)

    return api_key, collection_name, folder_name
