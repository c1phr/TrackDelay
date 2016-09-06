#!/usr/bin/env python
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
        self.process_delays()

    def process_delays(self):
        dal = data_access.DataAccess()
        disabled_train_alerts = alert_scanner.AlertScanner.get_alerts()
        for alert in disabled_train_alerts:
            record = delay_dict.to_delay_dict(alert)
            dal.add_delay_record(record)

while True:
    td = TrackDelay()
    td.run()
    time.sleep(600)
