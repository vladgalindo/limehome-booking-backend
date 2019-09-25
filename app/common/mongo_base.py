from pymongo import MongoClient
from app import app


class MongoBase(object):
    def __init__(self, uri=app.config['MONGO_URI']):
        mongo_bd_conn = MongoClient(uri, retryWrites=False)
        self.mongo_db = mongo_bd_conn[app.config['DB_NAME']]

    def get(self, collection_name, query):
        try:
            pointer = self.mongo_db[collection_name].find(query)
            count = self.mongo_db[collection_name].count_documents(filter=query)
            return count, list(pointer)
        except Exception as err:
            print('Something went wrong fetching from MongoDB Database', err)

    def insert(self, collection_name, documents):
        try:
            collection = self.mongo_db[collection_name]
            if isinstance(documents, list):
                _id = collection.insert_many(documents).inserted_ids
            else:
                _id = collection.insert_one(documents).inserted_id
            return _id
        except Exception as err:
            print('Something went wrong saving at MongoDB Database', err)

    def update(self, collection_name, query, value):
        try:
            if isinstance(value, list):
                self.mongo_db[collection_name].update_many(query, value)
            else:
                self.mongo_db[collection_name].update_one(query, value)
        except Exception as err:
            print('Something went wrong updating at MongoDB Database', err)

    def delete(self, collection_name, query):
        try:
            self.mongo_db[collection_name].update_many(query, {"$set": {"meta.is_deleted": True}})
        except Exception as err:
            print('Something went wrong deleting from MongoDB Database', err)