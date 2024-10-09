# routers/buttons.py

from fastapi import APIRouter, HTTPException
from control import buttons

router = APIRouter(
    prefix="/buttons",
    tags=["buttons"],
)

@router.get("/a")
def get_button_a_state():
    try:
        state = buttons.read_button_a()
        return {"button": "A", "pressed": state}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/b")
def get_button_b_state():
    try:
        state = buttons.read_button_b()
        return {"button": "B", "pressed": state}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/c")
def get_button_c_state():
    try:
        state = buttons.read_button_c()
        return {"button": "C", "pressed": state}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
