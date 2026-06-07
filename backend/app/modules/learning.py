from typing import Any


class LearningEngine:
    def __init__(self):
        self.history: list[dict[str, Any]] = []

    def record_outcome(self, task: str, outcome: str, metadata: dict[str, Any] | None = None) -> None:
        self.history.append({"task": task, "outcome": outcome, "metadata": metadata or {}})

    def summarize_feedback(self) -> dict[str, Any]:
        return {"entries": len(self.history), "recent": self.history[-5:]}
