from typing import Any
from app.agents.base import Agent
from app.modules.memory_engine import MemoryEngine


class MemoryAgent(Agent):
    name = "Memory Agent"

    def __init__(self):
        self.engine = MemoryEngine()

    def plan(self, objective: str, context: dict[str, Any] | None = None) -> dict[str, Any]:
        return {"plan": ["Store user preferences", "Search relevant memories"]}

    def execute(self, task: dict[str, Any]) -> dict[str, Any]:
        if task.get("action") == "save_memory":
            return self.engine.save_memory(
                category=task.get("category", "general"),
                memory_type=task.get("type", "conversation"),
                content=task.get("content", ""),
                metadata=task.get("metadata", {}),
            )
        return {"status": "unsupported", "task": task}
