import config
from SubredditInformation import *
from UserInformation import *
import praw
from pprint import pprint

r = praw.Reddit(user_agent=config.user_agent)

# subreddit_info = SubredditInformation(r, config.subreddit, config.submission_count)
#
# pprint(subreddit_info.hours)

user_name = 'gitarg'

user_info = UserInformation(r, user_name)

comments = user_info.comments
submissions = user_info.submissions

l = []
l2 = []

for key in comments:
    l.append((key, comments[key]))

for key in submissions:
    l2.append((key, submissions[key]))

l.sort(key=lambda node: node[1], reverse=True)
l2.sort(key=lambda node: node[1], reverse=True)

print("\n User info for: {}\n".format(user_name))
print("Comments:\n")
pprint(l)

print("\nSubmissions:\n")
pprint(l2)

print("\nCountries:\n")
pprint(user_info.countries)