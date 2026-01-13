# Changelog

## [0.1.0] - Módulo público

### Añadido

- Registro de usuario con nombre de tienda
- Generación automática de slug
- Confirmación de cuenta
- Recuperación y reseteo de contraseña
- Página NotFound pública
- Extre

### Cambiado

- Validaciones de caracteres en registro
- Manejo correcto de errores (400 vs 404)

### Seguridad

- Sanitización de errores backend
- Protección de rutas públicas inexistentes

---

## [0.2.0] - Módulo público v1 [Finalizado]

### Añadido

- Inicio de Sesión (JWT)
- Estructura base de módulo privado (panel protegido)

### Seguridad

- Protección de rutas privadas mediante JWT

---

## [0.3.0] - Módulo privado v1 [Personal]

### Añadido

- Creación de personal
- Visualización de personal mediante tabla interactiva
- Editar Personal

### Cambiado

- Ahora el módulo publico retralimenta al usuario con mensajes mas claros
- Se corrigieron los nombre de algunas vistas en el módulo publico. Ahora los nombres son acordes al funcionamiento de la vista

### Seguridad

- Se agregaron validaciones de seguridad en las vistas publicas
