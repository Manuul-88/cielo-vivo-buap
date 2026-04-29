import json
import random
import os

# Buscamos la ruta de la carpeta 'data'
ruta_data = os.path.join(os.path.dirname(__file__), "..", "data")
ruta_archivo = os.path.join(ruta_data, "star.json")

estrellas = []
colores = ["#FFFFFF", "#FFDDC1", "#C1D1FF", "#FFF4E8"] # Blanco, amarillento, azulado

# Generamos 500 estrellas aleatorias
for i in range(1, 501):
    estrella = {
        "id": i,
        "x": round(random.uniform(-2000, 2000), 2),
        "y": round(random.uniform(-2000, 2000), 2),
        "z": round(random.uniform(-2000, 2000), 2), # 3D para el motor
        "brightness": round(random.uniform(0.3, 1.0), 2),
        "color": random.choice(colores)
    }
    estrellas.append(estrella)

# Guardamos todo en el archivo stars.json
with open(ruta_archivo, "w", encoding="utf-8") as f:
    json.dump(estrellas, f, indent=4)

print("¡Éxito! 500 estrellas creadas en la carpeta data.")