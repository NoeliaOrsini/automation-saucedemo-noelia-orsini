import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@pytest.mark.inventory
def test_inventory(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    # 1. Navegar e iniciar sesión vía Page Object
    driver.get("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")

    # 2. Validar título y URL
    assert driver.title == "Swag Labs"
    assert "/inventory.html" in driver.current_url

    # 3. Validar productos usando ÚNICAMENTE los métodos de InventoryPage
    productos = inventory_page.obtener_productos()
    assert len(productos) > 0

    # 4. Validar primer producto 
    assert inventory_page.obtener_nombre_primer_producto() == "Sauce Labs Backpack"
    assert inventory_page.obtener_precio_primer_producto() == "$29.99"

    # 5. Validar menú y filtro usando los métodos de la clase
    assert inventory_page.menu_visible()
    assert inventory_page.filtro_visible()