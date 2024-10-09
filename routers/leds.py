# routers/leds.py

import logging
from fastapi import APIRouter, HTTPException
from control import leds
from models import LedColor, LedRequest, AllLedsRequest

router = APIRouter(
    prefix="/leds",
    tags=["leds"],
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@router.post("/on")
def leds_on(color: LedColor):
    try:
        leds.set_leds(color.red, color.green, color.blue)
        logger.info(f"Setting LEDs to color ({color.red}, {color.green}, {color.blue})")

        return {"status": "LEDs turned on", "color": {"red": color.red, "green": color.green, "blue": color.blue}}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/off")
def leds_off():
    try:
        leds.clear_leds()
        logger.info(f"LEDs turned off")

        return {"status": "LEDs turned off"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/set")
def set_single_led(request: LedRequest):
    try:
        # Extract index and color from the request model
        index = request.index
        color = request.color
        leds.set_led(index, color.red, color.green, color.blue)
        logger.info(f"Setting LED {index} to color ({color.red}, {color.green}, {color.blue})")

        return {"status": f"LED {index} set to color", "color": {"red": color.red, "green": color.green, "blue": color.blue}}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/set_all")
def set_all_leds(request: AllLedsRequest):
    try:
        leds.set_all_leds(request.colors)
        logger.info(f"Setting All LED values")

        return {"status": "All LEDs set to specified colors"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
