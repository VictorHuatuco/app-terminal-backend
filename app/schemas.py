from pydantic import BaseModel
from datetime import date, time

# BusCompany Schema
class BusCompanyBase(BaseModel):
    bus_company: str

class BusCompanyCreate(BusCompanyBase):
    pass

class BusCompany(BusCompanyBase):
    id: int

    class Config:
        orm_mode = True

# Destination Schema
class DestinationBase(BaseModel):
    destination: str

class DestinationCreate(DestinationBase):
    pass

class Destination(DestinationBase):
    id: int

    class Config:
        orm_mode = True

# BoardingGate Schema
class BoardingGateBase(BaseModel):
    boarding_gate: str

class BoardingGateCreate(BoardingGateBase):
    pass

class BoardingGate(BoardingGateBase):
    id: int

    class Config:
        orm_mode = True

# Travel Schema (Se define antes de Announcement)
class TravelBase(BaseModel):
    id_bus_companies: int
    id_destinations: int
    departure_time: time
    plate: str

class TravelCreate(TravelBase):
    pass

class Travel(TravelBase):
    id: int
    bus_company: BusCompany  # Relación con BusCompany
    destination: Destination  # Relación con Destination

    class Config:
        orm_mode = True

# Announcement Schema
class AnnouncementBase(BaseModel):
    id_travels: int
    id_boarding_gates: int
    id_users: int
    date_advertisement: date
    status: bool

class AnnouncementCreate(AnnouncementBase):
    pass

class Announcement(AnnouncementBase):
    id: int
    travel: Travel
    boarding_gate: BoardingGate  

    class Config:
        orm_mode = True

# User Schema
class UserBase(BaseModel):
    name: str
    email: str
    password: str
    id_terminals: int

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

# Terminal Schema
class TerminalBase(BaseModel):
    name: str
    city: str

class TerminalCreate(TerminalBase):
    pass

class Terminal(TerminalBase):
    id: int

    class Config:
        orm_mode = True
