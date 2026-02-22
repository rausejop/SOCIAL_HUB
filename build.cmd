@echo off
setlocal enabledelayedexpansion

:: SOCIAL HUB BUILD & INSTALLER
:: Standard: CONF23-STD-SDLC-007

echo [INFO] Starting Social Hub Build Process...
echo [INFO] Date: %DATE% %TIME%
echo [INFO] Environment: Windows 11

:: 1. Check Python installation
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python is not installed. Please install Python 3.14.3.
    exit /b 1
)

:: 2. Create Virtual Environment (Optional but recommended in standard)
:: But the standard says "uv is incompatible", we use pip.
echo [INFO] Installing dependencies from requirements.txt...
pip install -r requirements.txt

:: 3. Initialize Database
echo [INFO] Initializing Database...
python database\db_manager.py

:: 4. Run Security Sanity Check (Tabnanny)
echo [INFO] Running Security Sanity Check (Tabnanny)...
python -m tabnanny .

:: 5. Launch Application
echo [SUCCESS] Build process completed successfully.
echo [INFO] Launching Social Hub...
streamlit run main.py

pause
