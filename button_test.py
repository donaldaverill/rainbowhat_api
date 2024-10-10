import rainbowhat
import signal

@rainbowhat.touch.A.press()
def touch_a(channel):
    print("Touch A pressed")

signal.pause()
