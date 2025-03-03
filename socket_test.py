from flask import Flask
from flask_socketio import SocketIO, emit

app = Flask(__name__)  # Creamos la aplicación Flask
socketio = SocketIO(app, cors_allowed_origins="*")  # Habilitamos WebSockets con CORS permitido

@socketio.on("connect")
def handle_connect():
    print("Cliente conectado")

@socketio.on("bus")
def handle_message(data):
    print(f"Bus recibido: {data}")
    emit("bus_actualizado", data, broadcast=True)  # Enviamos a todos los clientes

if __name__ == "__main__":
    socketio.run(app, debug=True)  # Ejecutamos la aplicación con WebSockets
