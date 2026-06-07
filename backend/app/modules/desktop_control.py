import platform
from typing import Any

try:
    import pyautogui
except ImportError:
    pyautogui = None


class DesktopControl:
    def __init__(self):
        self.platform = platform.system().lower()

    def click(self, x: int, y: int) -> dict[str, Any]:
        if pyautogui:
            pyautogui.click(x, y)
            return {"status": "clicked", "x": x, "y": y}
        return {"error": "pyautogui not installed"}

    def type_text(self, text: str) -> dict[str, Any]:
        if pyautogui:
            pyautogui.write(text)
            return {"status": "typed", "text": text}
        return {"error": "pyautogui not installed"}

    def press_hotkey(self, keys: list[str]) -> dict[str, Any]:
        if pyautogui:
            pyautogui.hotkey(*keys)
            return {"status": "hotkey_pressed", "keys": keys}
        return {"error": "pyautogui not installed"}

    def screenshot(self, filename: str) -> dict[str, Any]:
        if pyautogui:
            screenshot = pyautogui.screenshot()
            screenshot.save(filename)
            return {"status": "screenshot_saved", "file": filename}
        return {"error": "pyautogui not installed"}
