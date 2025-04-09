#app/routers/videos.py
import os
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Videos
from app.schemas import Video, VideoCreate
from typing import Optional

router = APIRouter(prefix="/videos", tags=["Videos"])
# Define la ruta absoluta de la carpeta de videos
VIDEOS_DIR = os.path.join("app", "public", "videos")

@router.get("/", response_model=list[Video])
def list_videos(db: Session = Depends(get_db)):
    videos = db.query(Videos).order_by(Videos.order).all()
    return videos

@router.post("/upload", response_model=Video)
async def upload_video(
    file: UploadFile = File(...),
    title: Optional[str] = None,
    description: Optional[str] = None,
    db: Session = Depends(get_db)
):
    os.makedirs(VIDEOS_DIR, exist_ok=True)
    file_location = os.path.join(VIDEOS_DIR, file.filename)
    with open(file_location, "wb+") as file_object:
        file_object.write(await file.read())
    # Determinar el nuevo orden: máximo order + 1
    max_order = db.query(Videos.order).order_by(Videos.order.desc()).first()
    new_order = (max_order[0] + 1) if max_order else 1
    new_video = Videos(filename=file.filename, title=title, description=description, order=new_order)
    db.add(new_video)
    db.commit()
    db.refresh(new_video)
    return new_video

@router.put("/{video_id}", response_model=Video)
def update_video(video_id: int, video_data: VideoCreate, db: Session = Depends(get_db)):
    video = db.query(Videos).filter(Videos.id == video_id).first()
    if not video:
        raise HTTPException(status_code=404, detail="Video not found")
    for key, value in video_data.dict().items():
        setattr(video, key, value)
    db.commit()
    db.refresh(video)
    return video

@router.delete("/{video_id}")
def delete_video(video_id: int, db: Session = Depends(get_db)):
    video = db.query(Videos).filter(Videos.id == video_id).first()
    if not video:
        raise HTTPException(status_code=404, detail="Video not found")
    # Opcional: eliminar el archivo físico
    file_path = os.path.join(VIDEOS_DIR, video.filename)
    if os.path.exists(file_path):
        os.remove(file_path)
    db.delete(video)
    db.commit()
    return {"message": "Video eliminado"}

@router.get("/file/{video_name}")
def get_video_file(video_name: str):
    file_path = os.path.join(VIDEOS_DIR, video_name)
    return FileResponse(file_path)
