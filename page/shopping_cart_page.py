from selenium.webdriver.common.by import By
from page.base_page import BasePage

from utils.logger import logger

class ShoppingCartPage(BasePage):

    CART_ITEM = (By.CLASS_NAME, "cart_item")
    CART_ITEM_LABEL = (By.CLASS_NAME, "cart_item_label")
    CART_QUANTITY = (By.CLASS_NAME, "cart_quantity")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def is_loaded(self):
        logger.info("Verificando que la página de carrito se haya cargado")
        self.wait_url_contains("/cart.html")
        return True

    def get_cart_items(self):
        logger.info("Obteniendo los elementos del carrito")
        return self.find_all(self.CART_ITEM)
    
    def get_first_item_name(self):
        logger.info("Obteniendo el nombre del primer elemento del carrito")
        items = self.get_cart_items()

        if not items:
            logger.error("No se encontraron elementos en el carrito")
            return None
        
        return items[0].find_element(*self.CART_ITEM_LABEL).text
    
    def get_first_item_quantity(self):
        logger.info("Obteniendo la cantidad del primer elemento del carrito")
        items = self.get_cart_items()

        if not items:
            logger.error("No se encontraron elementos en el carrito")
            return None
        
        return items[0].find_element(*self.CART_QUANTITY).text
    
    def get_checkout_text(self):
        logger.info("Obteniendo el texto del botón de checkout")
        return self.get_text(self.CHECKOUT_BUTTON)
    
    def go_to_checkout(self):
        logger.info("Navegando a la página de checkout")
        self.click(self.CHECKOUT_BUTTON)
