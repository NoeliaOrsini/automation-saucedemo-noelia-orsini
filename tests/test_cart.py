import pytest
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from utils.logger import logger
from utils.reader import read_products_json

@pytest.mark.cart
def test_agregar_al_carrito(driver):
    login_page = LoginPage(driver)
    cart_page = CartPage(driver)

    try:
        logger.info("Iniciando prueba de adición al carrito en SauceDemo")
        # 1. Ingresar a la página e iniciar sesión mediante LoginPage
        driver.get("https://www.saucedemo.com/")
        login_page.login("standard_user", "secret_sauce")
        logger.info("Login exitoso con 'standard_user' para prueba de carrito")

        # 2. Agregar el producto al carrito mediante la CartPage
        cart_page.agregar_backpack_al_carrito()
        logger.info("Producto 'Sauce Labs Backpack' agregado al carrito")

        # 3. Verificar si se agregó: comprobar que el numerito (badge) del carrito diga "1"
        badge_num = cart_page.obtener_numero_badge()
        assert badge_num == "1"
        logger.info(f"Badge del carrito verificado correctamente con valor: {badge_num}")

        # 4. Entrar al carrito y confirmar que cambió la dirección web (URL)
        cart_page.ir_al_carrito()
        assert "/cart.html" in driver.current_url
        logger.info("Navegación al carrito validada (URL: /cart.html)")

        # 5. Confirmar si adentro del carrito está el producto correcto con su nombre y precio
        productos_json = read_products_json()
        producto_esperado = productos_json[0]
        nombre_item = cart_page.obtener_nombre_item()
        precio_item = cart_page.obtener_precio_item()
        assert nombre_item == producto_esperado["nombre"]
        assert precio_item == producto_esperado["precio"]
        logger.info(f"Ítem validado en carrito - Producto: '{nombre_item}', Precio: '{precio_item}'")
    
    except Exception:
        logger.exception("Error crítico durante la prueba del carrito de compras")
        raise