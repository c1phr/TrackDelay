#!/usr/bin/env python
import sqlite3
import logging
import json


class SqlDataAccess(object):
    def __init__(self):
        if not self.table_exists():
            self.create_table()
        super(SqlDataAccess, self).__init__()

    def add_delay_record(self, record_dict):
        existing_record = self.execute_command("SELECT ALERT_ID FROM TRAIN_DELAY WHERE ALERT_ID = ?",
                                               (record_dict["alert_id"],))
        if existing_record:
            self.execute_command(
                "UPDATE TRAIN_DELAY SET SEVERITY = ?, START_TIME = ?, END_TIME = ?, HEADER_TEXT = ? WHERE ALERT_ID = ?",
                (
                    record_dict["severity"], record_dict["start_time"], record_dict["end_time"],
                    record_dict["header_text"], record_dict["alert_id"]))
        else:
            logging.debug("Inserting record: " + str(record_dict))
            self.execute_command("INSERT INTO TRAIN_DELAY \
                                  (ALERT_ID, SEVERITY, LINE, BRANCH, START_TIME, END_TIME, HEADER_TEXT, CAUSE) VALUES\
                                    (?, ?, ?, ?, ?, ?, ?, ?)", (
                record_dict["alert_id"], record_dict["severity"], record_dict["line"], record_dict["branch"],
                record_dict["start_time"], record_dict["end_time"], record_dict["header_text"], record_dict["cause_name"]))

    def create_table(self):
        logging.debug("Creating table")
        self.execute_command('''CREATE TABLE IF NOT EXISTS TRAIN_DELAY
                            (
                              ID INTEGER PRIMARY KEY,
                              ALERT_ID INTEGER NOT NULL,
                              SEVERITY TEXT NOT NULL,
                              LINE TEXT NOT NULL,
                              BRANCH TEXT NULL,
                              START_TIME INTEGER NOT NULL,
                              END_TIME INTEGER NULL,
                              HEADER_TEXT TEXT NULL,
                              CAUSE TEXT NULL
                            );''')

    def table_exists(self):
        return bool(self.execute_command("SELECT name FROM sqlite_master WHERE type='table' AND name='TRAIN_DELAY'"))

    def get_all_rows_json(self):
        data = self.execute_command("SELECT ALERT_ID, SEVERITY, LINE, BRANCH, START_TIME, END_TIME, HEADER_TEXT, CAUSE from TRAIN_DELAY")
        data_dict_arr = []
        for record in data:
            data_dict = {"alert_id": record[0], "severity": record[1], "line": record[2], "branch": record[3],
                         "start_time": record[4], "end_time": record[5], "header_text": record[6], "cause": record[7]}
            data_dict_arr.append(data_dict)
        return json.dumps(data_dict_arr)


    @staticmethod
    def execute_command(cmd, params=()):
        logging.debug("Attempting to execute SQL: " + cmd + " PARAMETERS: " + str(params))
        conn = sqlite3.connect("../data.db")
        output = conn.execute(cmd, params).fetchall()
        conn.commit()
        conn.close()
        return output
