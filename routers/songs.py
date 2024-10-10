# routers/songs.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Tuple
from control.songs import play_song_with_lights, three_blind_mice
from models import SongNote

router = APIRouter(
    prefix="/songs",
    tags=["songs"]
)

@router.post("/play")
def play_song(song: List[SongNote]):
    try:
        # Convert the Pydantic models to a list of tuples
        song_data = [(item.note, item.duration, item.color) for item in song]
        play_song_with_lights(song_data)
        return {"status": "Song played successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/play_three_blind_mice")
def play_three_blind_mice():
    """
    Play the song 'Three Blind Mice' using the buzzer and lights.
    """
    try:
        play_song_with_lights(three_blind_mice)
        return {"status": "Three Blind Mice played successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
