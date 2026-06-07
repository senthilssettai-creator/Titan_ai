from datetime import datetime
from typing import Any


class AutomationEngine:
    def __init__(self):
        self.checkpoints: list[dict[str, Any]] = []
        self.pending_tasks: list[dict[str, Any]] = []

    def queue_task(self, task: dict[str, Any]) -> dict[str, Any]:
        task_record = {**task, "queued_at": datetime.utcnow().isoformat(), "status": "queued"}
        self.pending_tasks.append(task_record)
        return task_record

    def checkpoint(self, state: dict[str, Any]) -> dict[str, Any]:
        record = {"timestamp": datetime.utcnow().isoformat(), "state": state}
        self.checkpoints.append(record)
        return record

    def rollback(self) -> dict[str, Any]:
        if not self.checkpoints:
            return {"status": "no_checkpoints"}
        last = self.checkpoints.pop()
        return {"status": "rolled_back", "checkpoint": last}
