#!/usr/bin/env bash
set -e

cd "$(dirname "$0")/.."

echo "Starting backend..."
cd backend
poetry run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000 &
BACKEND_PID=$!

echo "Starting frontend..."
cd ../frontend
npm run dev

kill $BACKEND_PID
