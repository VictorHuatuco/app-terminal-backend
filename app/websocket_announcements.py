from fastapi import APIRouter, WebSocket
from sqlalchemy.orm import sessionmaker
from app.database import engine
from app.models import Announcements
import asyncio

router = APIRouter()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

clients = set()  # Almacena los clientes conectados

@router.websocket("/ws/announcements")
async def websocket_endpoint(websocket: WebSocket):
    """WebSocket que envía en tiempo real los anuncios con status=True."""
    await websocket.accept()
    clients.add(websocket)

    try:
        while True:
            await asyncio.sleep(2)  # Intervalo de actualización
            await send_active_announcements()
    except Exception as e:
        print(f"❌ Error en WebSocket: {e}")
    finally:
        clients.remove(websocket)

async def send_active_announcements():
    """Obtiene anuncios activos y los envía a los clientes WebSocket."""
    db = SessionLocal()
    active_announcements = db.query(Announcements).filter(Announcements.status == True).all()
    db.close()

    # Convertir los objetos SQLAlchemy a diccionarios
    data = [{"id": ann.id, "message": ann.observation, "status": ann.status} for ann in active_announcements]

    for client in clients.copy():  # Hacemos copia para evitar errores si se desconectan clientes
        try:
            await client.send_json(data)
        except Exception:
            clients.remove(client)  # Eliminar clientes desconectados

