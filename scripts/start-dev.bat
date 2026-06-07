@echo off
SETLOCAL ENABLEDELAYEDEXPANSION
cd /d %~dp0\..

echo Launching Titan AI backend and frontend...
start "Titan AI Backend" cmd /k "cd backend && python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000"
start "Titan AI Frontend" cmd /k "cd frontend && npm run dev"
echo Done.
