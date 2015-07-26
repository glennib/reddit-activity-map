import config
from SubredditInformation import *
import praw

r = praw.Reddit(user_agent=config.user_agent)

subreddit_info = SubredditInformation(r, config.subreddit, config.submission_count)

print(subreddit_info.hours)
