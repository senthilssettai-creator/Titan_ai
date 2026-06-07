@echo off
SETLOCAL ENABLEEXTENSIONS
cd /d %~dp0

echo Installing Titan AI dependencies...

if not exist backend\.venv (
    python -m venv backend\.venv
    if errorlevel 1 (
        echo Failed to create backend virtual environment.
        exit /b 1
    )
) else (
    echo Backend virtual environment already exists.
)

echo Activating backend virtual environment...
call backend\.venv\Scripts\activate.bat
if errorlevel 1 (
    echo Failed to activate backend virtual environment.
    exit /b 1
)

echo Upgrading pip...
python -m pip install --upgrade pip
if errorlevel 1 (
    echo Failed to upgrade pip.
    exit /b 1
)

echo Installing backend requirements...
pip install -r backend\requirements.txt
if errorlevel 1 (
    echo Failed to install backend requirements.
    exit /b 1
)

echo Installing frontend dependencies...
cd frontend
npm install
if errorlevel 1 (
    echo Failed to install frontend dependencies.
    exit /b 1
)

echo Installation complete.
exit /b 0
