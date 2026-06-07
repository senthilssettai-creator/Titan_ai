from fastapi import APIRouter
from app.api import agents, memory, planner, system, plugins

api_router = APIRouter()
api_router.include_router(agents.router, prefix="/agents", tags=["agents"])
api_router.include_router(memory.router, prefix="/memory", tags=["memory"])
api_router.include_router(planner.router, prefix="/planner", tags=["planner"])
api_router.include_router(system.router, prefix="/system", tags=["system"])
api_router.include_router(plugins.router, prefix="/plugins", tags=["plugins"])
