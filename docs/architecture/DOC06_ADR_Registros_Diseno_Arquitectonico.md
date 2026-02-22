# Registros de Diseño Arquitectónico (ADR) - SocialHub

## ADR-001: Selección del Stack Tecnológico
**Estado**: Aceptado
**Contexto**: Necesidad de una plataforma de microblogging segura en Windows 11 con 8GB de RAM disponible.
**Decisión**: Uso de Python 3.14.3, Streamlit para frontend y SQLite para persistencia.
**Consecuencias**: Agilidad en el desarrollo pero riesgo de inestabilidad por versión de lenguaje.
**Trazabilidad**: Cumple con CONF23-STD-SDLC-006 Sección 2.

## ADR-002: Lógica de Validación de Seguridad Nativa
**Estado**: Aceptado
**Contexto**: Evitar dependencias de terceros para análisis estático básico.
**Decisión**: Implementación de validaciones AST y `tabnanny` integradas en el pipeline local.
**Trazabilidad**: Mitigación de OWASP A03 (Inyección) y A06 (Vulnerabilidades de Configuración).

## ADR-003: Persistencia Local y Caché
**Estado**: Aceptado
**Contexto**: Soporte para red social con modo offline.
**Decisión**: Implementación de base de datos local SQLite replicando el comportamiento de Room.
**Trazabilidad**: Disponibilidad de datos y resiliencia.
