# app/main.py

from fastapi import FastAPI
from app.routes import travels, announcements, bus_companies, destinations, users

app = FastAPI()

app.include_router(travels.router)
app.include_router(announcements.router)
app.include_router(bus_companies.router)
app.include_router(destinations.router)
app.include_router(users.router)
