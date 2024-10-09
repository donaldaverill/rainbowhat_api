# control/sensors.py

import rainbowhat as rh

def read_temperature():
    """Read temperature from the sensor."""
    return rh.weather.temperature()

def read_pressure():
    """Read pressure from the sensor."""
    return rh.weather.pressure()
