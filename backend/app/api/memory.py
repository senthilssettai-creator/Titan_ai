from fastapi import APIRouter
from pydantic import BaseModel
from app.api.models import MemoryEntryCreate, MemoryEntry
from app.api.services import MemoryService

router = APIRouter()
service = MemoryService()


class MemoryCreateRequest(BaseModel):
    category: str
    type: str = "conversation"
    content: str
    metadata: dict | None = None


@router.post("/entries")
async def create_memory(request: MemoryCreateRequest):
    entry = MemoryEntryCreate(
        category=request.category,
        content=request.content,
        metadata=request.metadata or {},
    )
    result = service.save_memory(entry)
    return {"memory": result}


@router.get("/entries")
def list_memory():
    return {"entries": service.list_memories()}


class MemorySearchRequest(BaseModel):
    query: str


@router.post("/search")
def search_memory(request: MemorySearchRequest):
    return {"results": []}
