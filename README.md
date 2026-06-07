# TITAN AI

Titan AI is the open-source autonomous desktop AI agent designed to act as a digital employee inside your computer.

## Workspace structure

- `backend/` - FastAPI service, Gemini client, memory & task modules
- `frontend/` - Next.js + React + Tailwind UI shell
- `desktop/` - Desktop integration scaffold for Electron or Tauri
- `docs/` - Architecture and schema documentation
- `scripts/` - Developer scripts and local startup helpers

## Getting started

1. Install backend dependencies:
   - `cd backend && pip install -r requirements.txt`
2. Install frontend dependencies:
   - `cd frontend && npm install`
3. Run backend:
   - `cd backend && uvicorn app.main:app --reload --host 0.0.0.0 --port 8000`
4. Run frontend:
   - `cd frontend && npm run dev`

## Windows development

- Run both services on Windows with `start-dev.bat`
- Or use `scripts\start-dev.bat` from PowerShell or CMD

## Notes

- `backend/` now contains layered modules for Brain, Planning, Memory, Tool, Desktop Control, Browser Control, Voice, Vision, Learning, Security, Plugin, and Automation.
- `start-dev.bat` launches the backend and frontend in separate Windows terminals.

## Mission

Build a modular, secure, and extensible autonomous desktop AI with:

- Brain, planning, memory, tool, desktop, browser, voice, vision, learning, security, plugin, and automation layers
- Gemini API integration with fallback, retry, streaming, and prompt optimization
- Multi-agent orchestration, task planning, and memory-enabled execution
- Desktop UI, browser automation, and OS-level control

## Next steps

- Add Gemini API authentication and streaming support
- Implement desktop automation with Playwright, OpenCV, and OS control modules
- Expand frontend to support chat, task dashboard, voice controls, and memory manager
- Add plugin framework and security approval workflows
