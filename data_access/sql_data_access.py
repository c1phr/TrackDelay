#!/usr/bin/env python
import sqlite3
import logging


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
        self.execute_command('''CREATE TABLE delay
                            (
                              id INTEGER PRIMARY KEY,
                              alert_id INTEGER NOT NULL,
                              severity TEXT NOT NULL,
                              line TEXT NOT NULL,
                              branch TEXT NULL,
                              start_time INTEGER NOT NULL,
                              end_time INTEGER NULL,
                              header_text TEXT NULL,
                              cause TEXT NULL
                            );''')

    def table_exists(self):
        return bool(self.execute_command("SELECT name FROM sqlite_master WHERE type='table' AND name='TRAIN_DELAY'"))


    @staticmethod
    def execute_command(cmd, params=()):
        logging.debug("Attempting to execute SQL: " + cmd + " PARAMETERS: " + str(params))
        conn = sqlite3.connect("../data.db")
        output = conn.execute(cmd, params).fetchall()
        conn.commit()
        conn.close()
        return output
