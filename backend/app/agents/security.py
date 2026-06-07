from typing import Any
from app.agents.base import Agent
from app.modules.security import SecurityManager


class SecurityAgent(Agent):
    name = "Security Agent"

    def __init__(self):
        self.manager = SecurityManager()

    def plan(self, objective: str, context: dict[str, Any] | None = None) -> dict[str, Any]:
        return {"plan": ["Evaluate permission requirements", "Log actions for audit"]}

    def execute(self, task: dict[str, Any]) -> dict[str, Any]:
        return self.manager.log_action(task.get("action", "unknown"), task.get("source", "titan"), task.get("details", {}), level=task.get("level", "low"))
