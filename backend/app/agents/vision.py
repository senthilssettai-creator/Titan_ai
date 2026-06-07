from typing import Any
from app.agents.base import Agent
from app.modules.vision import VisionEngine


class VisionAgent(Agent):
    name = "Vision Agent"

    def __init__(self):
        self.engine = VisionEngine()

    def plan(self, objective: str, context: dict[str, Any] | None = None) -> dict[str, Any]:
        return {"plan": ["Capture screen", "Analyze UI elements", "Read text"]}

    def execute(self, task: dict[str, Any]) -> dict[str, Any]:
        if task.get("type") == "screen_analysis":
            return self.engine.describe_screenshot(task.get("path", "screenshot.png"))
        return {"status": "unsupported", "task": task}
