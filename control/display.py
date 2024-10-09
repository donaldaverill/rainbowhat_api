# control/display.py

import rainbowhat as rh

def display_text(text):
    """Display text on the alphanumeric display."""
    if len(text) > 4:
        raise ValueError("Text length exceeds display limit.")
    rh.display.print_str(text)
    rh.display.show()

def clear_display():
    """Clear the display."""
    rh.display.clear()
    rh.display.show()
