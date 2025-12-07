import pytest

from utils.data_setup import read_json_products
from utils.logger import logger

from page.login_page import LoginPage
from page.catalogo_page import CatalogPage

PRODUCTS = read_json_products("data/data_login.json")

@pytest.fixture
def logged_user(driver):
    logger.info("Login con standard_user")
    login = LoginPage(driver)
    login.open_login_page()
    login.login("standard_user", "secret_sauce")
    assert login.is_loaded()
    logger.info("Login exitoso")
    return login.driver

@pytest.mark.ui
@pytest.mark.parametrize("product", PRODUCTS)
def test_catalog_parametrized(logged_user, product):

    logger.info(f"Buscando producto: {product['name']}")
    catalog = CatalogPage(logged_user)

    inventory_items = catalog.get_all_products()
    assert len(inventory_items) > 0

    logger.info(f"Verificando el producto: {product['name']} si encuentre en la lista")

    inventory_texts = [item.text for item in inventory_items]
    assert any(product["name"] in text for text in inventory_texts)
