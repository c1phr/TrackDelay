#!/usr/bin/env python

import webapp2
import json

import appengine_data_access
from data_models.traindelay import TrainDelay
from track_delay import TrackDelay


class MainHandler(webapp2.RequestHandler):
    def get(self):
        td = TrackDelay()
        td.run()


class SqlDataAdapter(webapp2.RequestHandler):
    def post(self):
        data_arr = json.loads(self.request.body)
        delay_arr = []
        dal = appengine_data_access.AppEngineDataAccess()
        for record in data_arr:
            print(record)
            train_delay = TrainDelay(id=str(record["alert_id"]))
            train_delay.severity = record["severity"]
            train_delay.line = record["line"]
            train_delay.branch = record["branch"]
            train_delay.start_time = str(record["start_time"])
            train_delay.end_time = str(record["end_time"]) if record["end_time"] is not None else None
            train_delay.header_text = record["header_text"]
            train_delay.cause = record["cause"]
            delay_arr.append(train_delay)
        return "Added " + dal.add_all_records(delay_arr)


app = webapp2.WSGIApplication([
    ('/getData', MainHandler),
    ('/merge', SqlDataAdapter)
], debug=True)
