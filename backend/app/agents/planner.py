from typing import Any
from app.agents.base import Agent


class PlannerAgent(Agent):
    name = "Planner Agent"

    def plan(self, objective: str, context: dict[str, Any] | None = None) -> dict[str, Any]:
        return {
            "objective": objective,
            "steps": [
                "Analyze the intent",
                "Select required capabilities",
                "Generate a structured plan",
                "Validate permissions",
            ],
            "context": context or {},
        }

    def execute(self, task: dict[str, Any]) -> dict[str, Any]:
        return {"status": "planned", "task": task}
