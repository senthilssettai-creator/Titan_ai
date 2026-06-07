from typing import Any

try:
    from playwright.async_api import async_playwright
except ImportError:
    async_playwright = None


class BrowserControl:
    def __init__(self):
        self.sessions: dict[str, Any] = {}

    async def open_browser(self, browser_name: str = "chromium", headless: bool = False) -> dict[str, Any]:
        if not async_playwright:
            return {"error": "playwright not installed"}

        playwright = await async_playwright().start()
        browser = await getattr(playwright, browser_name).launch(headless=headless)
        context = await browser.new_context()
        page = await context.new_page()
        session_id = f"{browser_name}-{len(self.sessions)+1}"
        self.sessions[session_id] = {"browser": browser, "context": context, "page": page}
        return {"session_id": session_id, "browser": browser_name}

    async def navigate(self, session_id: str, url: str) -> dict[str, Any]:
        session = self.sessions.get(session_id)
        if not session:
            return {"error": "session not found"}
        await session["page"].goto(url)
        return {"status": "navigated", "url": url}
