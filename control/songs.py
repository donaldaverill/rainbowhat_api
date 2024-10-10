# control/songs.py

import rainbowhat as rh
import time

# Dictionary for musical notes to frequencies (in Hz)
NOTE_FREQUENCIES = {
    'C4': 261.63, 'D4': 293.66, 'E4': 329.63, 'F4': 349.23,
    'G4': 392.00, 'A4': 440.00, 'B4': 493.88, 'C5': 523.25,
    'REST': 0  # Special value for a rest (no sound)
}

def play_song_with_lights(song):
    """
    Play a song using the buzzer and flash the lights in sync.

    Parameters:
    - song: A list of tuples, where each tuple contains a note (str),
            duration (float in seconds), and color (tuple of RGB values).
            Example: [('C4', 0.5, (255, 0, 0)), ('D4', 0.5, (0, 255, 0))]
    """
    for note, duration, color in song:
        frequency = NOTE_FREQUENCIES.get(note, 0)

        if frequency > 0:
            # Play the note on the buzzer
            rh.buzzer.note(frequency)
        else:
            # Handle the rest (no sound)
            rh.buzzer.stop

        # Set the LED colors
        rh.rainbow.set_all(color[0], color[1], color[2])
        rh.rainbow.show()

        # Keep the note and lights on for the specified duration
        time.sleep(duration)

        # Turn off the buzzer and clear the lights
        rh.buzzer.stop()
        rh.rainbow.clear()
        rh.rainbow.show()

        # Short pause between notes
        time.sleep(0.1)

# Dictionary for musical notes to frequencies (in Hz)
NOTE_FREQUENCIES = {
    'C4': 261.63, 'D4': 293.66, 'E4': 329.63, 'F4': 349.23,
    'G4': 392.00, 'A4': 440.00, 'B4': 493.88, 'C5': 523.25,
    'REST': 0  # Special value for a rest (no sound)
}

three_blind_mice = [
    ('E4', 0.5, (255, 0, 0)),   # "Three"
    ('D4', 0.5, (0, 255, 0)),   # "Blind"
    ('C4', 0.5, (0, 0, 255)),   # "Mice"
    ('E4', 0.5, (255, 255, 0)), # "Three"
    ('D4', 0.5, (0, 255, 255)), # "Blind"
    ('C4', 0.5, (255, 0, 255)), # "Mice"
    ('G4', 0.75, (255, 255, 255)), # "Run"
    ('REST', 0.25, (0, 0, 0)),  # Pause
    ('G4', 0.75, (128, 128, 128)), # "Run"
    ('REST', 0.25, (0, 0, 0)),  # Pause
    ('G4', 0.75, (255, 165, 0)), # "Run"
    ('REST', 0.25, (0, 0, 0)),  # Pause
    ('E4', 0.5, (255, 0, 0)),   # "Three"
    ('D4', 0.5, (0, 255, 0)),   # "Blind"
    ('C4', 0.5, (0, 0, 255)),   # "Mice"
]
