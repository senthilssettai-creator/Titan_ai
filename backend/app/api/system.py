from fastapi import APIRouter
from pydantic import BaseModel
from app.modules.desktop_control import DesktopControl
from app.modules.browser_control import BrowserControl
from app.modules.vision import VisionEngine

router = APIRouter()

control = DesktopControl()
vision = VisionEngine()


class ClickRequest(BaseModel):
    x: int
    y: int


class ScreenshotRequest(BaseModel):
    filename: str


@router.post("/desktop/click")
def click(request: ClickRequest):
    return control.click(request.x, request.y)


@router.post("/desktop/screenshot")
def screenshot(request: ScreenshotRequest):
    return vision.describe_screenshot(request.filename)
