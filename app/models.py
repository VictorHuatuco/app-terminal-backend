# app/models.py

from sqlalchemy import Column, Integer, String, Boolean, Date, Time, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Announcements(Base):
    __tablename__ = "announcements"

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_travels = Column(Integer, ForeignKey("travels.id"))
    id_boarding_gates = Column(Integer, ForeignKey("boarding_gates.id"))
    id_users = Column(Integer, ForeignKey("users.id"))
    date_advertisement = Column(Date)
    status = Column(Boolean)

class BusCompanies(Base):
    __tablename__ = "bus_companies"

    id = Column(Integer, primary_key=True, autoincrement=True)
    bus_company = Column(String)

class Destinations(Base):
    __tablename__ = "destinations"

    id = Column(Integer, primary_key=True, autoincrement=True)
    destination = Column(String)

    travels_list = relationship("Travels", back_populates="destination")


class BoardingGates(Base):
    __tablename__ = "boarding_gates"

    id = Column(Integer, primary_key=True, autoincrement=True)
    boarding_gate = Column(String)

class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    id_terminals = Column(Integer, ForeignKey("terminals.id"))

class Terminals(Base):
    __tablename__ = "terminals"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    city = Column(String)

class Travels(Base):
    __tablename__ = "travels"

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_bus_companies = Column(Integer, ForeignKey("bus_companies.id"))
    id_destinations = Column(Integer, ForeignKey("destinations.id"))
    departure_time = Column(Time)
    plate = Column(String)

    # Relaciones
    bus_company = relationship("BusCompanies", backref="travels")
    destination = relationship("Destinations", back_populates="travels_list")

    # Relaciones
    bus_company = relationship("BusCompanies", backref="travels")
    destination = relationship("Destinations", back_populates="travels_list")
