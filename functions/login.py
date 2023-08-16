from selenium import webdriver

chrome_driver_path = "home/asafe/drivers/chromedriver.exe"
chrome_driver = webdriver.Chrome(executable_path=chrome_driver_path)

def login(email, password):
    chrome_driver.get('https://www.postman.com/')