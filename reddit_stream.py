import praw
import arrow

r = praw.Reddit(
    client_id='1tlYQ_1vjJ1W6w',
    client_secret='Aar-QVdnIWrqjbrYlcmbGqjqLYU',
    password='itAi_xhas3',
    user_agent='script to collect r/AmITheAsshole data',
    username='phoolish_philomath'
)

aita = r.subreddit('amitheasshole')

for comment in aita.stream.comments():
    print('Found a comment!')
    #print(submission.title, submission.subreddit.name, arrow.get(submission.created_utc))
    print(arrow.get(comment.created_utc), comment.body)
