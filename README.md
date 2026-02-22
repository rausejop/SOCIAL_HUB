# 🛡️ SocialHub — Red Social de Microblogging Segura

<p align="center">
  <img src="https://img.shields.io/badge/Versi%C3%B3n-v0.1.0--alpha-blueviolet?style=for-the-badge&logo=semver" alt="Versión">
  <img src="https://img.shields.io/badge/Python-3.14.3-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Framework-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit">
  <img src="https://img.shields.io/badge/Seguridad-SDLC--CONF23-success?style=for-the-badge&logo=shoppay&logoColor=white" alt="Seguridad">
  <br>
  <img src="https://img.shields.io/badge/Licencia-Apache--2.0-D22128?style=flat-square&logo=apache" alt="Licencia">
  <img src="https://img.shields.io/badge/Mantenido-S%C3%AD-008000?style=flat-square" alt="Mantenido">
  <img src="https://img.shields.io/badge/OS-Windows--11-0078D4?style=flat-square&logo=windows-11&logoColor=white" alt="Windows 11">
  <img src="https://img.shields.io/badge/OWASP-Top--10--2025-orange?style=flat-square" alt="OWASP">
</p>

---

## 📝 Resumen del Proyecto

**SocialHub** es una plataforma de microblogging de vanguardia diseñada bajo la metodología de desarrollo de software seguro **CONF23-STD-SDLC-006**. Su misión es proporcionar un espacio de comunicación ágil, privado y altamente resiliente, eliminando la dependencia de algoritmos opacos y priorizando la integridad de los datos de los usuarios.

### ✨ Características Estrella
- 📝 **Micro-pensamientos**: Exprésate con libertad en posts de hasta 280 caracteres.
- ⚡ **Tiempo Real**: Interacción instantánea con likes, comentarios y actualizaciones de feed.
- 🔦 **Trend Analytics**: Algoritmo de tendencias local basado en la actividad comunitaria.
- 💾 **Persistencia Inteligente**: Motor SQLite optimizado con caché para navegación sin conexión.
- 🧩 **Draft System**: Nunca pierdas una idea; guarda borradores y retómalos cuando quieras.
- 🕵️ **Seguridad Nativa**: Auditoría AST integrada que bloquea ejecuciones de código peligrosas.

---

## 🏗️ Guía de Construcción y Despliegue

### ⚙️ Requisitos de Entorno
Para garantizar el funcionamiento óptimo y la conformidad con los estándares de seguridad:
- 🐍 **Lenguaje**: Python 3.14.3 (Mandatorio para cumplimiento estricto).
- 💻 **Sistema**: Windows 11 [Versión 10.0.26200.7840].
- 🧠 **Hardware**: Mínimo 8GB de RAM disponibles (Monitoreo de umbral al 70%).

### 🛠️ Proceso Automatizado
El proyecto utiliza un sistema de construcción de "Zero Touch":
```powershell
# 1. Clona el repositorio
git clone https://github.com/tu-usuario/socialhub.git

# 2. Ejecuta el motor de construcción
.\build.cmd
```
> **Nota de Seguridad:** El script `build.cmd` detendrá el proceso si detecta indentaciones ambiguas (`tabnanny`) o patrones de código inseguros (`ast-scan`).

---

## 🚀 Instrucciones de Ejecución

Una vez que el sistema de construcción confirme el éxito del despliegue:

```powershell
# Lanzar la plataforma web
streamlit run src/app.py
```

🌐 **Acceso Local:** `http://localhost:8501`

---

## ⚙️ Manual de Operación y Gobierno

### 📲 Operativa Diaria
| Acción | Ubicación | Descripción |
| :--- | :--- | :--- |
| **Publicar** | Dashboard Inicio | Escribe y lanza tu post al timeline global. |
| **Interactuar** | Feed | Reacciona con ❤️ y comenta hilos de conversación. |
| **Buscar** | Barra de Búsqueda | Encuentra usuarios o contenido por palabras clave. |
| **Administrar** | Perfil | Gestiona tu biografía, avatar y revisa métricas. |

### 🛡️ Cumplimiento de Seguridad (DevSecOps)
- **A01:2025 – Control de Acceso**: Lógica de validación de identidad en capas.
- **A03:2025 – Inyección**: Mitigada mediante validación AST del árbol sintáctico.
- **Logs Estructurados**: Auditoría en tiempo real en `src/logs/` vía JSON estructurado.

---

## 📂 Organización del Ecosistema

```text
SOCIAL_HUB/
├── 📂 src/                 # Lógica core, apps y scripts de seguridad
│   └── 📄 verify_security.py # Auditor ast-based mandatorio
├── 📂 docs/                # Gobernanza y documentación técnica
│   ├── 📂 specifications/  # Documentos ISO/IEC/IEEE 29148
│   ├── 📂 scrum/           # Artefactos y seguimiento ágil
│   └── 📂 architecture/    # Decisiones de Diseño (ADR)
├── 📂 tests/               # Suite de pruebas unitarias (Pytest)
├── 📄 build.cmd            # Orquestador de construcción segura
├── 📄 requirements.txt     # Manifiesto de dependencias
└── 📄 README.md            # Documentación principal
```

---

## 🤝 Contribución y Roadmap

Actualmente nos encontramos en el **Sprint 1 (Fundación)**. Estamos abiertos a contribuciones que sigan el estándar de tipado estricto (PEP 484) y docstrings en formato Google.

---

## 📄 Licencia y Créditos
- **Licencia**: [Apache License 2.0](LICENSE)
- **Autoría**: Senior DevSecOps Architect @ **CONFIANZA23**
- **Soporte**: Antigravity AI Implementation

---
<p align="right">(<a href="#top">Volver al inicio</a>)</p>
