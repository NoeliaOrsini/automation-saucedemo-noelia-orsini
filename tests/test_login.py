import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.login
def test_login_exitoso(driver):
    # 1. Instanciar la espera explícita (WebDriverWait) para un tiempo máximo de 10 segundos
    wait = WebDriverWait(driver, 10)

    # 2. Navegar a la página de login de SauceDemo
    driver.get("https://www.saucedemo.com/")

    # 3. Ubicar elementos del formulario e ingresar credenciales con esperas explícitas (EC)
    usuario = wait.until(EC.presence_of_element_located((By.ID, "user-name")))
    password = wait.until(EC.presence_of_element_located((By.ID, "password")))
    boton_login = wait.until(EC.element_to_be_clickable((By.ID, "login-button")))

    usuario.send_keys("standard_user")
    password.send_keys("secret_sauce")
    boton_login.click()

    # 4. Validar redirección exitosa a la URL de inventario
    assert "/inventory.html" in driver.current_url

    # 5. Validar elementos clave de la interfaz post-login
    logo = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "app_logo")))
    assert logo.text == "Swag Labs"

    titulo = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-test="title"]')))
    assert titulo.text == "Products"