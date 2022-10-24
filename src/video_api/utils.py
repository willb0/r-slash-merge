import redvid
from typing import List
from ffprobe import FFProbe
import shutil
import os 
import subprocess
import glob
import re
from models import LinkMerge
import requests
from xml.etree import ElementTree

VRLINK = "https://v.redd.it/{}"

def download_video(url:str) -> None:
    dl = redvid.Downloader(max_q=True)
    dl.url = url
    dl.path = '/usr/src/api/videos'
    dl.download()
    return
def download_videos():
    pass

def merge_videos(path:str,output:str):
    for filename in glob.glob(f'{path}+videos/*.mp4'):
        ff = FFProbe(filename)
        print(str(ff.streams))
        resolution = (re.search(r'\d+x\d+',str(ff.streams)).group(0))
        a,b = resolution.split('x')
        if int(a) < int(b):
            print('phone video smh')
            os.remove(filename)
    subprocess.call(['sh','./merg.sh'])
    shutil.move(path + 'stitched-video.mp4',output + 'stitched-video.mp4')
    return 
def cleanup(paths):
    for path in paths:
        for filename in glob.glob(path + '*.mp4'):
            os.remove(filename)


    














