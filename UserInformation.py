import praw


class UserInformation:
    def __init__(self, r, user_name):
        self._r = r
        self.user_name = user_name
        self.user = r.get_redditor(self.user_name)

        self.comments = self._get_comments()
        self.submissions = self._get_submissions()


    def _get_comments(self):
        comments = {}
        c = self.user.get_comments(limit=None)

        for comment in c:
            subreddit_name = comment.subreddit.display_name
            comments[subreddit_name] = comments.get(subreddit_name, 0) + 1

        return comments

    def _get_submissions(self):
        submissions = {}

        s = self.user.get_submitted(limit=None)

        for submission in s:
            subreddit_name = submission.subreddit.display_name
            submissions[subreddit_name] = submissions.get(subreddit_name, 0) + 1

        return submissions
