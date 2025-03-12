🚍 App Terminal Backend
Este proyecto es una API backend para la gestión de terminales de buses, desarrollada con FastAPI, PostgreSQL y SQLAlchemy.

📌 Requisitos previos
Antes de comenzar, asegúrate de tener instalado lo siguiente:

Python 3.8+
PostgreSQL
Git
📥 Instalación
1️⃣ Clonar el repositorio
bash
Copiar
Editar
git clone https://github.com/VictorHuatuco/app-terminal-backend.git
cd app-terminal-backend
2️⃣ Crear y activar entorno virtual
bash
Copiar
Editar
python -m venv venv
source venv/Scripts/activate  # En Windows
# source venv/bin/activate    # En macOS/Linux
3️⃣ Instalar dependencias
bash
Copiar
Editar
pip install -r requirements.txt
🗄 Configuración de la base de datos
4️⃣ Instalar PostgreSQL
Descargar e instalar PostgreSQL desde aquí.
🔹 Importante: Guarda la contraseña que configures.

5️⃣ Configurar variables de entorno
Crea un archivo .env en la carpeta raíz del proyecto y copia lo siguiente:

env
Copiar
Editar
# Configuración de PostgreSQL
PG_HOST=localhost
PG_PORT=5432
PG_USER=postgres
PG_PASSWORD=*******  # Reemplaza con la contraseña que configuraste
PG_DATABASE=postgres

# Configuración de la base de datos de la app
APP_DB_NAME=terminal_db
APP_DB_USER=admin_terminal_app
APP_DB_PASSWORD=123456
🚀 Inicialización del sistema
6️⃣ Inicializar la base de datos
bash
Copiar
Editar
python -m app.init_db
7️⃣ Crear las tablas en la base de datos
bash
Copiar
Editar
python -m app.database
8️⃣ Insertar datos iniciales (seeds)
bash
Copiar
Editar
python -m app.seed
▶️ Ejecución del servidor
Para iniciar la API, ejecuta:

bash
Copiar
Editar
uvicorn app.main:app --reload
El backend estará disponible en:
🔗 http://127.0.0.1:8000

📄 Documentación de la API
FastAPI genera automáticamente la documentación en:

📜 Swagger UI: http://127.0.0.1:8000/docs
📄 Redoc: http://127.0.0.1:8000/redoc
💡 Notas adicionales
Si tienes problemas con dependencias, intenta:

bash
Copiar
Editar
pip install --upgrade pip
Para salir del entorno virtual:

bash
Copiar
Editar
deactivate
