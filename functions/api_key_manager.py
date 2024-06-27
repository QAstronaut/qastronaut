import os
import json
import requests

import os
import json
import requests

def load_api_key():
   
    config_dir = 'config'
    api_key_file = os.path.join(config_dir, 'api_key.json')

    def is_valid_postman_api_key(api_key):
       
        url = 'https://api.getpostman.com/me'
        headers = {
            'X-Api-Key': api_key
        }
        
        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                return True
            else:
                return False
        except requests.RequestException as e:
            print(f"An error occurred: {e}")
            return False

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

        os.makedirs(config_dir, exist_ok=True)
        with open(api_key_file, 'w') as config_file:
            json.dump(config, config_file, indent=4)

    while not is_valid_postman_api_key(api_key):
        error_api_message = "The API key is invalid or the file api_key.json was not found."
        print('\n\n' + error_api_message)
        api_key = input("Please enter a valid Postman API KEY: ").strip()

        config = {
            'api_key': api_key
        }

        os.makedirs(config_dir, exist_ok=True)
        with open(api_key_file, 'w') as config_file:
            json.dump(config, config_file, indent=4)

    return api_key



def lost_api_key():
    
    config_dir = 'config'
    api_key_file = os.path.join(config_dir, 'api_key.json')

    def is_valid_postman_api_key(api_key):
       
        url = 'https://api.getpostman.com/me'
        headers = {
            'X-Api-Key': api_key
        }
        
        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                return True
            else:
                return False
        except requests.RequestException as e:
            print(f"An error occurred: {e}")
            return False

    # Check if the api_key.json file exists
    try:
        with open(api_key_file, 'r') as config_file:
            config = json.load(config_file)
        api_key = config.get('api_key', '')
    except (FileNotFoundError, ValueError):
        api_key = ''

    while not is_valid_postman_api_key(api_key):
        error_api_message = "The API key is invalid or the file api_key.json was not found."
        print('\n\n' + error_api_message)
        api_key = input("Please enter a valid Postman API KEY: ").strip()

        config = {
            'api_key': api_key
        }

        # Ensure the config directory exists
        os.makedirs(config_dir, exist_ok=True)
        
        with open(api_key_file, 'w') as config_file:
            json.dump(config, config_file, indent=4)

    return api_key



