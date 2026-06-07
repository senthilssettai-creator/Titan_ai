@echo off
SETLOCAL ENABLEEXTENSIONS
cd /d %~dp0

echo Stopping Titan AI backend and frontend windows...

taskkill /F /FI "WINDOWTITLE eq Titan AI Backend" >nul 2>&1
taskkill /F /FI "WINDOWTITLE eq Titan AI Frontend" >nul 2>&1
echo Stopping Uvicorn, Node, and Python processes if still running...
taskkill /F /IM uvicorn.exe >nul 2>&1
taskkill /F /IM node.exe >nul 2>&1
taskkill /F /IM python.exe >nul 2>&1
echo Stop command complete.
exit /b 0
