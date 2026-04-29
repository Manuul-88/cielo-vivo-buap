from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.models import Planeta
from backend.database import obtener_planetas, guardar_nuevo_planeta

# crear la app
app = FastAPI()

# agrega middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#ENDPOINTS
@app.get("/api/planets")
def get_planets():
    return obtener_planetas()

@app.post("/api/planets")
def create_planet(planeta: Planeta):
    return guardar_nuevo_planeta(planeta.dict())