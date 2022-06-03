from tabnanny import check
from tkinter import E
import praw
from typing import List
import requests
from xml.etree import ElementTree
from models import LinkRequest
import re


orientations = {}
def agg_links(reddit:praw.Reddit,req:LinkRequest):
    print(req.orientation)
    links = []
    try:
        sreddit = reddit.subreddit(req.subreddit)
    except Exception as e:
        print(e)
        print('error, subreddit DNF')
    submissions = sreddit.top(time_filter=req.freq,limit=req.num*20)
    ct = 0
    length = req.length if req.length != 0 else None
    for submission in submissions:
        split_by_period = submission.url.split('.')
        start = split_by_period[0]
        or_check = check_video_orientation(submission.url,req.orientation)
        len_check = check_video_length(submission.url,length) if length else True
        if start[-1] == 'v' and len_check and or_check:
            ct += 1
            links.append(submission.url)
            if ct == req.num:
                return links
    print(f"Couldn't find enough videos for you, only found {ct}")
    print(f'orientations: {orientations}')
    assert ct != 0, 'Found no videos'
    return links

def check_video_orientation(url:str,orientation: str):
    res = requests.get(url + '/DASHPlaylist.mpd')
    try:
        tree = ElementTree.fromstring(res.content)
        attributes = tree[0]
        #print('finding orientation')
        for child in attributes:
            if 'par' in child.attrib:
                child_orien = child.attrib['par']
                orientations[child_orien] = orientations.get(child_orien,0) + 1
                (a,b) = tuple(map(int,orientation.split(':')))
                numerical = a/b
                if child_orien == orientation or float(child_orien) == numerical:
                    print(orientation,child.attrib['par'])
                    return True
        return False
    except Exception as e:
        print(e)
        return False

def check_video_length(url:str,length:int):
    res = requests.get(url + '/DASHPlaylist.mpd')
    try:
        tree = ElementTree.fromstring(res.content)
        attributes = tree[0].attrib
        #strings llook like this 'PT12.000S'
        if 'duration' in attributes:
            #print(attributes['duration'])
            dur = attributes['duration'][2:-1]
            #print(dur)
            try:
                float(dur)
            except ValueError as e:
                dur = dur[2:]
            if float(dur) <= length:
                #print(dur)
                return True
        return False
    except Exception as e:
        #print(e)
        return False
    
    
