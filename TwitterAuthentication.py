import tweepy
import TwitterCredentials


class TwitterAuthentication:

    def authentication_Handler(self):
        auth = tweepy.OAuthHandler(TwitterCredentials.consumer_key, TwitterCredentials.consumer_secret)
        auth.set_access_token(TwitterCredentials.access_key, TwitterCredentials.access_secret)
        return auth
