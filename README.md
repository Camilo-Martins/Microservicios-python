# 🏪 Sistema de Gestión Operativa para Pequeños Comercios

Proyecto de portafolio enfocado en el diseño y construcción de un **sistema backend realista**, pensado para la operación diaria de un **comercio pequeño (tienda de barrio)**.

El objetivo del proyecto es demostrar **criterio técnico**, buenas prácticas y capacidad de **modelar un dominio real**, priorizando claridad arquitectónica por sobre complejidad innecesaria.

---

## 🎯 Propósito del proyecto

Este sistema está orientado a un **dueño o administrador de tienda**, que necesita gestionar la operación diaria de forma simple:

- gestión de empleados
- control básico de la información laboral
- base para asistencia, pagos y horarios

❌ No es un sistema corporativo  
❌ No gestiona contratos, bonos ni liquidaciones  
❌ No busca cubrir todos los casos legales  

El foco está en **simplicidad, realismo y mantenibilidad**.

---

## 🧱 Arquitectura general

El proyecto está dividido en **microservicios independientes**, cada uno con una responsabilidad clara:

```

PYTHONMS/
├── authMS/      # Autenticación de administradores (JWT)
├── rrhhMS/      # Gestión operativa de empleados
├── storeMS/     # Productos y stock (en desarrollo)
├── frontend/    # Vue 3 (en desarrollo)
└── docker-compose.yml

````

Cada microservicio:
- es una aplicación Django independiente
- tiene su propia base de datos MySQL
- se configura exclusivamente mediante variables de entorno
- se comunica a través de la red interna de Docker Compose

---

## 🔐 Autenticación y modelo de acceso

- Solo los **administradores/dueños** se autentican en el sistema
- Autenticación basada en **JWT**
- Los empleados **no son usuarios del sistema**
- El acceso a los datos se controla por:
  - identidad validada por token
  - pertenencia de los recursos al admin autenticado

---

## ⚙️ Stack tecnológico

### Backend
- Python 3
- Django
- Django REST Framework
- MySQL

### Frontend
- Vue 3 (planeado)
- Vite

### Infraestructura
- Docker
- Docker Compose

---

## 🐳 Docker y contenedores

Principios aplicados:

- Un microservicio = un contenedor
- Una base de datos por microservicio
- Bases de datos no expuestas al host
- Variables de entorno externalizadas (`.env`)
- Volúmenes para persistencia de datos

El backend es **agnóstico a Docker**, siguiendo principios tipo *12-factor app*.

---

## 🔧 Configuración por variables de entorno

Toda la configuración sensible se gestiona mediante un archivo `.env`.

Ejemplo:

```env
DB_HOST=
DB_NAME=
DB_USER=
DB_PASSWORD=
MYSQL_ROOT_PASSWORD=
````

El archivo `.env` **no se versiona**.
Se incluye un `.env.example` como referencia.

---

## ▶️ Ejecución local

### Requisitos

* Docker
* Docker Compose

### Levantar el sistema

```bash
docker-compose up --build
```

Ejemplo de accesos:

* authMS: [http://localhost:8001](http://localhost:8001)
* rrhhthMS: [http://localhost:8003](http://localhost:8003)
* storethMS: [http://localhost:8004](http://localhost:8004) (proximamente)
* frontend: [http://localhost:5173](http://localhost:5173) (proximamente)

---

## 🧠 Decisiones de diseño destacadas

* Separación clara entre autenticación y dominios de negocio
* Empleados modelados como entidades operativas, no como usuarios
* JWT como contrato entre servicios
* Soft delete para mantener historial
* Alcance acotado y defendible en entrevistas técnicas

---

## 📌 Estado del proyecto

🟢 **En desarrollo activo**

### Funcionalidades actuales

* CRUD completo de empleados
* Endpoints protegidos por JWT
* Acceso filtrado por dueño (multi-tenant)

### Próximos pasos

* Documentación de la API con Swagger
* Registro de asistencia diaria
* Registro de pagos diarios
* Frontend básico en Vue
* Tests básicos por servicio

---

## 👤 Autor

**Camilo**
Ingeniero Informático

Interés en:

* arquitectura backend
* Docker y microservicios
* diseño de sistemas reales
* proyectos de portafolio con criterio técnico

---

## 📝 Nota

Este proyecto es **open source** y fue construido con fines educativos y de portafolio.
Se prioriza **claridad, decisiones conscientes y evolución incremental**, por sobre la acumulación de funcionalidades.

