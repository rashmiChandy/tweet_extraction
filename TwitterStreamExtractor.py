from tweepy import Stream
from TwitterAuthentication import TwitterAuthentication
from TwitterStreamListener import TwitterStreamListener


class TwitterStreamExtractor:

    def __init__(self):
        self.no_of_tweets = 2000
        self.twitter_stream_listener = TwitterStreamListener(self.no_of_tweets)
        authentication = TwitterAuthentication()
        self.auth = authentication.authentication_Handler()
        # Establishing connection Twitter API
        self.stream = Stream(self.auth, self.twitter_stream_listener)
        self.search_keywords = ["Storm", "Winter", "Canada", "Temperature", "Flu", "Snow", "Indoor", "Safety"]

    def extract_tweets_from_stream(self):
        self.call_stream()
        twitter_dict = self.twitter_stream_listener.data_in_pipeline
        self.twitter_stream_listener.mongoDb.insert_many_records(twitter_dict, "Stream_Collection")

    def call_stream(self):
        self.stream.filter(track=self.search_keywords, languages=["en"])
        if self.twitter_stream_listener.counter < self.no_of_tweets:
            self.call_stream()