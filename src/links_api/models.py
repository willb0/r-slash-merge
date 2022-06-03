from pydantic import BaseModel, Field 
from enum import Enum

class Frequency(str, Enum):
    all = 'all'
    day = 'day'
    hour = 'hour'
    month = 'month'
    week = 'week'

class LinkRequest(BaseModel):
    subreddit: str
    freq: Frequency
    num: int = Field(gt=0,le=100)

