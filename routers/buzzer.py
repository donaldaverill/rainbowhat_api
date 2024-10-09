# routers/buzzer.py

from fastapi import APIRouter, HTTPException
from control import buzzer
from models import BuzzerPlayRequest

router = APIRouter(
    prefix="/buzzer",
    tags=["buzzer"],
)

@router.post("/play")
def buzzer_play(request: BuzzerPlayRequest):
    try:
        # Use the note and duration from the request model
        buzzer.play_note(request.note, request.duration)
        return {"status": f"Playing note {request.note} for {request.duration} seconds"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/stop")
def buzzer_stop():
    try:
        buzzer.stop_buzzer()
        return {"status": "Buzzer stopped"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
