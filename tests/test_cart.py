import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.cart
def test_agregar_al_carrito(driver):
    # Crear la espera explicita de hasta 10 segundos
    wait = WebDriverWait(driver, 10)

    # Abrir la pagina de SauceDemo
    driver.get("https://www.saucedemo.com/")

    # Buscar e ingresar el usuario
    usuario = wait.until(EC.presence_of_element_located((By.ID, "user-name")))
    usuario.send_keys("standard_user")
    
    # Buscar e ingresar la contrasena
    password = wait.until(EC.presence_of_element_located((By.ID, "password")))
    password.send_keys("secret_sauce")
    
    # Hacer clic en el boton de login
    boton_login = wait.until(EC.element_to_be_clickable((By.ID, "login-button")))
    boton_login.click()

    # Hacer clic en 'Add to cart' del primer producto
    boton_add_cart = wait.until(
        EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
    )
    boton_add_cart.click()

    # Verificar que el badge del carrito muestre '1'
    badge_carrito = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
    )
    assert badge_carrito.text == "1"

    # Ir a la vista del carrito
    icono_carrito = wait.until(
        EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))
    )
    icono_carrito.click()

    # Validar que la URL sea /cart.html
    assert "/cart.html" in driver.current_url

    # Validar nombre y precio del producto en el carrito
    nombre_item = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_item_name"))
    ).text
    precio_item = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_item_price"))
    ).text

    assert nombre_item == "Sauce Labs Backpack"
    assert precio_item == "$29.99"