import praw
import datetime


class SubredditInformation:
    def __init__(self, r, subreddit_name, submission_count):
        assert type(r) is praw.Reddit
        self._r = r
        self.subreddit = r.get_subreddit(subreddit_name)
        self._gather_statistics(submission_count)

    def _gather_statistics(self, submission_count):
        submissions = []
        for submission in self.subreddit.get_new(limit=submission_count):
            submissions.append(submission)

        timestamps_utc = []
        for submission in submissions:
            timestamps_utc.append(submission.created_utc)

        self.hours = []
        for hour in range(24):
            self.hours.append(0)

        for timestamp in timestamps_utc:
            converted_time = datetime.datetime.fromtimestamp(timestamp)
            hour = converted_time.hour
            self.hours[hour] += 1
