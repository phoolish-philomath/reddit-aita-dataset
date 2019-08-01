import praw
from psaw import PushshiftAPI
from datetime import datetime, timedelta
import arrow
import time
import re
import pandas as pd
import numpy as np
from praw_reddit import clean_automod_record

ultimate_start_time = arrow.now()

def is_seeking_judgement(submission):
    return all([
        submission.author is not 'AITAMod',
        submission.distinguished is None,
        not submission.stickied
        ])

def get_submission_body(submission):
    if '[deleted]' in submission.selftext:
        setattr(submission, 'removed', 0)
        setattr(submission, 'deleted', 1)
        automod_saved_post = None
        for comment in submission.comments:
            if re.match(re.escape('^^^^AUTOMOD'), getattr(comment, 'body', '')) is not None:
                automod_saved_post = comment
        if automod_saved_post is not None:
            original_post = clean_automod_record(automod_saved_post.body)
        else:
            original_post = ''
        return original_post
    elif '[removed]' in submission.selftext:
        setattr(submission, 'deleted', 0)
        setattr(submission, 'removed', 1)
        return ''
    else:
        setattr(submission, 'deleted', 0)
        setattr(submission, 'removed', 0)
        return submission.selftext

subreddit = 'AmITheAsshole'

r = praw.Reddit(
    client_id='1tlYQ_1vjJ1W6w',
    client_secret='Aar-QVdnIWrqjbrYlcmbGqjqLYU',
    password='itAi_xhas3',
    user_agent=f'script to collect r/{subreddit} data',
    username='phoolish_philomath'
)
api = PushshiftAPI(r)

fields = ['id', 'created_ts', 'author', 'title', 'body', 'flair', 'was_deleted', 'was_removed']

start_date = datetime(2019, 6, 3)
end_date = datetime(2019, 7, 1)
total_submission_count = 0

while start_date < end_date:
    print(f'Getting data for {start_date.strftime("%d %B")}')
    query_start = int(start_date.timestamp())
    query_end = int((start_date + timedelta(days=1)).timestamp()) 
    processing_start_time = arrow.now()

    rows = []
    submission_count = 0
    for submission in api.search_submissions(
        after=query_start,
        before=query_end,
        subreddit=subreddit,
        ):
        if is_seeking_judgement(submission):
            submission_body = get_submission_body(submission)
            created_ts = arrow.get(submission.created_utc).format('YYYY-MM-DD HH:mm:ss')
            row = (submission.id, created_ts, submission.author, submission.title, submission_body, submission.link_flair_text, submission.deleted, submission.removed)
            rows.append(row)
        
        submission_count +=1
        if submission_count % 500 == 0:
            print(f"Found {submission_count} posts so far.")

    processing_end_time = arrow.now()
    print(f"Retrieved {submission_count} posts in total. Time taken was {(processing_end_time - processing_start_time).seconds} seconds.")

    df = pd.DataFrame(rows, columns=fields)
    print(f"Ended up with {len(df)} rows of data.")
    print(f"About to save data for {start_date.strftime('%d %B')} to file...")
    df.to_csv(f'aita_posts_{start_date.strftime("%d_%B").lower()}.csv', index=False, header=True, sep='\t')
    total_submission_count += len(df)
    start_date = start_date + timedelta(days=1)

ultimate_end_time = arrow.now()
print(f"Saved {total_submission_count} rows of data. Total time taken was {(ultimate_end_time - ultimate_start_time).seconds / 60} minutes.")
print("Done!")
