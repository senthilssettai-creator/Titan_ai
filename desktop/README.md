# Desktop Integration

This folder contains the desktop host integration for TITAN AI. The final product can be shipped with Electron or Tauri.

## Goals

- Launch the frontend UI
- Manage background backend process
- Expose OS automation APIs for desktop control
- Provide secure permission gating for sensitive actions

## Suggested implementation

- Use Tauri for cross-platform desktop shell with Rust + frontend
- Or use Electron with `main.js` as a lightweight launcher
- Communicate with the backend over HTTP or local IPC

## Current scaffold

This repository currently includes a frontend and backend starter architecture. The desktop integration layer is a placeholder for later native packaging and OS-level control.
