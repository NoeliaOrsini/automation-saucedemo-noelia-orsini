# SauceDemo — Automation Testing Suite

Este repositorio contiene la suite de pruebas automatizadas para la plataforma web SauceDemo ([saucedemo.com](https://www.saucedemo.com)).

El objetivo principal es validar la estabilidad y funcionalidad crítica de los flujos clave de la aplicación demo aplicando Selenium WebDriver, Pytest y buenas prácticas de arquitectura de software.

## 📌 Flujos Automatizados

1. **Autenticación (Login):** Validación de credenciales válidas, verificación de elementos clave de la interfaz (logo, título) y confirmación de la redirección al catálogo (`/inventory.html`).
2. **Navegación y Catálogo (Inventory):** Verificación de la carga de productos, validación de nombres/precios dinámicos e inspección de componentes de navegación.
3. **Gestión del Carrito (Cart):** Adición de productos al carrito, verificación del contador dinámico (*badge*) en la interfaz y confirmación de ítems dentro de la vista detallada del carrito.

## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** Python 3.13+
* **Framework de Testing:** Pytest
* **Automatización Web:** Selenium WebDriver
* **Arquitectura de Pruebas:** Pytest Fixtures (`conftest.py`)
* **Reporte de Pruebas:** pytest-html
* **Control de Versiones:** Git & GitHub

## 📁 Estructura del Repositorio

```text
automation-saucedemo-noelia-orsini/
│
├── assets/                 # Evidencias y reportes visuales de ejecución
├── data/                   # Archivos de datos de prueba (CSV/JSON)
│   ├── users.csv           # Datos parametrizados para autenticación (DDT)
│   └── products.json       # Datos de productos para inventario y carrito
├── pages/                  # Patrón Page Object Model (POM)
│   ├── __init__.py         # Inicializador del paquete pages
│   ├── login_page.py       # Acciones y selectores de la vista de login
│   ├── inventory_page.py   # Acciones y selectores del catálogo
│   └── cart_page.py        # Acciones y selectores del carrito
├── report/                 # Reporte HTML autónomo (reporte.html)
├── tests/                  # Suite de pruebas automatizadas
│   ├── test_login.py       # Pruebas del módulo de autenticación
│   ├── test_inventory.py   # Pruebas del catálogo de productos
│   └── test_cart.py        # Pruebas del módulo de carrito
├── utils/                  # Funciones auxiliares y helpers
│   ├── __init__.py         # Inicializador del paquete utils
│   └── reader.py           # Lectores centralizados para CSV y JSON
├── conftest.py             # Fixture global (inicialización del driver y teardown)
├── pytest.ini              # Configuración centralizada de Pytest y marcadores
├── README.md               # Documentación técnica del proyecto
└── requirements.txt        # Lista de dependencias del proyecto
```
## 🧩 Componentes Arquitectónicos Principales

- **Page Object Model (`pages/`):** 
  Implementa el patrón de diseño POM para desacoplar los selectores y la lógica de interacción web del código de prueba. Cada pantalla principal (`LoginPage`, `InventoryPage`, `CartPage`) cuenta con su propia clase dedicada, garantizando un mantenimiento limpio y escalable.

- **Data-Driven Testing & Helpers (`data/` y `utils/`):** 
  Los datos de entrada están completamente separados del código de ejecución mediante archivos estructurados en formato CSV (`users.csv`) y JSON (`products.json`). El módulo centralizado `utils/reader.py` se encarga de leerlos de forma dinámica y segura, permitiendo parametrizar las pruebas sin alterar la lógica de los tests.

## ⚙️ Instalación y Configuración

1. **Clonar el repositorio:**

   ```bash
   git clone [https://github.com/NoeliaOrsini/automation-saucedemo-noelia-orsini.git](https://github.com/NoeliaOrsini/automation-saucedemo-noelia-orsini.git)
   cd automation-saucedemo-noelia-orsini
   ```

2. **Crear y activar un entorno virtual:**
* **Windows:**
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
* **macOS/Linux:**
     ```bash
     python -m venv venv
     source venv/bin/activate
     ```

3. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

## 🔧 Decisiones Técnicas y Arquitectura del Framework

Para garantizar la máxima estabilidad, portabilidad y un uso eficiente de los recursos del sistema (optimizando la ejecución en entornos restringidos de memoria RAM), el framework incorpora las siguientes decisiones de diseño:

1. **Gestión Centralizada con Fixtures (`conftest.py`):**
   Uso de `@pytest.fixture` para inicializar el navegador y garantizar su cierre (`driver.quit()`) mediante `yield`, reduciendo código duplicado y asegurando la liberación de recursos.

2. **Aislamiento de Sesión y Perfiles Temporales (`tempfile`):**
   Cada prueba genera una carpeta temporal única con `tempfile.mkdtemp()` asignada a `--user-data-dir`. Esto elimina colisiones de sesiones previas, previene errores de puertos bloqueados (`DevToolsActivePort`) y garantiza ejecuciones independientes.

3. **Banderas de Estabilidad en `ChromeOptions`:**
   * `--no-sandbox`: Evita restricciones de permisos del sistema operativo.
   * `--disable-dev-shm-usage`: Fuerza el uso de la memoria RAM principal evitando el límite del almacenamiento compartido `/dev/shm`.
   * `--remote-allow-origins=*`: Autoriza las conexiones locales del ChromeDriver sin bloqueos de seguridad.
   * `--disable-gpu`: Desactiva la aceleración gráfica por hardware para optimizar el consumo de recursos.

4. **Estrategia de Esperas Explícitas (Explicit Waits):**
   Para garantizar la máxima estabilidad y evitar falsos negativos por desincronización, las pruebas prescinden de esperas fijas (`time.sleep`) y utilizan exclusivamente **esperas explícitas mediante `WebDriverWait` y `expected_conditions`**. Esto permite aguardar dinámicamente a que los elementos del DOM estén presentes o sean cliqueables (como botones de login, ítems y el contador del carrito) antes de interactuar con ellos.

5. **Reportes HTML Autónomos Centralizados (`pytest.ini`):**
   El archivo `pytest.ini` define la opción `addopts = -v -s --html=report/reporte.html --self-contained-html`, generando un informe visual consolidado en un solo archivo dentro de `report/reporte.html`.

6. Arquitectura Page Object Model (POM) y Data-Driven Testing (DDT):
El proyecto implementa formalmente el patrón Page Object Model (POM) en la carpeta pages/, desacoplando por completo la lógica de interacción de los elementos web (locators) del código de prueba propiamente dicho. Asimismo, se aplica Data-Driven Testing (DDT) mediante archivos externos users.csv y products.json ubicados en data/, centralizando su lectura a través de funciones seguras en utils/reader.py. Esto permite escalar la cobertura de pruebas de forma limpia sin duplicar código ni modificar las rutinas de testeo.

## 🧪 Ejecución de Pruebas

Debido a la preconfiguración en `pytest.ini`, podés disparar la ejecución completa con un solo comando:

```bash
pytest
```

### Ejecución por Marcadores (*Markers*):
Para filtrar la ejecución por módulos específicos:

```bash
# Módulo de Login
pytest -m login

# Módulo de Inventario
pytest -m inventory

# Módulo de Carrito
pytest -m cart
```

## 📸 Evidencias de Ejecución

Los resultados gráficos e informes de prueba se encuentran respaldados en la carpeta `assets/`:

* **Prueba Módulo Login (`test_login.py`):**  
  ![Resultado Test Login](assets/test_login.png)

* **Prueba Módulo Inventario (`test_inventory.py`):**  
  ![Resultado Test Inventario](assets/test_inventario.png)

* **Prueba Módulo Carrito (`test_cart.py`):**  
  ![Resultado Test Carrito](assets/test_cart.png)

*(El informe interactivo detallado en formato HTML se genera automáticamente en `report/reporte.html` tras cada ejecución).*

## 👩‍💻 Autora

**Noelia Orsini**  
*Desarrolladora Back-End | Abogada | Consultora Psicológica*

Soy Abogada, Counselor y Programadora. Trabajo en la intersección del derecho con la tecnología aportando una mirada humana, perfeccionándome constantemente en inteligencia artificial, desarrollo de software y procesos de automatización.

* **LinkedIn:** [noelia-orsini](https://www.linkedin.com/in/noelia-orsini/)
* **Portafolio:** [noelia-orsini-portafolio](https://noelia-orsini-portafolio.lovable.app/)

---
*Proyecto realizado para el curso AUTOMATIZACION QA de Talento Tech.*