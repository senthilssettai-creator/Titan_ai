from fastapi import APIRouter
from pydantic import BaseModel
from app.api.services import PlannerService

router = APIRouter()
planner = PlannerService()


class PlannerRequest(BaseModel):
    objective: str
    details: str | None = None


@router.post("/decompose")
async def decompose_task(request: PlannerRequest):
    return planner.decompose(request.objective, request.details)
