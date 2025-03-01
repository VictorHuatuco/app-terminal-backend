from flask import Flask
from flask_socketio import SocketIO, emit

app = Flask(_name_)  # Creamos la aplicación Flask
socketio = SocketIO(app, cors_allowed_origins="*")  # Habilitamos WebSockets con CORS permitido

@socketio.on("connect")
def handle_connect():
    print("Cliente conectado")

@socketio.on("pedido")
def handle_message(data):
    print(f"Pedido recibido: {data}")
    emit("pedido_actualizado", f"Nuevo pedido: {data}", broadcast=True)  # Enviamos a todos los clientes

if _name_ == "_main_":
    socketio.run(app, debug=True)