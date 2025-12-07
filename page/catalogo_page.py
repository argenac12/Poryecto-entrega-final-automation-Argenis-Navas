from selenium.webdriver.common.by import By
from page.base_page import BasePage

from utils.logger import logger

class CatalogPage(BasePage):

    INVENTORY_ITEM = (By.CLASS_NAME, "inventory_item")
    FILTERS = (By.CLASS_NAME, "product_sort_container")

    def is_loaded(self):
        logger.info("Verificando que la página de catalogo se haya cargado")
        self.wait_url_contains("/inventory.html")
        return True

    def get_all_products(self):
        logger.info("Obteniendo todos los productos")
        return self.find_all(self.INVENTORY_ITEM)
    
    def get_first_product_text(self):
        logger.info("Obteniendo el primer producto")
        products = self.get_all_products()

        if not products:
            logger.error("No se encontraron productos")
            return None

        return products[0].text
    
    def get_filters_text(self):
        logger.info("Obteniendo los filtros de productos")
        return self.get_text(self.FILTERS)