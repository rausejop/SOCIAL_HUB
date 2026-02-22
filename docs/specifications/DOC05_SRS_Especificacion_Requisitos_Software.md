# Especificación de Requisitos de Software (SRS) - SocialHub

## 1. Introducción
### 1.1 Ámbito del producto
SocialHub es una aplicación web basada en Streamlit que interactúa con una base de datos SQLite y APIs REST externas.

## 2. Descripción General
### 2.1 Funciones del software
- CRUD de posts.
- Lógica de seguidores (Follow/Unfollow).
- Sistema de notificaciones.
- Historial de búsquedas.

## 3. Requisitos Específicos
### 3.1 Interfaces
- **Interfaz de Usuario**: Minimalista, modo oscuro militar premium.
- **Interfaz de Base de Datos**: SQLite gestionado por SQLAlchemy o SQL directo con validación AST.
- **Interfaz de API**: Retrofit (para componentes móviles o simuladores Python equivalentes).

### 3.2 Atributos del Sistema
- **Seguridad**: Cumplimiento OWASP 2025.
- **Portabilidad**: Ejecución en Windows 11 con Python 3.14.3.
