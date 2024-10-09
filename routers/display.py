# routers/display.py

from fastapi import APIRouter, HTTPException
from control import display
from models import DisplayTextRequest

router = APIRouter(
    prefix="/display",
    tags=["display"],
)

@router.post("/text")
def display_text_endpoint(request: DisplayTextRequest):
    if len(request.text) > 4:
        raise HTTPException(status_code=400, detail="Text length exceeds display limit.")
    try:
        display.display_text(request.text)
        return {"status": f"Displayed text '{request.text}'"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/clear")
def display_clear():
    try:
        display.clear_display()
        return {"status": "Display cleared"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
