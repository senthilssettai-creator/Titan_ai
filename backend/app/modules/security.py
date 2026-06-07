import json
from datetime import datetime
from typing import Any
from sqlmodel import SQLModel, Field, Session, create_engine, select
from app.core.config import settings


class AuditLog(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    action: str
    source: str
    details: str
    level: str
    created_at: datetime = Field(default_factory=datetime.utcnow)


engine = create_engine(settings.database_url, connect_args={"check_same_thread": False})
SQLModel.metadata.create_all(engine)


class SecurityManager:
    def __init__(self):
        pass

    def log_action(self, action: str, source: str, details: dict[str, Any], level: str = "low") -> dict[str, Any]:
        with Session(engine) as session:
            record = AuditLog(action=action, source=source, details=json.dumps(details), level=level)
            session.add(record)
            session.commit()
            session.refresh(record)
            return {"id": record.id, "action": action, "source": source, "level": level}

    def list_audit(self, limit: int = 25) -> list[dict[str, Any]]:
        with Session(engine) as session:
            results = session.exec(select(AuditLog).order_by(AuditLog.created_at.desc()).limit(limit)).all()
            return [{"id": item.id, "action": item.action, "source": item.source, "details": json.loads(item.details), "level": item.level, "created_at": item.created_at.isoformat()} for item in results]
