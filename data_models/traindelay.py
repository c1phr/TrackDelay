from google.appengine.ext import ndb


class TrainDelay(ndb.Model):
    severity = ndb.TextProperty()
    line = ndb.TextProperty()
    branch = ndb.TextProperty()
    start_time = ndb.TextProperty()
    end_time = ndb.TextProperty()
    header_text = ndb.TextProperty()
    cause = ndb.TextProperty()
