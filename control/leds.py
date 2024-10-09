# control/leds.py

import rainbowhat as rh
from typing import List
from models import LedColor

def set_leds(red=255, green=0, blue=0):
    """Set all LEDs to the specified color."""
    rh.rainbow.set_all(red, green, blue)
    rh.rainbow.show()

def clear_leds():
    """Turn off all LEDs."""
    rh.rainbow.clear()
    rh.rainbow.show()

def set_led(index, red=255, green=0, blue=0):
    """Set a specific LED to the specified color."""
    rh.rainbow.set_pixel(index, red, green, blue)
    rh.rainbow.show()

def set_all_leds(colors: List[LedColor]):
    """Set all LEDs to the specified list of colors."""
    if len(colors) != 7:  # Assuming there are 7 LEDs on the Rainbow HAT
        raise ValueError("Exactly 7 colors are required, one for each LED.")

    # Set each LED to the corresponding color
    for index, color in enumerate(colors):
        rh.rainbow.set_pixel(index, color.red, color.green, color.blue)

    # Update the LED strip
    rh.rainbow.show()
