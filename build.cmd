@echo off
SETLOCAL EnableDelayedExpansion
TITLE "SocialHub Build & Deploy System"

echo [1/4] Verificando Entorno...
python --version | findstr "3.14.3" >nul
if %errorlevel% neq 0 (
    echo [ADVERTENCIA] Se recomienda Python 3.14.3 segun estandar. Procediendo bajo riesgo.
)

echo [2/4] Instalando Dependencias...
python -m pip install -r requirements.txt --quiet

echo [3/4] Ejecutando Verificaciones de Seguridad (SDLC)...
echo -> Verificando Indentacion (tabnanny)...
python -m tabnanny src
if %errorlevel% neq 0 (
    echo [ERROR] Fallo en verificacion de indentacion.
    exit /b 1
)

echo -> Ejecutando Analisis AST...
python src\verify_security.py
if %errorlevel% neq 0 (
    echo [ERROR] Fallo en analisis de seguridad AST.
    exit /b 1
)

echo [4/4] Preparando Lanzamiento...
echo Proyecto SocialHub construido con exito.
echo Para iniciar la plataforma ejecute: streamlit run src\app.py

ENDLOCAL
pause
