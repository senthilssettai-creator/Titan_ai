@echo off
SETLOCAL ENABLEEXTENSIONS
cd /d %~dp0

echo Launching Titan AI backend and frontend...

start "Titan AI Backend" cmd /k "cd /d %~dp0\backend && call .venv\Scripts\activate.bat && python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000"
start "Titan AI Frontend" cmd /k "cd /d %~dp0\frontend && npm run dev"

echo Titan AI services started in new windows.
exit /b 0
