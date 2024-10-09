from pydantic import BaseModel, conint
from typing import List

class LedColor(BaseModel):
    red: conint(ge=0, le=255) = 255
    green: conint(ge=0, le=255) = 0
    blue: conint(ge=0, le=255) = 0

class LedRequest(BaseModel):
    index: conint(ge=0, le=6)  # Restrict the index to between 0 and 6
    color: LedColor

class AllLedsRequest(BaseModel):
    colors: List[LedColor]

class DisplayTextRequest(BaseModel):
    text: str

class BuzzerPlayRequest(BaseModel):
    note: int
    duration: float = 0.5

