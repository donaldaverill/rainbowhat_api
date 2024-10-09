# routers/sensors.py

from fastapi import APIRouter, HTTPException
from control import sensors

router = APIRouter(
    prefix="/sensors",
    tags=["sensors"],
)

@router.get("/temperature")
def get_temperature():
    try:
        temperature = sensors.read_temperature()
        return {"temperature": temperature}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/pressure")
def get_pressure():
    try:
        pressure = sensors.read_pressure()
        return {"pressure": pressure}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
