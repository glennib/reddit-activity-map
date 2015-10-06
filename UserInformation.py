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
        self._countries = None

        self._subreddits_of_comments = None
        self._subreddits_of_submissions = None

    def get_comments(self):
        if self._comment_objects is None:
            comments = self.user.get_comments(limit=None)
            self._comment_objects = []

            for comment in comments:
                self._comment_objects.append(comment)

        return self._comment_objects

    def get_submissions(self):
        if self._submission_objects is None:
            submissions = self.user.get_submitted(limit=None)
            self._submission_objects = []

            for submission in submissions:
                self._submission_objects.append(submission)

        return self._submission_objects

    def get_subreddits_of_comments(self):

        def parser():
            comments = {}

            for comment in self.get_comments():
                subreddit_name = comment.subreddit.display_name
                comments[subreddit_name] = comments.get(subreddit_name, 0) + 1

            return comments

        if self._subreddits_of_comments is None:
            self._subreddits_of_comments = parser()

        return self._subreddits_of_comments

    def get_subreddits_of_submissions(self):

        def parser():
            submissions = {}

            for submission in self.get_submissions():
                subreddit_name = submission.subreddit.display_name
                submissions[subreddit_name] = submissions.get(subreddit_name, 0) + 1

            return submissions

        if self._subreddits_of_submissions is None:
            self._subreddits_of_submissions = parser()

        return self._subreddits_of_submissions

    def get_countries_mentioned(self):

        def parser():
            text = ''

            for comment in self.get_comments():
                text += comment.body + ' '

            for submission in self.get_submissions():
                text += submission.title + ' '
                if submission.is_self:
                    text += submission.selftext + ' '

            countries = {}

            for word in text.split():
                for key in country_synonyms.countries:
                    if word.strip(STRIPPED_CHARACTERS).lower() in country_synonyms.countries[key]:
                        countries[key] = countries.get(key, 0) + 1

            return countries

        if self._countries is None:
            self._countries = parser()

        return self._countries
