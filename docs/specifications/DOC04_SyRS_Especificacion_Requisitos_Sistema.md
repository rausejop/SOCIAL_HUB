# Especificación de Requisitos del Sistema (SyRS) - SocialHub

## 1. Introducción
### 1.1 Propósito
Definir los requisitos técnicos para la plataforma SocialHub.

### 1.2 Funciones del Sistema
- Almacenamiento persistente en SQLite.
- Integración con API externa (JSONPlaceholder/DummyJSON).
- Sistema de caché para modo offline.
- Monitoreo de recursos (Memoria < 70% de 8GB).

## 2. Requisitos Funcionales
- **RF-01**: Publicación de posts de hasta 280 caracteres.
- **RF-02**: Feed infinito basado en Room/SQLite.
- **RF-03**: Interacciones (Likes, Comentarios).
- **RF-04**: Gestión de borradores.

## 3. Requisitos de Seguridad
- Implementación de Fail-Safe wrappers.
- Protección contra SQL Injection y XSS.
- Validación de tipos estricta (PEP 484).
