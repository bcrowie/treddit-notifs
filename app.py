import praw
from secret import reddit
import time
import requests

print(reddit.user.me())
reddit.read_only = True

post = ""

while(True):
    for submission in reddit.subreddit("3dprintmything").new(limit=1):
        print(submission.title)
        if(post == ""):
            post = submission.title
        elif (post != "" and post != submission.title):
            post = submission.title
            x = requests.post("http://10.10.100.254:8123/api/webhook/3dprintmything", {"message": "New Post on 3dprintmything"})
            print(x)
    time.sleep(90)
