import os
import json
import sys

def load_api_key():
    config_dir = 'config'
    
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
        message_initial = (
        """Welcome to your test suite automator!\n\n
        Before we dive into the hard work, I'll need some information.\n
        *** No information provided will be stored outside your machine ***\n"""
    )
        print('\n\n' + message_initial)
        api_key = input("What is your API KEY? ").strip()
        

    return api_key
