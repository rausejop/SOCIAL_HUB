# DOC05 - Software Requirements Specification (SRS) - SOCIAL HUB

## 1. Introducción
### 1.1 Propósito
Definir las especificaciones técnicas del software Social Hub basado en Streamlit.

## 3. Requerimientos
### 3.1 Funciones
- **Publicación**: Módulo para redactar y publicar posts.
- **Perfil**: Visualización de estadísticas de usuario.
- **Caché**: Sistema de caché para modo offline o carga rápida.

### 3.5 Requerimientos de Base de Datos Lógica
- Tabla `Users`: id, username, bio, avatar, created_at.
- Tabla `Posts`: id, user_id, content, created_at.
- Tabla `Comments`: id, post_id, user_id, content.
- Tabla `Likes`: post_id, user_id.

### 3.6 Restricciones de Diseño
- Lenguaje: Python 3.14.3.
- Framework: Streamlit.
- UI: Estética Dark Premium, Glassmorphism.

### 3.7 Atributos del Sistema de Software
- **Seguridad**: Validación AST obligatoria antes de ejecución.
- **Mantenibilidad**: Código modular siguiendo principios SOLID.
