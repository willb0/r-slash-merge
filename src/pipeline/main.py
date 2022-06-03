from fastapi import FastAPI
from fastapi.responses import StreamingResponse,FileResponse
from models import LinkRequest
import requests
import datetime
import io

app = FastAPI()


@app.get('/')
def home():
    return {'home': 'page'}


@app.post('/compilation')
def build_compilation(lr: LinkRequest):
    print(lr.dict())
    links = requests.post('http://links_api:80/videos', json=lr.dict()).json()['links']
    requests.post('http://video_api:81/download',
                 json={'subreddit': lr.subreddit,
                       'date': str(datetime.datetime.today()),
                       'links': links})
    res = requests.get('http://video_api:81/merge',stream=True)
    return FileResponse('/shared/stitched-video.mp4', headers={'Content-Disposition': 'attachment; filename=merge.mp4'})
