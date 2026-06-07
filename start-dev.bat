@echo off
SETLOCAL ENABLEDELAYEDEXPANSION
cd /d %~dp0

echo Starting backend in a new window...
start "Titan AI Backend" cmd /k "cd backend && python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000"

echo Starting frontend in a new window...
start "Titan AI Frontend" cmd /k "cd frontend && npm run dev"
necho Titan AI development environment launched.
