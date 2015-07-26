import config
from SubredditInformation import *
import praw
from pprint import pprint

r = praw.Reddit(user_agent=config.user_agent)

subreddit_info = SubredditInformation(r, config.subreddit, config.submission_count)

pprint(subreddit_info.hours)
