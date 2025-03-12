from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import models, schemas

router = APIRouter(prefix="/announcements", tags=["Announcements"])

@router.post("/", response_model=schemas.Announcement)
def create_announcement(announcement: schemas.AnnouncementCreate, db: Session = Depends(get_db)):
    db_announcement = models.Announcements(**announcement.dict())
    db.add(db_announcement)
    db.commit()
    db.refresh(db_announcement)
    return db_announcement

@router.get("/{announcement_id}", response_model=schemas.Announcement)
def get_announcement(announcement_id: int, db: Session = Depends(get_db)):
    announcement = db.query(models.Announcements).filter(models.Announcements.id == announcement_id).first()
    if announcement is None:
        raise HTTPException(status_code=404, detail="Announcement not found")
    return announcement

@router.get("/", response_model=list[schemas.Announcement])
def list_announcements(db: Session = Depends(get_db)):
    return db.query(models.Announcements).all()

@router.put("/{announcement_id}", response_model=schemas.Announcement)
def update_announcement(announcement_id: int, announcement: schemas.AnnouncementCreate, db: Session = Depends(get_db)):
    db_announcement = db.query(models.Announcements).filter(models.Announcements.id == announcement_id).first()
    if db_announcement is None:
        raise HTTPException(status_code=404, detail="Announcement not found")
    for key, value in announcement.dict().items():
        setattr(db_announcement, key, value)
    db.commit()
    db.refresh(db_announcement)
    return db_announcement

@router.delete("/{announcement_id}")
def delete_announcement(announcement_id: int, db: Session = Depends(get_db)):
    db_announcement = db.query(models.Announcements).filter(models.Announcements.id == announcement_id).first()
    if db_announcement is None:
        raise HTTPException(status_code=404, detail="Announcement not found")
    db.delete(db_announcement)
    db.commit()
    return {"message": "Announcement deleted"}
