import csv
import json
import os

def read_users_csv():
    """
    Lee el archivo 'users.csv' ubicado en la carpeta 'data/'.
    Construye una ruta absoluta dinámica basada en la ubicación del proyecto
    para evitar errores de lectura independientemente de dónde se ejecute el comando.
    Retorna una lista de diccionarios con los datos de los usuarios.
    """
    # 1. Obtiene la ruta raíz del proyecto (sube 2 niveles desde utils/reader.py)
    base_path = os.path.dirname(os.path.dirname(__file__))
    
    # 2. Une las carpetas asegurando compatibilidad en cualquier sistema operativo (Windows/Linux/Mac)
    file_path = os.path.join(base_path, "data", "users.csv")
    
    # 3. Abre el archivo con codificación UTF-8 para evitar problemas con tildes o caracteres especiales
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        # csv.DictReader lee cada fila como un diccionario usando los encabezados como claves
        return list(csv.DictReader(csvfile))


def read_products_json():
    """
    Lee el archivo 'products.json' ubicado en la carpeta 'data/'.
    Retorna los datos estructurados en formato de lista u objeto según la estructura JSON.
    """
    # 1. Construye la ruta absoluta segura hacia el JSON de productos
    base_path = os.path.dirname(os.path.dirname(__file__))
    file_path = os.path.join(base_path, "data", "products.json")
    
    # 2. Carga y parsea el archivo JSON a un tipo de dato nativo de Python (lista/diccionario)
    with open(file_path, encoding='utf-8') as jsonfile:
        return json.load(jsonfile)