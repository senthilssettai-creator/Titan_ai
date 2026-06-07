from enum import Enum
from typing import Any


def require_permission(level: str, context: dict[str, Any]) -> bool:
    current = context.get("permission_level", "low")
    levels = ["low", "medium", "high", "critical"]
    return levels.index(current) >= levels.index(level)


class PermissionLevel(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"
