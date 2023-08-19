import json
from selenium import webdriver
from functions.welcome import welcome
from functions.login import login

if __name__ == "__main__":
    welcome()

    driver_path = json.load(open('login_config.json'))['driver_path']

        #precisa realizar uma alteração criar a opção do firefox e do edge 
    
    driver = webdriver.Chrome(executable_path=driver_path)

    login(driver)

    driver.quit()
