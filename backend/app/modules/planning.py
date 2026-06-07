from typing import Any


class PlanningEngine:
    def decompose_goal(self, goal: str, context: str | None = None) -> dict[str, Any]:
        return {
            "goal": goal,
            "context": context or "none",
            "steps": [
                "Analyze user intent and environment",
                "Choose the appropriate agent stack",
                "Build a multi-step plan with dependencies",
                "Validate the plan against safety and permissions",
                "Execute tasks incrementally with monitoring",
            ],
        }

    def summarize_plan(self, tasks: list[str]) -> str:
        return " -> ".join(tasks)
