from typing import Optional
from pydantic import BaseModel, Field 
from enum import Enum

class Frequency(str, Enum):
    all = 'all'
    day = 'day'
    hour = 'hour'
    month = 'month'
    week = 'week'

class Orientation(str,Enum):
    landscape = '16:9'
    portrait = '4:3'
    ios = '3:4'
    sq = '1:1'
    Any = 'Any'

class LinkRequest(BaseModel):
    subreddit: str
    freq: Frequency
    num: int = Field(gt=0,le=100)
    orientation: Orientation
    lo: int = 0
    hi: int = 30

    class Config:
        use_enum_values = True

