import praw
import country_synonyms

STRIPPED_CHARACTERS = '!"#¤%&/()=?+\\-_.,;:\'<>|§¦¡@£$¥{[]}±´`'

class UserInformation:
    def __init__(self, r, user_name):
        self._r = r
        self.user_name = user_name
        self.user = r.get_redditor(self.user_name)

        self._comment_objects = None
        self._submission_objects = None

        self.comments = self._get_comments()
        self.submissions = self._get_submissions()

        self.countries = self._get_countries_mentioned()



    def _get_comments(self):
        comments = {}
        self._comment_objects = self.user.get_comments(limit=None)

        for comment in self._comment_objects:
            subreddit_name = comment.subreddit.display_name
            comments[subreddit_name] = comments.get(subreddit_name, 0) + 1

        return comments

    def _get_submissions(self):
        submissions = {}

        self._submission_objects = self.user.get_submitted(limit=None)

        for submission in self._submission_objects:
            subreddit_name = submission.subreddit.display_name
            submissions[subreddit_name] = submissions.get(subreddit_name, 0) + 1

        return submissions

    def _get_countries_mentioned(self):
        text = ''

        for comment in self._comment_objects:
            text += comment.body + ' '

        for submission in self._submission_objects:
            text += submission.title + ' '
            if submission.is_self:
                text += submission.selftext + ' '

        countries = {}

        for word in text.split():
            for key in country_synonyms.countries:
                if word.strip(STRIPPED_CHARACTERS).lower() in country_synonyms.countries[key]:
                    countries[key] = countries.get(key, 0) + 1

        return countries
