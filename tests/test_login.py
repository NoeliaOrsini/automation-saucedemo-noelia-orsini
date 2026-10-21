import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from utils.reader import read_users_csv

@pytest.mark.login
@pytest.mark.parametrize("data", read_users_csv())
def test_login(driver, data):
    wait = WebDriverWait(driver, 10)
    login_page = LoginPage(driver)

    # 1. Navegar a SauceDemo e ingresar credenciales desde el CSV
    driver.get("https://www.saucedemo.com/")
    login_page.login(data["usuario"], data["password"])

    # 2. Validación para usuarios válidos (caso positivo)
    if data["tipo_usuario"] == "True":
        # Valida redirección y elementos clave de la interfaz post-login
        assert "/inventory.html" in driver.current_url

        logo = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "app_logo")))
        assert logo.text == "Swag Labs"

        titulo = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-test="title"]')))
        assert titulo.text == "Products"

    # 3. Validación para usuarios inválidos (caso negativo)
    elif data["tipo_usuario"] == "False":
        # Valida mensaje de error en pantalla para credenciales incorrectas
        error = login_page.obtener_mensaje_error()
        assert "Epic sadface" in error