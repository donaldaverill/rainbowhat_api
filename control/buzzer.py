# control/buzzer.py

import rainbowhat as rh

def play_note(note, duration=0.5):
    """Play a MIDI note on the buzzer."""
    rh.buzzer.midi_note(note, duration)

def stop_buzzer():
    """Stop any ongoing buzzer sound."""
    rh.buzzer.stop()
