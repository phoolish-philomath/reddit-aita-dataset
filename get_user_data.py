from psaw import PushshiftAPI
import arrow
import pandas as pd

file_name_template = 'aita_posts_{}_june.csv'
cols = ['id','created_ts', 'author', 'title', 'body', 'flair', 'was_deleted', 'was_removed']

api = PushshiftAPI()
data_lines = []

for day in range(5, 31):
    
    start_time = arrow.now()
    file_name = file_name_template.format(str(day) if day > 9 else f'0{day}')
    # file_name = 'aita_posts_small_june_sample.csv' 
    print(f'Processing {file_name}...')
    
    df = pd.read_csv(file_name, sep='\t', header=None, names=cols)   
    
    for index, row in df.iterrows():

            all_comments_count = 0
            aita_comments_count = 0
            all_submissions_count = 0
            aita_submissions_count = 0
            
            author = row['author']
            created_ts = row['created_ts']

            if author and created_ts and not pd.isnull(author) and not pd.isnull(created_ts):
                submission_date_epoch_timestamp = arrow.get(created_ts).timestamp
                user_activity_profile = api.redditor_subreddit_activity(author, before=submission_date_epoch_timestamp)
                
                if 'comment' in user_activity_profile:
                    all_comments_count = sum(user_activity_profile['comment'].values())
                    aita_comments_count = user_activity_profile['comment']['amitheasshole']
                
                if 'submission' in user_activity_profile:
                    all_submissions_count = sum(user_activity_profile['submission'].values())
                    aita_submissions_count = user_activity_profile['submission']['amitheasshole']
            
            df.loc[index, 'all_comments_count'] = int(all_comments_count)
            df.loc[index, 'all_submissions_count'] = int(all_submissions_count)
            df.loc[index, 'aita_comments_count'] = int(aita_comments_count)
            df.loc[index, 'aita_submissions_count'] = int(aita_submissions_count)
    
    df.to_csv('with_user_data_' + file_name, sep='\t', header=False, index=False)
    end_time = arrow.now()
    print(f'Done processing {file_name}. Time taken to process {len(df)} rows was {(end_time - start_time).seconds} seconds.')
