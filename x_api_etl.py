#Importing all the necessary packages
import pandas as pd
import tweepy #Package for accessing X(twitter) data
import json
from datetime import datetime
import s3fs  #Used to store, read or write data from the S3 bucket

access_key = "11j4gpdgM2YfVidG67H9D5zxL"
access_secret = "TV1hIodkjKyIxUqk9hebzv9HHOvCjL39jMDsceoEpCU13zw5Bx"
consumer_key = "1864626832429207556-JPYsu2JKSndgp4N8Tjfp7i8JfYZ9TP"
consumer_secret = "LWvM8FudT8s4ltGWp8GAnpcnvw3LFaDxlo0ZzlEjupgsm"

#X authentication (Connection between my code and X api)
auth = tweepy.OAuthHandler(access_key, access_secret)
auth.set_access_token(consumer_key, consumer_secret)

#Creating API object
api = tweepy.API(auth)

tweets = api.user_timeline(
    screen_name ='@elonmusk',
    count = 100,
    include_rts = False,
    tweet_mode = 'Extended'
)

tweet_list = []
for tweet in tweets:
    text = tweet._json['full_text']

    refined_tweet = {
        "user": tweet.user.screen_name,
        "text": text,
        "favorite_count": tweet.favorite_count,
        "retweet_count": tweet.retweet_count,
        "created_at": tweet.created_at
    }
    tweet_list.append(refined_tweet)

#Converting extracted info to Pandas Dataframe
df = pd.DataFrame(tweet_list)
df.to_csv("Twitter_data.csv")