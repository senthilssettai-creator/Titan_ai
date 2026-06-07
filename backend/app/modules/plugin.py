from typing import Any


class PluginManager:
    def __init__(self):
        self.plugins: dict[str, Any] = {}

    def register_plugin(self, name: str, handler: Any) -> None:
        self.plugins[name] = handler

    def available(self) -> list[str]:
        return list(self.plugins.keys())

    def run(self, name: str, payload: dict[str, Any]) -> dict[str, Any]:
        plugin = self.plugins.get(name)
        if not plugin:
            return {"error": "plugin_not_found"}
        return plugin(payload)
