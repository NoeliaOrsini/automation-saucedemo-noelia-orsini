import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.logger import logger
from utils.reader import read_products_json


@pytest.mark.inventory
def test_inventory(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    try:
        logger.info("Iniciando prueba de inventario en SauceDemo")

        # 1. Navegar e iniciar sesión vía Page Object
        driver.get("https://www.saucedemo.com/")
        login_page.login("standard_user", "secret_sauce")
        logger.info("Login exitoso con 'standard_user' para prueba de inventario")

        # 2. Validar título y URL
        assert driver.title == "Swag Labs"
        assert "/inventory.html" in driver.current_url
        logger.info("Título ('Swag Labs') y URL (/inventory.html) validados correctamente")

        # 3. Validar productos usando ÚNICAMENTE los métodos de InventoryPage
        productos = inventory_page.obtener_productos()
        assert len(productos) > 0
        logger.info(f"Productos cargados correctamente - Cantidad total: {len(productos)}")

        # 4. Validar primer producto 

        productos_json = read_products_json()
        producto_esperado = productos_json[0]
        nombre_primer_producto = inventory_page.obtener_nombre_primer_producto()
        precio_primer_producto = inventory_page.obtener_precio_primer_producto()
        assert nombre_primer_producto == producto_esperado["nombre"]
        assert precio_primer_producto == producto_esperado["precio"]
        logger.info(f"Primer producto validado - Nombre: '{nombre_primer_producto}', Precio: '{precio_primer_producto}'")


        # 5. Validar menú y filtro usando los métodos de la clase
        assert inventory_page.menu_visible()
        assert inventory_page.filtro_visible()
        logger.info("Menú hamburguesa y filtro de ordenamiento visibles en inventario")

    except Exception:
        logger.exception("Error crítico durante la prueba de inventario")
        raise