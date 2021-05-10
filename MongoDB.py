from pymongo import MongoClient


class MongoDB:
    def __init__(self, db_name):
        # Provide MongoDb hostname, username and password
        self.client = MongoClient('mongodb+srv://<username>:<password>@<hostname>')
        self.db = self.client[db_name]

    def insert_record(self, record, collection_name):
        collection = self.db[collection_name]
        collection.insert_one(record)

    def insert_many_records(self, list_of_records, collection_name):
        collection = self.db[collection_name]
        collection.insert_many(list_of_records)

    def fetch_records(self, collection_name):
        collection = self.db[collection_name]
        document = collection.find()
        return document

    def list_of_collections(self):
        return self.db.list_collection_names()

