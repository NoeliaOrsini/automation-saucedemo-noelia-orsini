import pytest
import requests

@pytest.mark.api
def test_obtener_usuario(api_headers):
    url = "https://reqres.in/api/users/2"
    
    # Uso fixture para validar credenciales de la API
    response = requests.get(url, headers=api_headers)

    # NIVEL 1: STATUS CODE
    codigo = response.status_code
    assert codigo == 200

    # NIVEL 2: HEADERS
    assert "application/json" in response.headers["Content-Type"]

    # NIVEL 3: ESTRUCTURA
    data = response.json()

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

    # NIVEL 5: TIEMPO DE RESPUESTA
    assert response.elapsed.total_seconds() < 2


@pytest.mark.api
def test_crear_usuario(api_headers):
    url = "https://reqres.in/api/users/"
    
    usuario = {
        "email": "jose.montezuma@bue.edu.ar",
        "first_name": "Jose",
        "last_name": "Montezuma",
        "job": "Instructor"
    }

    # Uso fixture para validar credenciales de la API
    response = requests.post(url, headers=api_headers, json=usuario)

    # NIVEL 1: STATUS CODE (201 Created)
    assert response.status_code == 201

    # NIVEL 2: HEADERS
    assert "application/json" in response.headers["Content-Type"]

    # NIVEL 3: ESTRUCTURA
    data = response.json()
    assert isinstance(data, dict)
    assert "email" in data
    assert "first_name" in data
    assert "last_name" in data
    assert "job" in data
    assert "id" in data

    # NIVEL 4: CONTENIDO COMPLETO
    assert data["email"] == usuario["email"]
    assert data["first_name"] == usuario["first_name"]
    assert data["last_name"] == usuario["last_name"]
    assert data["job"] == usuario["job"]
    assert data["id"] is not None

    # NIVEL 5: TIEMPO DE RESPUESTA
    assert response.elapsed.total_seconds() < 2