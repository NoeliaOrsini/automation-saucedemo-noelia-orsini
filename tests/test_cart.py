import pytest
from pages.login_page import LoginPage
from pages.cart_page import CartPage

@pytest.mark.cart
def test_agregar_al_carrito(driver):
    login_page = LoginPage(driver)
    cart_page = CartPage(driver)

    # 1. Ingresar a la página e iniciar sesión mediante LoginPage
    driver.get("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")

    # 2. Agregar el producto al carrito mediante la CartPage
    cart_page.agregar_backpack_al_carrito()

    # 3. Verificar si se agregó: comprobar que el numerito (badge) del carrito diga "1"
    assert cart_page.obtener_numero_badge() == "1"

    # 4. Entrar al carrito y confirmar que cambió la dirección web (URL)
    cart_page.ir_al_carrito()
    assert "/cart.html" in driver.current_url

    # 5. Confirmar si adentro del carrito está el producto correcto con su nombre y precio
    assert cart_page.obtener_nombre_item() == "Sauce Labs Backpack"
    assert cart_page.obtener_precio_item() == "$29.99"