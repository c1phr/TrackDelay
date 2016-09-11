#!/usr/bin/env python
from __future__ import print_function
import alert_scanner
import delay_dict
import data_access
import logging
import datetime
import time


class TrackDelay(object):
    def run(self):
        logging.basicConfig(filename="log.log", level=logging.DEBUG)
        logging.info("Starting run at:" + datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y"))
        print("Starting run at:" + datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y"))
        self.process_delays()

    def process_delays(self):
        dal = data_access.DataAccess()
        retry_count = 3
        while retry_count > 0:
            disabled_train_alerts = alert_scanner.AlertScanner.get_alerts()
            if disabled_train_alerts is not None:
                retry_count = 0 # Stop retrying
                for alert in disabled_train_alerts:
                    record = delay_dict.to_delay_dict(alert)
                    dal.add_delay_record(record)
            else:
                retry_count -= 1
                logging.info("Retrying, disabled_train_alerts is empty")
        if retry_count == 0:
            logging.info("Error, retries failed. Sleeping until next run")

td = TrackDelay()
while True:
    td.run()
    time.sleep(600)
