from sys import stderr
from turtle import down
from fastapi import FastAPI, File
from fastapi.responses import FileResponse
from models import LinkMerge
from utils import download_video,merge_videos

app = FastAPI()

@app.get('/')
def home():
    return {'Homepage of':"Video API"}

@app.post('/download')
def download_videos(lm:LinkMerge):
    for link in lm.links:
        download_video(link)
    return

@app.get('/merge')
def agg_videos():
    merge_videos('/usr/src/api/','/shared/')
    return FileResponse('/shared/stitched-video.mp4',media_type='video/mp4',headers={'Content-Disposition': 'attachment; filename=merge.mp4'})

    


