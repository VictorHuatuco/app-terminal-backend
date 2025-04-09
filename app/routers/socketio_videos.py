#app/socketio_videos.py
import socketio
from sqlalchemy.orm import sessionmaker
from app.database import engine
from app.models import Videos
from app.schemas import Video as VideoSchema
from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
import asyncio

sio = socketio.AsyncServer(async_mode="asgi", cors_allowed_origins="http://localhost:4200")
sio_app = socketio.ASGIApp(sio)
router = APIRouter()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@sio.event
async def connect(sid, environ):
    print(f"Socket.IO (videos): Cliente conectado: {sid}")

@sio.event
async def disconnect(sid):
    print(f"Socket.IO (videos): Cliente desconectado: {sid}")

async def broadcast_videos():
    db = SessionLocal()
    try:
        videos = db.query(Videos).order_by(Videos.order).all()
        data = [jsonable_encoder(VideoSchema.model_validate(video)) for video in videos]
    finally:
        db.close()
    await sio.emit("videos", data)

@router.get("/broadcast")
async def trigger_video_broadcast():
    await broadcast_videos()
    return {"message": "Broadcast videos realizado"}
