# app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # Importa CORS
from app.routes import announcements, boarding_gates, bus_companies, destinations, travels, users

app = FastAPI()

# Configurar CORS correctamente
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  # Asegura que tu frontend pueda acceder
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],  # Métodos permitidos
    allow_headers=["*"],  # Permitir todos los encabezados
)

# Incluir las rutas
app.include_router(announcements.router)
app.include_router(boarding_gates.router)
app.include_router(bus_companies.router)
app.include_router(destinations.router)
app.include_router(travels.router)
app.include_router(users.router)
