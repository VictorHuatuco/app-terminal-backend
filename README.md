# 🚍 App Terminal Backend

Este proyecto es una API backend para la gestión de terminales de buses, desarrollada con **FastAPI**, **PostgreSQL** y **SQLAlchemy**.

---

## 📌 Requisitos previos

Antes de comenzar, asegúrate de tener instalado lo siguiente:

- [Python 3.8+](https://www.python.org/downloads/)
- [PostgreSQL](https://www.postgresql.org/download/)
- [Git](https://git-scm.com/downloads)

---

## 📥 Instalación

Sigue estos pasos para instalar y configurar el proyecto en tu entorno local.

### 1️⃣ Clonar el repositorio

Abre una terminal y ejecuta el siguiente comando:

``` bash
git clone https://github.com/VictorHuatuco/app-terminal-backend.git
```
Luego, accede a la carpeta del proyecto:

bash
Copiar
Editar
cd app-terminal-backend
2️⃣ Crear y activar el entorno virtual
Para mantener organizadas las dependencias, crea un entorno virtual:

bash
Copiar
Editar
python -m venv venv
Luego, actívalo según tu sistema operativo:

Windows (cmd o PowerShell):

bash
Copiar
Editar
venv\Scripts\activate
macOS/Linux:

bash
Copiar
Editar
source venv/bin/activate
3️⃣ Instalar las dependencias del proyecto
Una vez activado el entorno virtual, instala las dependencias con:

bash
Copiar
Editar
pip install -r requirements.txt
Esto descargará e instalará automáticamente todas las librerías necesarias para el proyecto.

🗄 Configuración de la base de datos
4️⃣ Instalar PostgreSQL
Si aún no tienes PostgreSQL instalado, descárgalo e instálalo desde aquí.
🔹 Importante: Durante la instalación, se te pedirá que configures una contraseña para el usuario postgres. Recuerda esta contraseña, ya que la necesitarás más adelante.

5️⃣ Configurar las variables de entorno
Crea un archivo .env en la carpeta raíz del proyecto y copia el siguiente contenido:

env
Copiar
Editar
# Configuración de PostgreSQL
PG_HOST=localhost
PG_PORT=5432
PG_USER=postgres
PG_PASSWORD=*******  # Reemplaza con la contraseña de PostgreSQL
PG_DATABASE=postgres

# Configuración de la base de datos de la app
APP_DB_NAME=terminal_db
APP_DB_USER=admin_terminal_app
APP_DB_PASSWORD=123456
🔹 Nota: Asegúrate de reemplazar PG_PASSWORD con la contraseña que configuraste en PostgreSQL.

🚀 Inicialización del sistema
6️⃣ Inicializar la base de datos
Ejecuta el siguiente comando para crear la base de datos:

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
