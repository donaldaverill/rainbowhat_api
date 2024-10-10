# app.py

from fastapi import FastAPI
from routers import leds, display, buzzer, sensors, buttons, songs

app = FastAPI(
    title="Rainbow HAT API",
    description="API to control Rainbow HAT features on Raspberry Pi",
    version="1.0.0",
)

# Include routers
app.include_router(leds.router)
app.include_router(display.router)
app.include_router(buzzer.router)
app.include_router(sensors.router)
app.include_router(buttons.router)
app.include_router(songs.router)

# Optionally, add a root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Rainbow HAT API!"}
