from typing import Any


class ToolManager:
    def __init__(self):
        self.tools: dict[str, Any] = {}

    def register(self, name: str, tool: Any) -> None:
        self.tools[name] = tool

    def get(self, name: str) -> Any | None:
        return self.tools.get(name)

    def list_tools(self) -> list[str]:
        return list(self.tools.keys())
