import json
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any

import numpy as np
from sqlmodel import SQLModel, Field, Session, create_engine, select
from app.core.config import settings

VECTOR_DB_PATH = Path(settings.database_url.replace("sqlite:///", ""))
engine = create_engine(settings.database_url, connect_args={"check_same_thread": False})


class EmbeddingEntry(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    memory_id: int
    vector: str
    metadata: str
    category: str


SQLModel.metadata.create_all(engine)


@dataclass
class VectorSearchResult:
    memory_id: int
    score: float
    metadata: Any


class VectorStore:
    def __init__(self):
        self.engine = engine

    def save_embedding(self, memory_id: int, vector: list[float], metadata: dict[str, Any], category: str):
        with Session(self.engine) as session:
            entry = EmbeddingEntry(
                memory_id=memory_id,
                vector=json.dumps(vector),
                metadata=json.dumps(metadata),
                category=category,
            )
            session.add(entry)
            session.commit()
            session.refresh(entry)
            return entry

    def search(self, query_vector: list[float], top_k: int = 5) -> list[VectorSearchResult]:
        with Session(self.engine) as session:
            statement = select(EmbeddingEntry)
            results = session.exec(statement).all()
            candidates: list[VectorSearchResult] = []
            q = np.array(query_vector)
            for row in results:
                vector = np.array(json.loads(row.vector), dtype=float)
                if vector.size != q.size:
                    continue
                score = float(np.dot(q, vector) / (np.linalg.norm(q) * np.linalg.norm(vector) + 1e-8))
                candidates.append(VectorSearchResult(memory_id=row.memory_id, score=score, metadata=json.loads(row.metadata)))
            candidates.sort(key=lambda item: item.score, reverse=True)
            return candidates[:top_k]
