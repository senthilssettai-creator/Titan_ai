from fastapi import APIRouter
from pydantic import BaseModel
from app.agents.coordinator import CoordinatorAgent

router = APIRouter()
coordinator = CoordinatorAgent()


class AgentRequest(BaseModel):
    goal: str
    context: dict | None = None


@router.post("/plan")
def plan_goal(request: AgentRequest):
    return coordinator.orchestrate(request.goal, request.context)


@router.post("/execute")
def execute_goal(request: AgentRequest):
    plan = coordinator.orchestrate(request.goal, request.context)
    return {
        "status": "execution_started",
        "plan": plan,
    }
