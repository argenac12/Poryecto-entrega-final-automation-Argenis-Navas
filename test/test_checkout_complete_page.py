import pytest
from selenium.webdriver.common.by import By

from page.login_page import LoginPage
from page.catalogo_page import CatalogPage
from page.product_page import ProductPage
from page.shopping_cart_page import ShoppingCartPage
from page.checkout_complete_page import CheckoutPage

from utils.logger import logger

@pytest.fixture
def logged_user(driver):
    logger.info("Logueándose con standard_user")
    login = LoginPage(driver)
    login.open_login_page()
    login.login("standard_user", "secret_sauce")
    assert login.is_loaded()
    logger.info("Login exitoso")
    return login.driver

@pytest.mark.ui
def test_checkout(logged_user):

    catalog = CatalogPage(logged_user)

    logger.info("Seleccionando el primer producto del catálogo")
    inventory_items = catalog.get_all_products()
    inventory_items[0].find_element(By.TAG_NAME, "a").click()

    product = ProductPage(logged_user)
    assert product.is_loaded()

    logger.info("Agregando el producto al carrito")
    product.add_to_cart()
    assert product.get_cart_badge() == "1"

    logger.info("Navegando al carrito de compras")
    product.go_to_cart()

    cart = ShoppingCartPage(logged_user)
    assert cart.is_loaded()
    
    logger.info("Verificando que se haya agregado el producto al carrito")
    cart_items = cart.get_cart_items()
    assert len(cart_items) > 0

    assert "Backpack" in cart.get_first_item_name()
    assert "1" in cart.get_first_item_quantity()

    logger.info("Iniciando el proceso de checkout")
    checkout_text = cart.get_checkout_text()
    assert "Checkout" in checkout_text

    logger.info("Navegando a la página de checkout")
    cart.go_to_checkout()

    checkout = CheckoutPage(logged_user)
    assert checkout.is_loaded("step-one")

    logger.info("Completando el formulario de checkout")
    checkout.fill_checkout_form("Jollie", "Ollie", "69420")
    assert checkout.is_loaded("step-two")

    logger.info("Finalizando el proceso de checkout")
    checkout.finish_checkout()
    assert checkout.is_loaded("complete")

    logger.info("Verificando que el checkout se haya completado exitosamente")
    complete_header = checkout.get_complete_header()
    assert "Thank you for your order!" in complete_header
   
