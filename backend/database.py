import json
import os

# Ruta donde se guardarán los datos en la carpeta 'data'
DB_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "universo.json")

def obtener_planetas():
    # Si el archivo no existe, devolvemos una lista vacía
    if not os.path.exists(DB_PATH):
        return []
    with open(DB_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def guardar_nuevo_planeta(datos_planeta: dict):
    planetas = obtener_planetas()
    planetas.append(datos_planeta)
    with open(DB_PATH, "w", encoding="utf-8") as f:
        json.dump(planetas, f, indent=4, ensure_ascii=False)
    return {"status": "success", "message": "Planeta lanzado al universo"}