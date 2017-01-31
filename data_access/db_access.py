import pymysql.cursors

def getConn():
    return pymysql.connect(
    host='localhost',
    user='delayuser',
    db='track_delay',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

def saveDelay(delay):
