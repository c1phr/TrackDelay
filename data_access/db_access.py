import os
from pymongo import MongoClient


class MongoDbClient:
    def __init__(self):
        self.client = MongoClient(os.environ['DB_PORT_27017_TCP_ADDR'],  27017)

    def add_records(self, records):
        collection = self.client.track_delay.delays
        for rec in records:
            collection.update({'_id': rec['_id']}, rec, upsert=True)
