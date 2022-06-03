import praw
from typing import List

def agg_links(reddit:praw.Reddit,subreddit:str,num:int,freq:str):
    links = []
    try:
        sreddit = reddit.subreddit(subreddit)
    except Exception as e:
        print(e)
        print('error, subreddit DNF')
    submissions = sreddit.top(time_filter=freq,limit=num*2)
    for submission in submissions:
        split_by_period = submission.url.split('.')
        start = split_by_period[0]
        if start[-1] == 'v':
            links.append(submission.url)
    return links[:num]