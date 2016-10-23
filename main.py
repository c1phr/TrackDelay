#!/usr/bin/env python

import webapp2

from track_delay import TrackDelay


class MainHandler(webapp2.RequestHandler):
    def get(self):
        td = TrackDelay()
        td.run()

app = webapp2.WSGIApplication([
    ('/getData', MainHandler)
], debug=True)
