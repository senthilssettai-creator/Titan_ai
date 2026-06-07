import asyncio
import logging
from typing import Any
import httpx
from app.core.config import settings

logger = logging.getLogger(__name__)


class GeminiClient:
    def __init__(self, api_key: str | None = None):
        self.api_key = api_key or settings.gemini_api_key
        self.base_url = "https://api.generativeai.google/v1beta2"
        self.model = settings.gemini_model
        self.fallback_model = settings.gemini_fallback_model

    async def _request(self, endpoint: str, payload: dict) -> dict:
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }
        async with httpx.AsyncClient(timeout=settings.request_timeout_seconds) as client:
            response = await client.post(f"{self.base_url}/{endpoint}", json=payload, headers=headers)
            response.raise_for_status()
            return response.json()

    async def generate(self, prompt: str, max_tokens: int = 1024, stream: bool = False) -> dict:
        payload = {
            "model": self.model,
            "prompt": prompt,
            "maxTokens": max_tokens,
            "temperature": 0.3,
            "stream": stream,
        }
        for attempt in range(1, settings.max_retry_attempts + 1):
            try:
                logger.info("Gemini request attempt %s", attempt)
                return await self._request("responses:generate", payload)
            except Exception as exc:
                logger.warning("Gemini request failed on attempt %s: %s", attempt, exc)
                if attempt >= settings.max_retry_attempts:
                    raise
                await asyncio.sleep(min(2 ** attempt, 10))

    async def generate_with_fallback(self, prompt: str, **kwargs: Any) -> dict:
        try:
            return await self.generate(prompt, **kwargs)
        except Exception:
            logger.info("Falling back to secondary Gemini model %s", self.fallback_model)
            self.model = self.fallback_model
            return await self.generate(prompt, **kwargs)

    async def embed(self, text: str) -> list[float]:
        if not text:
            return []
        return [float((ord(c) % 10) / 10.0) for c in text[:512]]

    def estimate_tokens(self, text: str) -> int:
        return max(1, len(text) // 4)
