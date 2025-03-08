import sqlite3

# Conecta a la base de datos y en caso no existe la crea
conn = sqlite3.connect("bdterminalpv.db")
print("Conexión exitosa a la base de datos")

# Crear un cursor para ejecutar sentencias SQL
cursor = conn.cursor()

# Cerrar la conexión (siempre que no se esté ejecutando algo)
conn.close()