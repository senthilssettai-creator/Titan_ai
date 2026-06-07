import hashlib
import json
import sqlite3
import zlib
from pathlib import Path
from typing import Any

CACHE_DB = Path(__file__).resolve().parent.parent / "titan_cache.db"

CREATE_SQL = '''
CREATE TABLE IF NOT EXISTS prompt_cache (
    hash TEXT PRIMARY KEY,
    prompt TEXT,
    response TEXT,
    created_at TEXT
)
'''

conn = sqlite3.connect(CACHE_DB, check_same_thread=False)
conn.execute(CREATE_SQL)
conn.commit()


def compress_prompt(prompt: str) -> bytes:
    return zlib.compress(prompt.encode("utf-8"))


def decompress_prompt(data: bytes) -> str:
    return zlib.decompress(data).decode("utf-8")


def prompt_hash(prompt: str) -> str:
    return hashlib.sha256(prompt.encode("utf-8")).hexdigest()


def cache_response(prompt: str, response: Any) -> None:
    key = prompt_hash(prompt)
    conn.execute(
        "INSERT OR REPLACE INTO prompt_cache (hash, prompt, response, created_at) VALUES (?, ?, ?, datetime('now'))",
        (key, prompt, json.dumps(response, default=str)),
    )
    conn.commit()


def get_cached_response(prompt: str) -> Any | None:
    key = prompt_hash(prompt)
    row = conn.execute("SELECT response FROM prompt_cache WHERE hash = ?", (key,)).fetchone()
    if not row:
        return None
    return json.loads(row[0])
