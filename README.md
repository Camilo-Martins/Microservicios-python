# 🏪 Sistema de Gestión de Tienda, Productos y Empleados

Proyecto de **portafolio** orientado a demostrar buenas prácticas en **arquitectura backend**, **contenedorización con Docker** y **separación de responsabilidades** entre servicios.

---

## 🎯 Objetivo del proyecto

Construir un sistema modular para la gestión de:

- **Autenticación y usuarios**
- **Productos y stock**
- **Empleados / RRHH**

El foco del proyecto no es solo la funcionalidad, sino:

- diseño limpio
- uso correcto de Docker
- configuración desacoplada
- estructura defendible en entrevistas técnicas

---

## 🧱 Arquitectura general

El sistema está compuesto por **múltiples microservicios**, cada uno con:

- su propia aplicación Django
- su propia base de datos MySQL
- configuración independiente vía variables de entorno

```text
PYTHONMS/
├── authMS/      # Autenticación y usuarios
├── storeMS/     # Productos y stock
├── rrhhMS/      # Empleados
├── frontend/    # Vue 3
└── docker-compose.yml
```

Cada servicio se comunica a través de la red interna de Docker Compose.

---

## ⚙️ Stack tecnológico

### Backend

- Python 3
- Django
- MySQL
- Django REST Framework (si aplica)

### Frontend

- Vue 3
- Vite

### Infraestructura

- Docker
- Docker Compose

---

## 🐳 Docker y contenedores

### Principios aplicados

- Un servicio = un contenedor
- Una base de datos por microservicio
- Bases de datos **no expuestas** al host por defecto
- Variables de entorno externalizadas (`.env`)
- Volúmenes para persistencia de datos

---

## 🔐 Configuración por variables de entorno

El proyecto utiliza un archivo `.env` como **fuente única de configuración**.

Ejemplo:

```env
# Base de datos (ejemplo authMS)
DB_HOST=
DB_NAME=
DB_USER=
DB_PASSWORD=

MYSQL_ROOT_PASSWORD=root
```

> ⚠️ El archivo `.env` **no se versiona**. Se incluye un `.env.example`.

---

## ▶️ Ejecución del proyecto (local)

### Requisitos

- Docker
- Docker Compose

### Levantar el sistema

```bash
docker-compose up --build
```

Accesos:

- Backend (ejemplo authMS): `http://localhost:8001`
- Frontend: `http://localhost:5173`

---

## 🗄️ Migraciones

Una vez levantado el sistema:

```bash
docker-compose exec authms python manage.py migrate
docker-compose exec authms python manage.py createsuperuser
```

(Repetir por cada microservicio si aplica).

---

## 🧠 Decisiones de diseño destacadas

- No se usan credenciales hardcodeadas en el código
- El backend es agnóstico a Docker (12-factor style)
- Cada microservicio puede evolucionar de forma independiente
- Configuración pensada para portafolio y entrevistas

---

## 📌 Estado del proyecto

🟢 En desarrollo activo

Próximos pasos:

- Documentar endpoints
- Agregar autenticación JWT
- Integración frontend-backend
- Tests básicos por servicio

---

## 👤 Autor

**Camilo**
Ingeniero Informático – SOC Entry Level
Interés en arquitectura backend, Docker y microservicios

---

## 📝 Nota

Este proyecto fue construido con fines **educativos y de portafolio**, priorizando claridad arquitectónica y buenas prácticas por sobre complejidad innecesaria.
