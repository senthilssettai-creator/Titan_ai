from typing import Any
from app.agents.planner import PlannerAgent
from app.agents.browser import BrowserAgent
from app.agents.desktop import DesktopAgent
from app.agents.vision import VisionAgent
from app.agents.memory import MemoryAgent
from app.agents.optimization import OptimizationAgent
from app.agents.security import SecurityAgent


class CoordinatorAgent:
    def __init__(self):
        self.planner = PlannerAgent()
        self.browser = BrowserAgent()
        self.desktop = DesktopAgent()
        self.vision = VisionAgent()
        self.memory = MemoryAgent()
        self.optimization = OptimizationAgent()
        self.security = SecurityAgent()

    def orchestrate(self, objective: str, context: dict[str, Any] | None = None) -> dict[str, Any]:
        plan = self.planner.plan(objective, context)
        return {
            "objective": objective,
            "plan": plan,
            "agents": [
                self.planner.name,
                self.browser.name,
                self.desktop.name,
                self.vision.name,
                self.memory.name,
                self.optimization.name,
                self.security.name,
            ],
        }
