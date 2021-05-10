from DictionaryCleaning import DictionaryCleaning
from MongoDB import MongoDB


class FetchRecords:

    def fetch_tweets(self):
        mongoDb = MongoDB("RawDb")
        collections = mongoDb.list_of_collections()
        for collection_name in collections:
            collection_list = []
            for record in mongoDb.fetch_records(collection_name):
                dictionary_cleaning = DictionaryCleaning()
                dictionary_cleaning.clean_dictionary(record)
                collection_list.append(record)
            self.insert_processed_db(collection_list,collection_name)

    def insert_processed_db(self, collection_list,collection_name):
        processed_db = MongoDB("ProcessedDb")
        processed_db.insert_many_records(collection_list, collection_name)

