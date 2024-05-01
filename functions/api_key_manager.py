import os
import json
import sys

def load_api_key():
    config_dir = 'config'
    api_key_file = os.path.join(config_dir, 'api_key.json')

    try:
        with open(api_key_file, 'r') as config_file:
            # Verificar se o arquivo não está vazio
            if os.stat(api_key_file).st_size == 0:
                raise ValueError("The api_key.json is empty")

            config = json.load(config_file)
            api_key = config.get('api_key', '')



    except (FileNotFoundError, ValueError) as error:
        # Lidar com a exceção aqui
        print("The API key is missing, invalid, or the api_key.json file is empty.")
        print(error)
        sys.exit(1)  

    return api_key

def lost_api_key():

    config_dir = 'config'       
    api_key_file = os.path.join(config_dir, 'api_key.json')

    # Check if the api_key.json file exists
    try:
        with open(api_key_file, 'r') as config_file:
            config = json.load(config_file)
        api_key = config.get('api_key', '')



    except (FileNotFoundError, ValueError):
        
        # Lidar com a exceção aqui
        print("The API key is missing, invalid, or the api_key.json file is empty.")
        api_key = input("What is your API KEY? ").strip()
        

    return api_key
