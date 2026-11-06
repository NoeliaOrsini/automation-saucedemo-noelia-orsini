import pytest
import requests
from utils.logger import logger


@pytest.mark.api
def test_obtener_usuario(base_url, api_headers):
    url = f"{base_url}/users/2"
    logger.info(f"Iniciando prueba GET para obtener usuario en: {url}")
    
    # Uso fixture para validar credenciales de la API
    response = requests.get(url, headers=api_headers)

    try:
        # NIVEL 1: STATUS CODE
        codigo = response.status_code
        assert codigo == 200
        logger.info("Nivel 1 verificado: Status Code 200 OK.")

        # NIVEL 2: HEADERS
        assert "application/json" in response.headers["Content-Type"]
        logger.info("Nivel 2 verificado: Content-Type application/json presente.") 
        # NIVEL 3: ESTRUCTURA
        data = response.json()
        logger.info("Nivel 3 verificado: La clave 'data' está presente en la respuesta.")

        assert isinstance(data, dict) # Validar que el contenido sea un diccionario
        assert "data" in data
        assert isinstance(data["data"], dict)

        assert "id" in data["data"]
        assert "email" in data["data"]
        assert "first_name" in data["data"]
        assert "last_name" in data["data"]

        # NIVEL 4: CONTENIDO COMPLETO
        usuario = data["data"]
        assert usuario["id"] == 2
        assert usuario["email"] == "janet.weaver@reqres.in"
        assert usuario["first_name"] == "Janet"
        assert usuario["last_name"] == "Weaver"
        logger.info("Nivel 4 verificado: Contenido completo del usuario validado correctamente.")
        
        # NIVEL 5: TIEMPO DE RESPUESTA
        assert response.elapsed.total_seconds() < 5
        logger.info(f"Nivel 5 verificado: Tiempo de respuesta óptimo ({response.elapsed.total_seconds()}s).")
        
        logger.info("Prueba test_obtener_usuario finalizada con éxito.")
    except Exception as e:
        logger.exception(f"Error crítico durante la prueba de API en test_obtener_usuario: {e}")
        raise    
    
@pytest.mark.api
def test_crear_usuario(base_url, api_headers):
    url = f"{base_url}/users/"
    
    usuario = {
        "email": "jose.montezuma@bue.edu.ar",
        "first_name": "Jose",
        "last_name": "Montezuma",
        "job": "Instructor"
    }
    logger.info(f"Iniciando prueba POST para crear usuario en: {url} con datos: {usuario}")
    
    # Uso fixture para validar credenciales de la API
    response = requests.post(url, headers=api_headers, json=usuario)

    try:
        # NIVEL 1: STATUS CODE (201 Created)
        assert response.status_code == 201
        logger.info("Nivel 1 verificado: Status Code 201 Created.")

        # NIVEL 2: HEADERS
        assert "application/json" in response.headers["Content-Type"]
        logger.info("Nivel 2 verificado: Content-Type application/json presente.")

        # NIVEL 3: ESTRUCTURA
        data = response.json()
        assert isinstance(data, dict)
        assert "email" in data
        assert "first_name" in data
        assert "last_name" in data
        assert "job" in data
        assert "id" in data
        logger.info("Nivel 3 verificado: Estructura de respuesta de creación validada.")
        
        # NIVEL 4: CONTENIDO COMPLETO
        assert data["email"] == usuario["email"]
        assert data["first_name"] == usuario["first_name"]
        assert data["last_name"] == usuario["last_name"]
        assert data["job"] == usuario["job"]
        assert data["id"] is not None
        logger.info("Nivel 4 verificado: Contenido completo del usuario creado validado.")
        
        # NIVEL 5: TIEMPO DE RESPUESTA
        assert response.elapsed.total_seconds() < 5
        logger.info(f"Nivel 5 verificado: Tiempo de respuesta óptimo ({response.elapsed.total_seconds()}s).")
        
        logger.info("Prueba test_crear_usuario finalizada con éxito.")
    except Exception as e:
        logger.exception(f"Error crítico durante la prueba de API en test_crear_usuario: {e}")
        raise         

@pytest.mark.api
def test_eliminar_usuario(base_url, api_headers):
    
    url = f"{base_url}/users/2"
    
    logger.info(f"Iniciando prueba de eliminación (DELETE) en la URL: {url}")
    
    response = requests.delete(url, headers=api_headers)
    
    logger.info(f"Respuesta recibida. Código de estado: {response.status_code}, Tiempo: {response.elapsed.total_seconds()}s")
    
    try:
        # NIVEL 1: STATUS CODE
        assert response.status_code == 204
        logger.info("Nivel 1 verificado: Status Code 204 OK.")
        
        # NIVEL 2: HEADERS
        assert "Content-Type" not in response.headers
        logger.info("Nivel 2 verificado: Content-Type ausente como se esperaba para 204.")
        
        # NIVEL 3 Y 4: ESTRUCTURA Y CONTENIDO
        assert len(response.content) == 0
        logger.info("Nivel 3 y 4 verificado: Contenido de la respuesta vacío.")
        
        # NIVEL 5: TIEMPO DE RESPUESTA
        assert response.elapsed.total_seconds() < 5
        logger.info(f"Nivel 5 verificado: Tiempo de respuesta óptimo ({response.elapsed.total_seconds()}s).")
        
        logger.info("Prueba test_eliminar_usuario finalizada con éxito.")
    
    except Exception as e:
        logger.exception(f"Error crítico durante la prueba de API en test_eliminar_usuario: {e}")
        raise