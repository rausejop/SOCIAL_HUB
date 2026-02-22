# DOC04 - System Requirements Specification (SyRS) - SOCIAL HUB

## 1. Introducción
### 1.1 Propósito del Sistema
Sistema de backend y frontend integrados para la gestión de micro-publicaciones.

### 1.3 Perfil del Sistema
#### 1.3.1 Contexto del Sistema
El sistema interactúa con el usuario mediante Streamlit y almacena datos en SQLite.

#### 1.3.2 Funciones del Sistema
- CRUD de publicaciones.
- Gestión de relaciones (Seguidores/Seguidos).
- Sistema de likes y comentarios.

## 3. Requerimientos del Sistema
### 3.1 Requerimientos Funcionales
- **RF01**: El sistema permitirá crear posts con un máximo de 280 caracteres.
- **RF02**: El sistema mostrará un feed de noticias ordenado cronológicamente.
- **RF03**: Capacidad de dar/quitar like a una publicación.

### 3.3 Requerimientos de Rendimiento
- Carga de la página inicial en menos de 2 segundos.
- Soporte para 100 usuarios concurrentes en servidor local.

### 3.4 Requerimientos de Interfaz
- **3.4.1 Interfaz Externa**: Integración con API JSONPlaceholder para datos iniciales opcionales.
- **3.4.2 Interfaz Interna**: Conexión SQLite vía `st.connection`.

### 3.9 Requerimientos de Seguridad
- Sanitización de entradas para prevenir XSS.
- Protección contra inyección SQL mediante el uso de parámetros en consultas.
