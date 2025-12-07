from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.logger import logger

class BasePage:

    def __init__(self, driver, timeout=5):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)


    def open(self, url):
        logger.info(f"Abriendo la URL: {url}")
        self.driver.get(url)

    def click(self, locator):
        logger.info(f"Click en: {locator}")
        self.wait.until(EC.element_to_be_clickable(locator)).click()
    
    def write(self, locator, text):
        logger.info(f"Escribiendo en {locator}: {text}")
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        logger.info(f"Obteniendo el texto de: {locator}")
        return self.wait.until(EC.presence_of_element_located(locator)).text
    
    def find(self, locator):
        logger.info(f"Buscando: {locator}")
        return self.wait.until(EC.presence_of_element_located(locator))
    
    def find_all(self, locator):
        logger.info(f"Buscando todos los elementos: {locator}")
        return self.driver.find_elements(*locator)
    

    def wait_url_contains(self, fragment):
        logger.info(f"Esperando que la URL contenga: {fragment}")
        self.wait.until(EC.url_contains(fragment))

    def is_visible(self, locator):
        try:
            logger.info(f"Verificando visibilidad de: {locator}")
            self.wait.until(EC.visibility_of_element_located(locator))
            logger.info(f"Elemento visible: {locator}")
            return True
        except:
            logger.error(f"Elemento no visible: {locator}")
            return False

    def screenshot(self, name):
        path = f"reports/screenshots/{name}.png"
        self.driver.get_screenshot_as_file(path)
        return path
