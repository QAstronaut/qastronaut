import json

def welcome():

    def display_welcome_message():
        message = (
            "Welcome to your test suite automator!\n\n"
            "Before we dive into the hard work, I'll need some information.\n"
            "*** No information provided will be stored outside your machine ***\n"
        )
        print(50 * '-' + 'QAstronaut' + 50 * '-')
        print('\n\n' + message)


    def get_user_information():
        try:
            with open('login_config.json', 'r') as config_file:
                config = json.load(config_file)
                email = config.get('email', '')
                password = config.get('password', '')
                browser = config.get('browser', '')
                driver_path = config.get('driver_path', '')
        except FileNotFoundError:
            email = input('Enter the email used in Postman: ')
            password = input('Enter the password used in Postman: ')

            browser = input('Which browser will you use? (chrome/edge/firefox): ')

            driver_path = None
            if browser == 'chrome':
                driver_path = input('Enter the path to the Chromedriver: ')
            elif browser == 'edge':
                driver_path = input('Enter the path to the Edge WebDriver: ')
            elif browser == 'firefox':
                driver_path = input('Enter the path to the geckodriver: ')

            config = {

                'email': email,
                'password': password,
                'browser': browser,
                'driver_path': driver_path
            }

            with open('login_config.json', 'w') as config_file:
                json.dump(config, config_file, indent=4)

        return email, password, browser, driver_path
    
    display_welcome_message()
    get_user_information()
