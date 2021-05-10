from tweepy.streaming import StreamListener
import json
from MongoDB import MongoDB


class TwitterStreamListener(StreamListener):

    def __init__(self, num_of_tweets_to_grab):
        super().__init__()
        self.counter = 0
        self.num_of_tweets_to_grab = num_of_tweets_to_grab
        self.mongoDb = MongoDB("RawDb")
        self.data_in_pipeline = []

    def on_data(self, data):
        self.counter += 1
        twitter_dict = json.loads(data)
        self.data_in_pipeline.append(twitter_dict)

        if self.counter > self.num_of_tweets_to_grab:
            return False
        return True

    def on_error(self, status_code):
        if status_code == 420:
            return False