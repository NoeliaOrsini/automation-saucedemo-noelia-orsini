import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.inventory
def test_inventory(driver):
    # 1. Instanciar la espera explícita (WebDriverWait) para este test
    wait = WebDriverWait(driver, 10)

    # 2. Navegar e iniciar sesión previa en SauceDemo
    driver.get("https://www.saucedemo.com/")

    usuario = wait.until(EC.presence_of_element_located((By.ID, "user-name")))
    password = wait.until(EC.presence_of_element_located((By.ID, "password")))
    boton_login = wait.until(EC.element_to_be_clickable((By.ID, "login-button")))

    usuario.send_keys("standard_user")
    password.send_keys("secret_sauce")
    boton_login.click()

    # 3. Validar título del sitio y URL de inventario
    assert driver.title == "Swag Labs"
    assert "/inventory.html" in driver.current_url

    # 4. Comprobar que existan productos visibles en la página
    productos = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item")))
    assert len(productos) > 0

    # 5. Validar el primer producto (requerido) y productos adicionales
    producto_1 = productos[0]
    nombre_1 = producto_1.find_element(By.CLASS_NAME, "inventory_item_name").text
    precio_1 = producto_1.find_element(By.CLASS_NAME, "inventory_item_price").text
    assert nombre_1 == "Sauce Labs Backpack"
    assert precio_1 == "$29.99"

    producto_2 = productos[1]
    nombre_2 = producto_2.find_element(By.CLASS_NAME, "inventory_item_name").text
    precio_2 = producto_2.find_element(By.CLASS_NAME, "inventory_item_price").text
    assert nombre_2 == "Sauce Labs Bike Light"
    assert precio_2 == "$9.99"

    producto_3 = productos[2]
    nombre_3 = producto_3.find_element(By.CLASS_NAME, "inventory_item_name").text
    precio_3 = producto_3.find_element(By.CLASS_NAME, "inventory_item_price").text
    assert nombre_3 == "Sauce Labs Bolt T-Shirt"
    assert precio_3 == "$15.99"

    # 6. Validar presencia de elementos importantes de la interfaz (menú, filtro y carrito)
    menu = wait.until(EC.presence_of_element_located((By.ID, "react-burger-menu-btn")))
    assert menu.is_displayed()

    filtro = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product_sort_container")))
    assert filtro.is_displayed()

    icono_carrito = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_link")))
    assert icono_carrito.is_displayed()