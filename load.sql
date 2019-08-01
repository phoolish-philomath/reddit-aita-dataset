CREATE TABLE posts (
 id TEXT PRIMARY KEY,
 created_ts TEXT,
 author TEXT,
 title TEXT,
 body TEXT,
 flair TEXT,
 was_deleted INTEGER,
 was_removed INTEGER,
 all_comments_count INTEGER,
 all_submissions_count INTEGER,
 aita_comments_count INTEGER,
 aita_submissions_count INTEGER
);
.mode csv
.headers off
.separator "\t"
.import ./with_user_data_aita_posts_01_june.csv posts
.import ./with_user_data_aita_posts_02_june.csv posts
.import ./with_user_data_aita_posts_03_june.csv posts
.import ./with_user_data_aita_posts_04_june.csv posts
.import ./with_user_data_aita_posts_05_june.csv posts
.import ./with_user_data_aita_posts_06_june.csv posts
.import ./with_user_data_aita_posts_07_june.csv posts
.import ./with_user_data_aita_posts_08_june.csv posts
.import ./with_user_data_aita_posts_09_june.csv posts
.import ./with_user_data_aita_posts_10_june.csv posts
.import ./with_user_data_aita_posts_11_june.csv posts
.import ./with_user_data_aita_posts_12_june.csv posts
.import ./with_user_data_aita_posts_13_june.csv posts
.import ./with_user_data_aita_posts_14_june.csv posts
.import ./with_user_data_aita_posts_15_june.csv posts
.import ./with_user_data_aita_posts_16_june.csv posts
.import ./with_user_data_aita_posts_17_june.csv posts
.import ./with_user_data_aita_posts_18_june.csv posts
.import ./with_user_data_aita_posts_19_june.csv posts
.import ./with_user_data_aita_posts_20_june.csv posts
.import ./with_user_data_aita_posts_21_june.csv posts
.import ./with_user_data_aita_posts_22_june.csv posts
.import ./with_user_data_aita_posts_23_june.csv posts
.import ./with_user_data_aita_posts_24_june.csv posts
.import ./with_user_data_aita_posts_25_june.csv posts
.import ./with_user_data_aita_posts_26_june.csv posts
.import ./with_user_data_aita_posts_27_june.csv posts
.import ./with_user_data_aita_posts_28_june.csv posts
.import ./with_user_data_aita_posts_29_june.csv posts
.import ./with_user_data_aita_posts_30_june.csv posts
