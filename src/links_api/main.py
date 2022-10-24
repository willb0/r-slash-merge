from fastapi import FastAPI
from praw import Reddit
from link_grabber import agg_links
from models import LinkRequest

CLIENT_ID = "Iy-hbvXMSqeMJVZWVfrpUg"
CLIENT_SECRET = "QsjGezAYk5Z_ck6juh_uPjMVmTnPHQ"
reddit = Reddit(
    client_id = CLIENT_ID,
    client_secret = CLIENT_SECRET,
    user_agent = "Finding v.reddit links to download"
)

app = FastAPI()

@app.get("/")
def root():
    return {"Home page":"Hit /videos/subreddit"}

@app.get('/videos/')
def missing_subreddit():
    return {'Need a subreddit to check links for':'videos/subreddit'}

@app.post('/videos/')
def get_links(req:LinkRequest):
    links = agg_links(reddit, req)
    return {
        "subreddit":req.subreddit,
        'links':links,
        'freq':req.freq,
        'num':req.num
        }
