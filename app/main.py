# app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # Importa CORS
from app.routes import travels, announcements, bus_companies, destinations, users

app = FastAPI()

# Habilitar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Puedes restringirlo a 'http://localhost:4200'
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Permite todos los encabezados
)

# Incluir las rutas
app.include_router(travels.router)
app.include_router(announcements.router)
app.include_router(bus_companies.router)
app.include_router(destinations.router)
app.include_router(users.router)
