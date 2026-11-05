import os
import pytest
import pytest_html
import tempfile
import shutil
from selenium import webdriver
import base64
import pathlib


@pytest.fixture
def driver():
    # 1. Crear carpeta temporal aislada para los datos de sesión de Chrome
    temp_dir = tempfile.mkdtemp()
    
    # 2. Configurar opciones del navegador Chrome
    options = webdriver.ChromeOptions()
    options.add_argument(f'--user-data-dir={temp_dir}')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    options.add_argument('--remote-allow-origins=*')
    options.add_argument('--disable-gpu')
    
    # 3. Inicializar el driver de Chrome con las opciones configuradas
    browser = webdriver.Chrome(options=options)
    
    # 4. Entregar el navegador a las funciones de prueba
    yield browser
    
    # 5. Limpieza posterior al test: cerrar navegador y eliminar la carpeta temporal
    browser.quit()
    shutil.rmtree(temp_dir, ignore_errors=True)
    
@pytest.fixture
def api_headers():
    """Fixture que centraliza la API Key y las cabeceras comunes para las pruebas de API"""
    api_key = os.getenv("API_KEY")
    return {
        "x-api-key": api_key,
        "Content-Type": "application/json"
    }
    
@pytest.fixture
def base_url():
    return "https://reqres.in/api"

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    # Se ejecuta únicamente cuando la prueba falla en su fase de llamada (call)
    if report.when == "call" and report.failed:
        # Intentamos obtener el driver si el test utilizaba Selenium (UI)
        driver = item.funcargs.get("driver")

        # PROTECCIÓN API/UI: Verifica que el driver exista. 
        # Si es un test de API, 'driver' será None y evita que el hook falle por falta de navegador.
        if driver:
            carpeta = pathlib.Path("reports/screenshots")
            carpeta.mkdir(parents=True, exist_ok=True)
            archivo = carpeta / f"{item.name}.png"

            driver.save_screenshot(str(archivo))

            imagen = base64.b64encode(archivo.read_bytes()).decode("utf-8")
            report.extras = [
                pytest_html.extras.png(imagen, name="Screenshot")
            ]