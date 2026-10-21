import pytest
import tempfile
import shutil
from selenium import webdriver

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