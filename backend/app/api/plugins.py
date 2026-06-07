from fastapi import APIRouter
from pydantic import BaseModel
from app.modules.plugin import PluginManager

router = APIRouter()
manager = PluginManager()


class PluginInvokeRequest(BaseModel):
    plugin_name: str
    payload: dict | None = None


@router.get("/list")
def list_plugins():
    return {"plugins": manager.available()}


@router.post("/invoke")
def invoke_plugin(request: PluginInvokeRequest):
    return manager.run(request.plugin_name, request.payload or {})
