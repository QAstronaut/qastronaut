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
                return True, response.status_code
            else:
                return False, response.status_code
        except requests.RequestException as e:
            print(f"An error occurred: {e}")
            return False, None

    try:
        with open(api_key_file, 'r') as config_file:
            config = json.load(config_file)
        api_key = config.get('api_key', '')

    except FileNotFoundError:
        # Simulate a 404 error if the API key file does not exist. Reminder: 404 error in postman is a client error response, where "This status code indicates that the requested resource was not found on the server."
        print("\n\nThe API key file was not found. HTTP Status Code: 404")
        api_key = input("Please enter a valid Postman API KEY: ").strip()

        config = {
            'api_key': api_key
        }

        os.makedirs(config_dir, exist_ok=True)
        with open(api_key_file, 'w') as config_file:
            json.dump(config, config_file, indent=4)

    valid, status_code = is_valid_postman_api_key(api_key)
    while not valid:
        error_api_message = f"The API key is invalid. HTTP Status Code: {status_code}"
        print('\n\n' + error_api_message)
        api_key = input("Please enter a valid Postman API KEY: ").strip()

        config = {
            'api_key': api_key
        }

        os.makedirs(config_dir, exist_ok=True)
        with open(api_key_file, 'w') as config_file:
            json.dump(config, config_file, indent=4)

        valid, status_code = is_valid_postman_api_key(api_key)

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
                return True, response.status_code
            else:
                return False, response.status_code
        except requests.RequestException as e:
            print(f"An error occurred: {e}")
            return False, None

    try:
        with open(api_key_file, 'r') as config_file:
            config = json.load(config_file)
        api_key = config.get('api_key', '')
    except (FileNotFoundError, ValueError):
        # Simulate a 404 error if the API key file does not exist. Reminder: 404 error in postman is a client error response, where "This status code indicates that the requested resource was not found on the server."
        print("\n\nThe API key file was not found. HTTP Status Code: 404")
        api_key = input("Please enter a valid Postman API KEY: ").strip()

        config = {
            'api_key': api_key
        }

        os.makedirs(config_dir, exist_ok=True)
        with open(api_key_file, 'w') as config_file:
            json.dump(config, config_file, indent=4)

    valid, status_code = is_valid_postman_api_key(api_key)
    while not valid:
        error_api_message = f"The API key is invalid. HTTP Status Code: {status_code}"
        print('\n\n' + error_api_message)
        api_key = input("Please enter a valid Postman API KEY: ").strip()

        config = {
            'api_key': api_key
        }

        os.makedirs(config_dir, exist_ok=True)
        with open(api_key_file, 'w') as config_file:
            json.dump(config, config_file, indent=4)

        valid, status_code = is_valid_postman_api_key(api_key)

    return api_key
