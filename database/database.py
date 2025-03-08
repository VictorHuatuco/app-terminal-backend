import sqlite3

try:
    # Conectar a la base de datos (si no existe, la crea)
    conn = sqlite3.connect("bdterminalpv.db")
    cursor = conn.cursor()

    # 🔹 ACTIVAR CLAVES FORÁNEAS EN SQLITE
    cursor.execute("PRAGMA foreign_keys = ON;")
    print("Conexión exitosa a la base de datos y claves foráneas activadas.")

    # Crear las tablas basadas en el diagrama
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS terminals (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        city TEXT NOT NULL
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        id_terminals INTEGER,
        FOREIGN KEY (id_terminals) REFERENCES terminals(id) ON DELETE SET NULL
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS boarding_gates (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        boarding_gate TEXT NOT NULL
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS bus_companies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        bus_company TEXT NOT NULL
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS destinations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        destination TEXT NOT NULL
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS travels (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_bus_companies INTEGER,
        id_destinations INTEGER,
        departure_time TEXT NOT NULL,
        plate TEXT NOT NULL,
        FOREIGN KEY (id_bus_companies) REFERENCES bus_companies(id) ON DELETE CASCADE,
        FOREIGN KEY (id_destinations) REFERENCES destinations(id) ON DELETE CASCADE
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS advertisements (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_travels INTEGER,
        id_boarding_gates INTEGER,
        id_users INTEGER,
        date_advertisement TEXT NOT NULL,
        status TEXT NOT NULL,
        FOREIGN KEY (id_travels) REFERENCES travels(id) ON DELETE CASCADE,
        FOREIGN KEY (id_boarding_gates) REFERENCES boarding_gates(id) ON DELETE CASCADE,
        FOREIGN KEY (id_users) REFERENCES users(id) ON DELETE CASCADE
    );
    ''')

    # save commits
    conn.commit()
    print("Base de datos y tablas creadas con éxito.")

except sqlite3.Error as e:
    print(f"Error en la base de datos: {e}")

finally:
    # Cerramos la conexión siempre, incluso si hay un error
    if conn:
        conn.close()
        print("Conexión cerrada.")
