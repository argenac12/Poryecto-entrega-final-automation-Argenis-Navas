from selenium.webdriver.common.by import By
from page.base_page import BasePage

from utils.logger import logger

class ProductPage(BasePage):

    ADD_TO_CART = (By.ID, "add-to-cart")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def is_loaded(self):
        logger.info("Verificando que la página de producto se haya cargado")
        self.wait_url_contains("/inventory-item.html")
        return True

    def add_to_cart(self):
        logger.info("Agregando el producto al carrito")
        self.click(self.ADD_TO_CART)

    def get_cart_badge(self):
        logger.info("Obteniendo el badge del carrito")
        return self.get_text(self.CART_BADGE)
    
    def go_to_cart(self):
        logger.info("Navegando al carrito de compras")
        self.click(self.CART_LINK)



