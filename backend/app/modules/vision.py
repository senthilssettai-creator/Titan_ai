from typing import Any

try:
    import cv2
except ImportError:
    cv2 = None


class VisionEngine:
    def describe_screenshot(self, path: str) -> dict[str, Any]:
        if not cv2:
            return {"error": "opencv-python not installed"}
        image = cv2.imread(path)
        if image is None:
            return {"error": "file not found"}
        height, width = image.shape[:2]
        return {"status": "analyzed", "width": width, "height": height}

    def detect_ui_elements(self, path: str) -> dict[str, Any]:
        return {"status": "placeholder", "elements": []}
