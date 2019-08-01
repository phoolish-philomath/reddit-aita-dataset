import praw
import re

def clean_automod_record(comment_body):
    start = "^^^^AUTOMOD  ***The following is a copy of the above post. This comment is a record of the above post as it was originally written, in case the post is deleted or edited.***"
    end = '*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/AmItheAsshole) if you have any questions or concerns.*'
    start_pattern = re.compile(f"{re.escape(start)}\s*") 
    end_pattern = re.compile(f"\s*{re.escape(end)}\s*")
    start_cleaned = re.sub(start_pattern, '', comment_body)
    end_cleaned = re.sub(end_pattern, '', start_cleaned)
    return end_cleaned


r = praw.Reddit(
    client_id='1tlYQ_1vjJ1W6w',
    client_secret='Aar-QVdnIWrqjbrYlcmbGqjqLYU',
    password='itAi_xhas3',
    user_agent='script to collect r/AmITheAsshole data',
    username='phoolish_philomath'
)

aita = r.subreddit('amitheasshole')
"""
sub = praw.models.Submission(reddit=r, id='cclfpw')
print(sub.title)
print(sub.author)
# print(sub.selftext)
print(sub.link_flair_text)
print("distinguished: ", sub.distinguished)
print("stickied: ", sub.stickied)
"""
"""
comments = sub.comments
original_post = ''
automod_record = None

for comment in comments:
    if comment.author.name == 'AutoModerator':
        if '^^^^AUTOMOD' in comment.body:
            # print(comment.id, comment.author, comment.body)
            automod_record = comment

if automod_record is not None:
    cleaned_post = clean_automod_record(automod_record.body)
    print(f'Comment ID: {automod_record.id}, Comment Author: {automod_record.author}')
    print()
    print('Original automod record:')
    print(automod_record.body)
    print()
    print('Cleaned automod record:')
    print(cleaned_post)
"""
