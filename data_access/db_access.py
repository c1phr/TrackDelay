from pymongo import MongoClient


class MongoDbClient:
    def __init__(self):
        self.client = MongoClient('127.0.0.1',  27017)

    def add_records(self, records):
        collection = self.client.track_delay.delays
        for rec in records:
            collection.update({'_id': rec['_id']}, rec, upsert=True)
