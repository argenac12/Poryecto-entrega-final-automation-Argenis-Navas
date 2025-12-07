import pytest
from selenium.webdriver.common.by import By

from page.login_page import LoginPage
from utils.data_setup import read_csv_login
from utils.logger import logger

LOGIN_CASES = read_csv_login("data/data_login.csv")

@pytest.mark.ui
@pytest.mark.parametrize("username, password, must_pass, description", LOGIN_CASES)
def test_login_parametrized(driver, username, password, must_pass, description):

    logger.info(f"Ejecutando caso de prueba: {description}")
    login = LoginPage(driver)
    login.open_login_page()
    login.login(username, password)

    if must_pass:
        logger.info("Verificando login exitoso")
        title = login.get_text((By.CLASS_NAME, "title"))
        assert "Products" in title
    else:
        logger.info("Verificando mensaje de error por login fallido")
        error_message = login.get_text((By.CLASS_NAME, "error-message-container"))
        assert "Epic sadface" in error_message