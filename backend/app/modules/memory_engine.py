import json
from datetime import datetime
from typing import Any
from sqlmodel import SQLModel, Field, Session, create_engine, select
from app.core.config import settings
from app.core.vector_store import VectorStore


class MemoryRecord(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    category: str
    type: str
    content: str
    metadata: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    last_accessed: datetime = Field(default_factory=datetime.utcnow)


engine = create_engine(settings.database_url, connect_args={"check_same_thread": False})
SQLModel.metadata.create_all(engine)


class MemoryEngine:
    def __init__(self):
        self.store = VectorStore()

    def save_memory(self, category: str, memory_type: str, content: str, metadata: dict[str, Any]) -> dict[str, Any]:
        with Session(engine) as session:
            record = MemoryRecord(
                category=category,
                type=memory_type,
                content=content,
                metadata=json.dumps(metadata),
            )
            session.add(record)
            session.commit()
            session.refresh(record)
            self.store.save_embedding(record.id, self._embed(content), metadata, category)
            return {
                "id": record.id,
                "category": category,
                "type": memory_type,
                "content": content,
                "metadata": metadata,
                "created_at": record.created_at.isoformat(),
            }

    def search_memory(self, query: str, top_k: int = 5) -> list[dict[str, Any]]:
        query_vector = self._embed(query)
        results = self.store.search(query_vector, top_k=top_k)
        return [
            {"memory_id": item.memory_id, "score": item.score, "metadata": item.metadata}
            for item in results
        ]

    def _embed(self, text: str) -> list[float]:
        return [float((ord(c) % 10) / 10.0) for c in text[:256]]
