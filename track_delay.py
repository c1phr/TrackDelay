#!/usr/bin/env python
from __future__ import print_function

import datetime
import logging
from urllib2 import URLError
from data_access import dynamo_data_access

import alert_scanner
from data_models import DelayModel


class TrackDelay(object):
    def run(self):
        logging.basicConfig(filename="log.log", level=logging.DEBUG)
        logging.info("Starting run at:" + datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y"))
        print("Starting run at:" + datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y"))
        self.process_delays()

    def process_delays(self):
        disabled_train_alerts = None
        dal = dynamo_data_access.DynamoDataAccess("track_delay")
        retry_count = 3
        while retry_count > 0:
            try:
                disabled_train_alerts = alert_scanner.AlertScanner.get_alerts(None)
            except URLError:
                retry_count -= 1
                logging.info("Retrying, connection error")

            if disabled_train_alerts is not None:
                retry_count = 0  # Stop retrying
                records = []
                for alert in disabled_train_alerts:
                    record = DelayModel.to_delay_dict(alert)
                    records.append(record)
                    dal.add_delay_record(record)
            else:
                retry_count -= 1
                logging.info("Retrying, disabled_train_alerts is empty")
        if retry_count == 0:
            logging.info("Error, retries failed. Sleeping until next run")

if __name__ == "__main__":
    td = TrackDelay()
    td.run()

def lambda_handler(event, context):
    td = TrackDelay()
    td.run()