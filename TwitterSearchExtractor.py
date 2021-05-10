import tweepy
from tweepy import Cursor
from MongoDB import MongoDB
from TwitterAuthentication import TwitterAuthentication


class TwitterSearchExtractor:
    def __init__(self):
        twitter_authentication = TwitterAuthentication()
        self.auth = TwitterAuthentication.authentication_Handler(twitter_authentication)
        self.api = tweepy.API(self.auth)
        self.search_keywords = ["Storm", "Winter", "Canada", "Temperature", "Flu", "Snow", "Indoor", "Safety"]
        self.mongoDb = MongoDB("RawDb")

    def extract_tweets_from_search(self):
        for word in self.search_keywords:
            tweets = []
            tweets_cursor = Cursor(self.api.search, q=word, lang="en").items(300)

            for tweet in tweets_cursor:
                tweets.append(tweet._json)
            self.mongoDb.insert_many_records(tweets, "Search_Collection")
