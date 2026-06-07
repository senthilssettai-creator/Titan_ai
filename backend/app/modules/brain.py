from typing import Any
from app.core.ai_client import GeminiClient
from app.core.cache import get_cached_response, cache_response
from app.modules.planning import PlanningEngine


class Brain:
    def __init__(self):
        self.client = GeminiClient()
        self.planner = PlanningEngine()

    async def think(self, goal: str, context: str | None = None) -> dict[str, Any]:
        prompt = (
            "You are Titan AI Brain. Create a safe, autonomous execution plan for the user goal.\n"
            f"Goal: {goal}\n"
            f"Context: {context or 'default'}\n"
            "Return a structured plan and next actions."
        )
        cached = get_cached_response(prompt)
        if cached:
            return {"source": "cache", "plan": cached}

        response = await self.client.generate_with_fallback(prompt, max_tokens=800)
        cache_response(prompt, response)
        return {"source": "gemini", "plan": response}
