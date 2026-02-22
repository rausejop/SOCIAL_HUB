# DOC06 - Architectural Design Records (ADR) - SOCIAL HUB

## ADR-001: Selección de Stack Tecnológico
**Estado**: Aceptado
**Contexto**: Necesidad de desarrollar una red social minimalista en un entorno Windows 11 con restricciones de memoria (8GB disponibles) y cumplimiento de seguridad CONF23.
**Decisión**: Usar Streamlit como framework de frontend/backend debido a su rapidez de desarrollo y compatibilidad con Python 3.14.3. SQLite será el motor de persistencia por su ligereza y nula necesidad de configuración externa.
**Consecuencias**: Simplificación del despliegue, pero limitaciones en la personalización extrema de CSS comparado con frameworks tradicionales (se mitigará con inyección de estilos personalizados).
**Trazabilidad de Cumplimiento**: Mitigación de OWASP A01:2025 mediante control de acceso centralizado.

## ADR-002: Gestión de Estado y Datos
**Estado**: Aceptado
**Contexto**: El usuario requiere interacción en tiempo real y persistencia local.
**Decisión**: Utilizar `st.connection` para SQLite y `st.session_state` para la gestión de estados temporales de la interfaz. Implementar una capa de servicios (`src/core/services.py`) para desligar la UI de la lógica de negocio.
**Consecuencias**: Código más limpio y fácil de testear.
**Trazabilidad de Cumplimiento**: Cumplimiento del estándar ISO 27001 sobre integridad de datos.
