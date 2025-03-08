import sqlite3

def get_connection():
    """Establece y retorna la conexión a la base de datos."""
    conext = sqlite3.connect("bdterminalpv.db")
    conext.execute("PRAGMA foreign_keys = ON;")  # Activar claves foráneas
    return conext