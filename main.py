import config
from SubredditInformation import *
import praw
from pprint import pprint

r = praw.Reddit(user_agent=config.user_agent)

subreddit_info = SubredditInformation(r, config.subreddit, config.submission_count)

for hour in range(24):
    print(str(hour).zfill(2) + ':00-' + str(hour).zfill(2) + ':59 - ' + str(subreddit_info.hours[hour]).rjust(
        3) + ' posts')

print('\nTotal of ' + str(subreddit_info.number_of_submissions) + ' submissions found.')
