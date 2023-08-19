import json

def welcome():

    message = (
        """Welcome to your test suite automator!\n\n
        Before we dive into the hard work, I'll need some information.\n
        *** No information provided will be stored outside your machine ***\n"""
    )
    print(30 * '-' + 'QAstronaut' + 30 * '-')
    print('\n\n' + message)

    # Check if the login_config.json file exists
    try:
        with open('api_key.json', 'r') as config_file:
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

        with open('api_key.json', 'w') as config_file:
            json.dump(config, config_file, indent=4)

    return api_key, collection_name, folder_name
 