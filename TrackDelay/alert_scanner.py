from __future__ import print_function
import requests
import api_key


class AlertScanner(object):
    def get_alerts(self):
        url = "http://realtime.mbta.com/developer/api/v2/alerts?api_key={0}&include_access_alerts=false&format=json".format(
            api_key.get_key())
        full_data = requests.get(url)
        if full_data.status_code == requests.codes.ok:
            full_data_json = full_data.json()
            delay_data = [obj for obj in full_data_json["alerts"] if
                          "cause_name" in obj and obj["cause_name"] == "disabled train"]
            return delay_data


scanner = AlertScanner()
scanner.get_alerts()
