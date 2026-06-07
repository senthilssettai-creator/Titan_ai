from typing import Any
from app.agents.base import Agent
from app.modules.desktop_control import DesktopControl


class DesktopAgent(Agent):
    name = "Desktop Agent"

    def __init__(self):
        self.control = DesktopControl()

    def plan(self, objective: str, context: dict[str, Any] | None = None) -> dict[str, Any]:
        return {"plan": ["Interact with desktop UI", "Manage windows and clipboard"]}

    def execute(self, task: dict[str, Any]) -> dict[str, Any]:
        action = task.get("action")
        if action == "click":
            return self.control.click(task.get("x", 0), task.get("y", 0))
        return {"status": "unsupported", "task": task}
