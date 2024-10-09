# control/buttons.py

import rainbowhat as rh

def read_button_a():
    """Return True if button A is pressed, otherwise False."""
    return rh.touch.A.pressed

def read_button_b():
    """Return True if button B is pressed, otherwise False."""
    return rh.touch.B.pressed

def read_button_c():
    """Return True if button C is pressed, otherwise False."""
    return rh.touch.C.pressed
