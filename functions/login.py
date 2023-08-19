import json


def login(driver):
    from selenium.webdriver.common.by import By
    from selenium import webdriver
    
    with open('login_config.json', 'r') as config_file:
        config = json.load(config_file)

    email = config.get('email')
    password = config.get('password')

    driver.get('https://winter-shuttle-884158.postman.co/workspace/My-Workspace~4319089f-eee9-4433-8d99-17f86c328e59/overview')

   # sing_in_button = driver.find_element(By.CSS_SELECTOR, 'button[type="outline"]')
   # sing_in_button.click()


    email_text_box = driver.find_element(By.ID,'input[id="username"]')
    email_text_box.click()
    email_text_box.send_keys(email)

    password_text_box = driver.find_element(By.ID,'input[id="username"]')
    password_text_box.click()
    password_text_box.send_keys(password)


