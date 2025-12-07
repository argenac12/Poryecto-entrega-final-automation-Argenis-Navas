from selenium.webdriver.common.by import By
from page.base_page import BasePage

from utils.logger import logger

class LoginPage(BasePage):

    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def open_login_page(self):
        logger.info("Abriendo la página de login")
        self.open("https://www.saucedemo.com/")
    
    def is_loaded(self):
        logger.info("Verificando que la página de login se haya cargado")
        self.wait_url_contains("/inventory.html")
        return True

    def login(self, username, password):
        logger.info(f"Iniciando sesión con el usuario: {username}")
        self.write(self.USERNAME, username)
        self.write(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)