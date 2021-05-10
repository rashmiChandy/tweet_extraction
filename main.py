from FetchRecords import FetchRecords
from TwitterSearchExtractor import TwitterSearchExtractor
from TwitterStreamExtractor import TwitterStreamExtractor

if __name__ == '__main__':
    twitter_search_extractor = TwitterSearchExtractor()
    twitter_search_extractor.extract_tweets_from_search()
    twitter_stream_extractor = TwitterStreamExtractor()
    twitter_stream_extractor.extract_tweets_from_stream()
    fetchRecord = FetchRecords()
    fetchRecord.fetch_tweets()
