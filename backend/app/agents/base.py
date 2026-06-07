from abc import ABC, abstractmethod
from typing import Any


class Agent(ABC):
    name: str

    @abstractmethod
    def plan(self, objective: str, context: dict[str, Any] | None = None) -> dict[str, Any]:
        pass

    @abstractmethod
    def execute(self, task: dict[str, Any]) -> dict[str, Any]:
        pass
