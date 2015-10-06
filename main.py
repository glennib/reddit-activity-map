import config
from SubredditInformation import *
from UserInformation import *
import praw
from pprint import pprint

r = praw.Reddit(user_agent=config.user_agent)

# subreddit_info = SubredditInformation(r, config.subreddit, config.submission_count)
#
# pprint(subreddit_info.hours)

# for hour in range(24):
#     print(str(hour).zfill(2) + ':00-' + str(hour).zfill(2) + ':59 - ' + str(subreddit_info.hours[hour]).rjust(
#         3) + ' posts')
#
# print('\nTotal of ' + str(subreddit_info.number_of_submissions) + ' submissions found.')
user_name = 'hmlangs'

user_info = UserInformation(r, user_name)

comments = user_info.get_subreddits_of_comments()
submissions = user_info.get_subreddits_of_submissions()

comment_list = []
submission_list = []

for key in comments:
    comment_list.append((key, comments[key]))

for key in submissions:
    submission_list.append((key, submissions[key]))

comment_list.sort(key=lambda node: node[1], reverse=True)
submission_list.sort(key=lambda node: node[1], reverse=True)

print("\n User info for: {}\n".format(user_name))
print("Comments:\n")
pprint(comment_list)

print("\nSubmissions:\n")
pprint(submission_list)

print("\nCountries:\n")

country_list = []
countries = user_info.get_countries_mentioned()

for key in countries:
    country_list.append((key, countries[key]))

country_list.sort(key=lambda t: t[1], reverse=True)

pprint(country_list)
