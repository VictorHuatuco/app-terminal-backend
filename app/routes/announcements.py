from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload
from app.database import get_db
from app import models, schemas
from app.schemas import TravelCreate, Travel, BoardingGate

router = APIRouter(prefix="/announcements", tags=["Announcements"])

@router.post("/")
def create_announcement(announcement: schemas.AnnouncementCreate, db: Session = Depends(get_db)):
    db_announcement = models.Announcements(**announcement.dict())
    db.add(db_announcement)
    db.commit()
    db.refresh(db_announcement)
    return {"message": "success", "data": db_announcement}

@router.get("/{announcement_id}", response_model=schemas.Announcement)
def get_announcement(announcement_id: int, db: Session = Depends(get_db)):
    announcement = db.query(models.Announcements).filter(models.Announcements.id == announcement_id).first()
    if announcement is None:
        raise HTTPException(status_code=404, detail="Announcement not found")
    return announcement

@router.get("/", response_model=list[schemas.Announcement])
def list_announcements(db: Session = Depends(get_db)):
    announcements = (
        db.query(models.Announcements)
        .options(
            joinedload(models.Announcements.travel).joinedload(models.Travels.bus_company),
            joinedload(models.Announcements.travel).joinedload(models.Travels.destination),
            joinedload(models.Announcements.boarding_gate),
        )
        .all()
    )
    return announcements

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

@router.patch("/{announcement_id}/status", response_model=schemas.Announcement)
def update_announcement_status(
    announcement_id: int, 
    status: bool, 
    db: Session = Depends(get_db)
):
    db_announcement = db.query(models.Announcements).filter(models.Announcements.id == announcement_id).first()
    
    if db_announcement is None:
        raise HTTPException(status_code=404, detail="Announcement not found")
    
    db_announcement.status = status
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
