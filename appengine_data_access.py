from google.appengine.ext import ndb


class AppEngineDataAccess(object):
    def add_delay_record(self, record):
        record.put()

    def add_all_records(self, records):
        ndb.put_multi(records)