import sqlite3


class DataAccess(object):
    def __init__(self):
        if not self.table_exists():
            self.create_table()
        super(DataAccess, self).__init__()

    def add_delay_record(self, record_dict):
        self.execute_command("INSERT INTO TRAIN_DELAY \
                              (ALERT_ID, SEVERITY, LINE, BRANCH, START_TIME, END_TIME, HEADER_TEXT, DESCR_TEXT) VALUES\
                                (?, ?, ?, ?, ?, ?, ?, ?)", (
            record_dict["alert_id"], record_dict["severity"], record_dict["line"], record_dict["branch"],
            record_dict["start_time"], record_dict["end_time"], record_dict["header_text"], record_dict["descr_text"]))

    def table_exists(self):
        cursor = self.execute_command("SELECT * FROM sqlite_master WHERE type='table' AND name='TRAIN_DELAY'")
        return len(cursor) == 1

    def create_table(self):
        self.execute_command('''CREATE TABLE TRAIN_DELAY
                            (
                              ID INT PRIMARY KEY NOT NULL,
                              ALERT_ID INT NOT NULL,
                              SEVERITY TEXT NOT NULL,
                              LINE TEXT NOT NULL,
                              BRANCH TEXT NULL,
                              START_TIME INT NOT NULL,
                              END_TIME INT NULL,
                              HEADER_TEXT TEXT NULL,
                              DESCR_TEXT TEXT NULL
                            )''')

    @staticmethod
    def execute_command(cmd, params=()):
        conn = sqlite3.connect("data.db")
        output = conn.execute(cmd, params)
        conn.close()
        return output
