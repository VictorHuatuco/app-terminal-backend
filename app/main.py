from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # Importa CORS
from app.routers import announcements, boarding_gates, bus_companies, destinations, travels, users, socketio_announcements

app = FastAPI()

# Configurar CORS correctamente
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  # Asegura que tu frontend pueda acceder
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"],  # Métodos permitidos
    allow_headers=["*"],  # Permitir todos los encabezados
)

# Incluir las rutas HTTP
app.include_router(announcements.router)
app.include_router(boarding_gates.router)
app.include_router(bus_companies.router)
app.include_router(destinations.router)
app.include_router(travels.router)
app.include_router(users.router)

# Incluir la ruta Socket.IO para los announcements
app.include_router(socketio_announcements.router)

# Montar la aplicación Socket.IO
app.mount("/socket.io", socketio_announcements.sio_app)

@app.get("/")
def root():
    return {"message": "API con Socket.IO en ejecución"}
