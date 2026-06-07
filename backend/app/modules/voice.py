from typing import Any


class VoiceEngine:
    def __init__(self):
        self.enabled = False

    def speak(self, text: str) -> dict[str, Any]:
        return {"status": "queued", "text": text}

    def listen(self) -> dict[str, Any]:
        return {"status": "listening", "transcript": ""}

    def wake_word(self) -> str:
        return "Hey Titan"
