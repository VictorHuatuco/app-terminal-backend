from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import models

def seed_data(db: Session):
    # Crear terminales
    terminal1 = models.Terminals(name="Terminal Central", city="Lima")
    terminal2 = models.Terminals(name="Terminal Norte", city="Trujillo")
    db.add_all([terminal1, terminal2])
    db.commit()

    # Crear empresas de buses
    bus_company1 = models.BusCompanies(bus_company="Expreso Lima")
    bus_company2 = models.BusCompanies(bus_company="Transportes Andinos")
    db.add_all([bus_company1, bus_company2])
    db.commit()

    # Crear destinos
    destination1 = models.Destinations(destination="Arequipa")
    destination2 = models.Destinations(destination="Cusco")
    db.add_all([destination1, destination2])
    db.commit()

    # Crear puertas de embarque
    gate1 = models.BoardingGates(boarding_gate="Puerta 1")
    gate2 = models.BoardingGates(boarding_gate="Puerta 2")
    db.add_all([gate1, gate2])
    db.commit()

    # Crear usuarios
    user1 = models.Users(name="Juan Perez", email="juan@example.com", password="1234", id_terminals=terminal1.id)
    user2 = models.Users(name="Maria López", email="maria@example.com", password="5678", id_terminals=terminal2.id)
    db.add_all([user1, user2])
    db.commit()

    # Crear viajes
    travel1 = models.Travels(id_bus_companies=bus_company1.id, id_destinations=destination1.id, departure_time="08:30:00", plate="ABC-123")
    travel2 = models.Travels(id_bus_companies=bus_company2.id, id_destinations=destination2.id, departure_time="14:15:00", plate="XYZ-789")
    db.add_all([travel1, travel2])
    db.commit()

    # Crear anuncios
    announcement1 = models.Announcements(id_travels=travel1.id, id_boarding_gates=gate1.id, id_users=user1.id, date_advertisement="2025-03-12", status=True)
    announcement2 = models.Announcements(id_travels=travel2.id, id_boarding_gates=gate2.id, id_users=user2.id, date_advertisement="2025-03-12", status=False)
    db.add_all([announcement1, announcement2])
    db.commit()

    print("✅ Seed completado con éxito.")

if __name__ == "__main__":
    db = SessionLocal()
    seed_data(db)
    db.close()
