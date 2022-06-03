from datetime import datetime
from pydantic import BaseModel
from typing import List

class LinkMerge(BaseModel):
    subreddit: str
    date: str
    links: List[str]
