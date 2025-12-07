from selenium.webdriver.common.by import By
from page.base_page import BasePage

from utils.logger import logger

class CheckoutPage(BasePage):

    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    ZIP_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")

    def is_loaded(self, step):
        logger.info(f"Verificando que la página de checkout {step} se haya cargado")
        self.wait_url_contains(f"/checkout-{step}.html")
        return True

    def fill_checkout_form(self, first_name, last_name, zip_code):
        logger.info("Llenando formulario de checkout")
        self.write(self.FIRST_NAME, first_name)
        self.write(self.LAST_NAME, last_name)
        self.write(self.ZIP_CODE, zip_code)
        self.click(self.CONTINUE_BUTTON)

    def finish_checkout(self):
        logger.info("Finalizando el checkout")
        self.click(self.FINISH_BUTTON)

    def get_complete_header(self):
        logger.info("Obteniendo el texto del encabezado de completado")
        return self.get_text(self.COMPLETE_HEADER)