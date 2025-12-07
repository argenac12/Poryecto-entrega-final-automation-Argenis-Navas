from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
# import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = 'https://www.saucedemo.com/'
USERNAME = 'standard_user'
PASSWORD = 'secret_sauce'

def get_driver():

    # options  = Options()
    # options.add_argument('--start-maximized')


    #instalacion de driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)


    # time.sleep(5)
    driver.implicitly_wait(5)
    # driver.implicitly_wait(10)

    return driver










