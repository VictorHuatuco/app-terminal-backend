import json
from datetime import datetime
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
    # buscar informacion completa del bus a partir de la data enviada desde del front
    # ejm por mientras
    # Construcción del objeto con la data recibida
    hora_actual = datetime.now().strftime('%H:%M')
    dataBus = {
        "id": "22",
        "company": data.get("company"),  # Usa .get() para evitar errores si no existe la clave
        "destination": data.get("destination"),
        "arrivalTime": hora_actual,
        "boardingGate": data.get("boardingGate"),
    }

    # mandar la data al front para mostrar
    emit("bus_actualizado", dataBus, broadcast=True)  # Enviamos a todos los clientes
    print(f"Bus enviado: {dataBus}")

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5001, debug=True)
  # Ejecutamos la aplicación con WebSockets
