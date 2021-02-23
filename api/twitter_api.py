import os
import tweepy
import datetime
import json


class TwitterAPI:
    """."""

    def __init__(self):
        consumer_key = os.getenv('CONSUMER_KEY')
        consumer_secret = os.getenv('CONSUMER_SECRET')
        self.api = tweepy.API(tweepy.OAuthHandler(consumer_key, consumer_secret))


    def get_user(self, user_name: str) -> bool:
        user = self.api.get_user(user_name)
        return user


    def from_user_tweet(self, user_name: str):
        query = f'from:{user_name}'
        return self.api.search(q=query, count=1)


    def get_24h_tweet_user(self, user_name: str) -> [int, int]:
        yesterday_utc = datetime.datetime.now() + datetime.timedelta(days=-1)
        tweet_count = 0
        retweet_count = 0
        max_id = None

        while True: 
            user_timeline = self.api.user_timeline(screen_name=user_name, include_rts=True, max_id=max_id)
            for tweet in user_timeline:
                try:
                    if yesterday_utc <= tweet.created_at:
                        tweet_count += 1
                    if tweet.retweeted_status:
                        retweet_count += 1
                except AttributeError:
                    pass
                max_id = tweet.id - 1
            
            if user_timeline[len(user_timeline) - 1].created_at < yesterday_utc:
                break
        
        return tweet_count, retweet_count
