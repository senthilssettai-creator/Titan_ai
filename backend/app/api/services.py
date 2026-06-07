import json
from typing import Any
from sqlmodel import SQLModel, Session, create_engine, select
from app.core.config import settings
from app.api.models import MemoryEntry, MemoryEntryCreate

engine = create_engine(settings.database_url, connect_args={"check_same_thread": False})
SQLModel.metadata.create_all(engine)


class MemoryService:
    def save_memory(self, entry: MemoryEntryCreate) -> dict[str, Any]:
        with Session(engine) as session:
            memory_entry = MemoryEntry(
                category=entry.category,
                content=entry.content,
                metadata=json.dumps(entry.metadata),
            )
            session.add(memory_entry)
            session.commit()
            session.refresh(memory_entry)
            return {
                "id": memory_entry.id,
                "category": memory_entry.category,
                "content": memory_entry.content,
                "metadata": entry.metadata,
                "created_at": memory_entry.created_at.isoformat(),
            }

    def list_memories(self) -> list[dict[str, Any]]:
        with Session(engine) as session:
            statement = select(MemoryEntry).order_by(MemoryEntry.created_at.desc())
            results = session.exec(statement).all()
            return [
                {
                    "id": item.id,
                    "category": item.category,
                    "content": item.content,
                    "metadata": json.loads(item.metadata),
                    "created_at": item.created_at.isoformat(),
                }
                for item in results
            ]


class PlannerService:
    def decompose(self, objective: str, details: str | None = None) -> dict[str, str]:
        return {
            "objective": objective,
            "details": details or "",
            "tasks": [
                "1. Analyze user objective and dependencies",
                "2. Create a safe execution plan",
                "3. Allocate tasks to specialized agents",
                "4. Monitor progress and recover from errors",
            ],
        }
