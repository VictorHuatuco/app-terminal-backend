import sqlite3
from db_connection import get_connection

# Aquí la función para insertar una nueva empresa de buses/:
def create_bus_company(name):
    """Inserta una nueva empresa de buses a la base de datos"""
    conext = get_connection()
    insert_bus = conext.cursor()
    insert_bus.execute("INSERT INTO bus_companies (bus_company) VALUES (?)", (name,))
    conext.commit()
    conext.close()

# Está es la función para obtener todas las empresas de buses:_:
def get_bus_companies():
    """Obten todas las empresas de buses registradas"""
    conext = get_connection()
    trae_bus = conext.cursor()
    trae_bus.execute("SELECT * FROM bus_companies")
    companies = trae_bus.fetchall()
    conext.close()
    return companies

# Aquí para insertar un nuevo destino/:
def create_destination(name):
    """Inserta un nuevo destino en la base de datos"""
    conext = get_connection()
    insert_dest = conext.cursor()
    insert_dest.execute("INSERT INTO destinations (destination) VALUES (?)", (name,))
    conext.commit()
    conext.close()

# Aquí para obtener todos los destinos:_:
def get_destinations():
    """Obten todos los destinos registrados"""
    conext = get_connection()
    leer_dest = conext.cursor()
    leer_dest.execute("SELECT * FROM destinations")
    destinations = leer_dest.fetchall()
    conext.close()
    return destinations

# Función para insertar un nuevo viaje/:
def create_travel(bus_company_id, destination_id, departure_time, plate):
    """Inserta un nuevo viaje a la base de datos"""
    conext = get_connection()
    create_viaje = conext.cursor()
    create_viaje.execute("""
        INSERT INTO travels (id_bus_companies, id_destinations, departure_time, plate)
        VALUES (?, ?, ?, ?)""", (bus_company_id, destination_id, departure_time, plate))
    conext.commit()
    conext.close()

# Función para obtener todos los viajes:_:
def get_travels():
    """Obtiene todos los viajes registrados con ombre de empresa y destino"""
    conext = get_connection()
    trae_viaje = conext.cursor()
    trae_viaje.execute("""
        SELECT travels.id, bus_companies.bus_company, destinations.destination, travels.departure_time, travels.plate
        FROM travels
        JOIN bus_companies ON travels.id_bus_companies = bus_companies.id
        JOIN destinations ON travels.id_destinations = destinations.id
    """)
    travels = trae_viaje.fetchall()
    conext.close()
    return travels

# Función para actualizar un viaje:)
def update_travel(travel_id, bus_company_id, destination_id, departure_time, plate):
    """Actualiza los datos de un viaje existente"""
    conext = get_connection()
    update_viaje = conext.cursor()
    update_viaje.execute("""
        UPDATE travels 
        SET id_bus_companies = ?, id_destinations = ?, departure_time = ?, plate = ?
        WHERE id = ?
    """, (bus_company_id, destination_id, departure_time, plate, travel_id))
    conext.commit()
    conext.close()

# Función para eliminar un viaje._.
def delete_travel(travel_id):
    """Elimina un viaje de la base de datos"""
    conext = get_connection()
    delete_viaje = conext.cursor()
    delete_viaje.execute("DELETE FROM travels WHERE id = ?", (travel_id,))
    conext.commit()
    conext.close()
