#https://github.com/pushshift/api

import requests
import json
import time
import datetime
from datetime import datetime, timedelta

#returns selected number of posts from sub from last 24 hrs
def getURL(sub, howmany):
    after = datetime.now() - timedelta(days=1)
    after = time.mktime(after.timetuple())
    after = int(after)
    url = 'https://api.pushshift.io/reddit/search/submission/?&size='+str(howmany)+'&after='+str(after)+'&subreddit='+str(sub)
    #print(url)
    return url

#gets the title and text of a post
def getPost(sub):
    url = getURL(sub,3)
    r = requests.get(url)
    post = r.json()['data'][0]['title'] + " " + r.json()['data'][0]['selftext']
    return post
