#!/usr/bin/env python

import webapp2
import logging

from data_models.traindelay import TrainDelay
from track_delay import TrackDelay
from google.appengine.ext import deferred, ndb

class MainHandler(webapp2.RequestHandler):
    def get(self):
        td = TrackDelay()
        td.run()

app = webapp2.WSGIApplication([
    ('/getData', MainHandler)
], debug=True)
